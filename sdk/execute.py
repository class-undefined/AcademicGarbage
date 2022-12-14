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
    print(stdout)
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

def upload(id: str, address: str):
    """id: 需要通知的用户id, address: 传输的api地址"""
    import requests
    

def identify(url: str):
    import os
    YOLOV5_PT = os.getenv("YOLOV5_PT")
    YOLOV5_DETECT = os.getenv("YOLOV5_DETECT")
    YOLOV5_DETECT_ARGS = os.getenv("YOLOV5_DETECT_ARGS")
    command = f"python {YOLOV5_DETECT} --weights {YOLOV5_PT} --source {url} {YOLOV5_DETECT_ARGS}"
    log = execute(command)
    pwd = execute("pwd").replace("\n", "")
    lines = log.split("\n")
    detect_path = lines[0]
    workspace = f"{pwd}/{detect_path}"
    print(workspace)
    
identify("https://bins-1.oss-cn-hangzhou.aliyuncs.com/I.jpeg")
