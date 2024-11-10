from detect_my_picture import detect 
from fastapi import FastAPI
from  pydantic import BaseModel 
from decocing_base64 import decode_image
import uvicorn



app = FastAPI()

class Image(BaseModel):
    base64 : str


@app.post("/solve_captcha/")
def get_code(image: Image):
    
    
    print(image.base64)
    print(decode_image(image.base64))

    
    captcha_number = detect('/home/mmd/vscode/model/solve_captcha/pic/pic.jpg')
    return {"code":captcha_number}


uvicorn.run(app,port=3000)



