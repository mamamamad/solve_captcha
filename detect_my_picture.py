import numpy as np
from yolov5.detect import run
from os import walk
import os
import shutil



def detect(picture_path):
  '''this function detect the numbers in an image based on the image path.'''
  number_detect = ''
  try:
    path_save='/home/mmd/vscode/model/SelfMe/captcha/yolov5/runs/detect/exp9'
    run(weights="/home/mmd/vscode/model/SelfMe/captcha/yolov5/runs/train/captcha_detection/weights/best.pt",
    source=picture_path,
    imgsz=(450,450),
    conf_thres=0.25,
    save_txt=True,
    save_crop=True,
    project=path_save
    )
    
  
    path=f"/home/mmd/vscode/model/SelfMe/captcha/yolov5/runs/detect/exp9/exp/labels"
    for file in os.listdir(path):
      my_file=np.loadtxt(os.path.join(path,file))
      ff=sorted(my_file,key=lambda x:x[1])
      number_detect +=(np.array(ff)[:,0].astype(int).astype(str))
    shutil.rmtree('/home/mmd/vscode/model/SelfMe/captcha/yolov5/runs/runs/detect/exp9/exp',ignore_errors=True)
    return number_detect
    
    
  except:
    print('eroooor')
    return number_detect 
    
print(detect('/home/mmd/vscode/model/SelfMe/captcha/yolov5/picture/picture1.jpg'))  
  

  









