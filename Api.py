
from detect_my_picture import detect 
from fastapi import FastAPI
from typing import Union
from decocing_base64 import decoding

app = FastAPI()



@app.get("/solve_captcha")
def get_code(image_base64: str):
    decoding(image_base64)
    
    captcha_number = detect('SelfMe/captcha/yolov5/picture/picture1.jpg')
    return {"code":captcha_number}




