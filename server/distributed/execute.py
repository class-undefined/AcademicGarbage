from typing import Dict, Union
import ray
import yaml
config = yaml.load(open("/home/class-undefined/code/AcademicGarbage/server/distributed/config.yaml", "rb"), yaml.SafeLoader)
def execute(cmd: str):
    import subprocess
    process = subprocess.Popen(
        cmd,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate()
    stdout = stdout.decode("utf8").replace("\\n", "\n").replace("\\t", "\t")
    stderr = stderr.decode("utf8")
    if (
        stderr.find("Error") >= 0
        or stderr.find("ERROR:") >= 0
        or stderr.find("fatal error") >= 0
    ):
        raise Exception(f"Error executing: {cmd}, error: {stderr}")
    process.wait()
    return stdout

def get_filename(path: str) -> str:
    last = len(path) - 1
    filename = ""
    split = ["\\", "/"]
    while last >= 0:
        if path[last] in split:
            break
        filename = path[last] + filename
        last -= 1
    return filename

    
def parse_identify_result_txt(path: str):
    """解析识别结果的txt文本, 转为Dict"""
    data = []
    with open(path, "r", encoding="utf8") as f:
        while True:
            line = f.readline()
            if line == "":
                break
            cols = line.split(" ")
            bbox = [float(cols[1]), float(cols[2]), float(cols[3]), float(cols[4])]
            accuracy_rate = float(cols[5])
            data.append({"bbox": bbox, "accuracy_rate": accuracy_rate})
    return data
        
        
def parse_identify_result(workspace: str):
    """解析识别结果"""
    import os
    names = os.listdir(workspace)
    process_img = None
    result = None
    filename = None
    for name in names:
        path = os.path.join(workspace, name)
        if os.path.isfile(path): # 如果是文件,则是处理后的图片
            process_img = path
            filename = name
            continue
        if os.path.isdir(path) and name == "labels":
            rsts = os.listdir(path)
            if len(rsts) != 0:
                rst_path = os.path.join(path, rsts[0]) # 检测结果文件
                result = parse_identify_result_txt(rst_path)
    if process_img is not None: # 转为二进制数据
        process_img = open(process_img, "rb").read()
    return {"filename": filename, "process_img": process_img, "result": result}


def identify(url: str, envs: Union[Dict, None]=None):
    """识别图片中的安全帽"""
    import os
    YOLOV5_PT = os.getenv("YOLOV5_PT") or envs is not None and envs["YOLOV5_PT"]
    YOLOV5_DETECT = os.getenv("YOLOV5_DETECT") or envs is not None and envs["YOLOV5_DETECT"]
    YOLOV5_DETECT_ARGS = os.getenv("YOLOV5_DETECT_ARGS") or envs is not None and envs["YOLOV5_DETECT_ARGS"]
    if YOLOV5_PT is None or YOLOV5_DETECT is None or YOLOV5_DETECT_ARGS is None:
        raise Exception("环境遍历错误, ray没有对其进行导入")
    command = f"python {YOLOV5_DETECT} --weights {YOLOV5_PT} --source {url} {YOLOV5_DETECT_ARGS}"
    log = execute(command)
    pwd = execute("pwd").replace("\n", "")
    lines = log.split("\n")
    detect_path = lines[0]
    workspace = f"{pwd}/{detect_path}"
    return parse_identify_result(workspace)

def upload(user_id: str, photo_id: str, original_url: str, envs: Union[Dict, None]=None):
    """userid: 需要通知的用户id, photo_id: 处理的图片id, original_url: 图片url地址"""
    import requests
    import json
    print("ray出手了")
    url = f"http://172.17.0.5:5001/middle/identify_result"
    identify_result = identify(original_url, envs=envs)
    identify_result["result"] = json.dumps(identify_result["result"])
    identify_result.update({
        "user_id": user_id,
        "photo_id": photo_id,
    })
    response = requests.post(url, data=identify_result) # 提交即可
    response.raise_for_status()

@ray.remote(num_cpus=1, runtime_env={"env_vars": config})
def identify_async(user_id: str, photo_id: str, original_url: str):
    import asyncio
    asyncio.run(upload(user_id, photo_id, original_url))

def wrap_identify(user_id: str, photo_id: str, original_url: str):
    import multiprocessing
    def worker():
        upload(user_id, photo_id, original_url)
    p = multiprocessing.Process(target=worker)
    p.start()
    # identify_async.remote(user_id, photo_id, original_url)

# rst = identify("https://bins-1.oss-cn-hangzhou.aliyuncs.com/I.jpeg")
# print(rst)
