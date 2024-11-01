import numpy as np
from yolov5.detect import run
from os import walk
import os
import json
import shutil


with open("/home/mmd/vscode/model/solve_captcha/path.json",'r') as file:
  path_m = json.load(file)
print(path_m["save_path"])

def detect(picture_path):
  '''this function detect the numbers in an image based on the image path.'''
  number_detect = ''
  try:
    path_save=path_m['save_path'] # the path to save the processed data.
    run(weights=path_m['model_save'], # model path
    source=picture_path,
    imgsz=(450,450),
    conf_thres=0.25,
    save_txt=True,
    save_crop=True,
    project=path_save
    )
    
  
    path= path_m["load_model"] 
    for file in os.listdir(path):
      my_file=np.loadtxt(os.path.join(path,file))
      ff=sorted(my_file,key=lambda x:x[1])
      x = (np.array(ff)[:,0].astype(int).astype(str))
    for i in x:
      if i =='10':
        number_detect += '9' # Because the model detects the number 9 as 10.
      else:
        number_detect+=i
    # shutil.rmtree('/home/mmd/vscode/model/SelfMe/captcha/yolov5/runs/runs/detect/exp9/exp',ignore_errors=True) #delete folder
    return number_detect
    
    
  except:
    print('eroooor')
    return number_detect 
    
print(detect('/home/mmd/Captcha.jpg'))  
  

  









