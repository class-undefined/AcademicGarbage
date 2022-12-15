import datetime
from typing import Dict, Union
from flask import Blueprint, request
from common.error import RequestError
from common.response import Response
from common import get_cache, get_socketio, get_oss
from db.photo import Photo
from common.package import debug
from services.interceptor import interceptor

middle_blue = Blueprint("middle", __name__, url_prefix="/middle")

"""
```
body:
{
    "user_id",
    "photo_id",
    "identify": {
        "filename",
        "process_img",
        "result": [
            "bbox",
            "accuracy_rate"
        ]
    }
}
```
"""
@middle_blue.route("/identify_result", methods=["POST", "GET"])
@interceptor()
def identify_result():
    import json
    body = request.form
    user_id = body["user_id"]
    photo_id = body["photo_id"] # 处理的图像id
    filename = body["filename"]
    process_img = body["process_img"] # 二进制数据
    result = json.loads(body["result"]) # 识别结果
    sid = get_cache().pull("user", user_id) # 用户的sid
    debug("sid", sid, "user_id", user_id)
    processed_url = get_oss().upload(f"{user_id}/processed_{filename}", open(process_img, "rb"))
    photo: Photo = Photo.query_by_id(id=photo_id)
    if photo is None or process_img is None or result is None or len(result) == 0:
        data =  {"photo_id": photo_id, "data": None}
        response = Response.error(data=data)
        get_socketio().emit("accept_identify_rst", response.to_dict(), room=sid)
        return response
    else:
        photo.processed_url = processed_url
        photo.helmets_count = len(result)
        accuracy_rate = 0
        for record in result:
            accuracy_rate += record["accuracy_rate"]
        accuracy_rate /= len(result)
        photo.accuracy = accuracy_rate # 取平均
        photo.update_time = datetime.datetime.utcnow()
        photo.save()
        data =  {"photo_id": photo_id, "data": photo.to_dict()}
        response = Response.ok(data=data)
        get_socketio().emit("accept_identify_rst", response.to_dict(), room=sid)
        return response
