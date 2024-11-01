from PIL import Image
import base64
from io import BytesIO



def decoding(bs64:str):
    '''This function is for decoding a Base64 string into an image.'''
    try:
        image_data = base64.b64decode(bs64)
        image = Image.open(BytesIO(image_data))
        image.save("/home/mmd/vscode/model/SelfMe/captcha/yolov5/picture/picture1.jpg")
        return("success")
    except:
        return("erroooor in decoding")


    

    