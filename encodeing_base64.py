import base64
# from solve_captcha.decocing_base64 import decoding

def Encode_to_base64(path):
    try:
        with open(path,'rb')as image_file:
            base64_code_image = base64.b64encode(image_file.read())
            base64_code_string = base64_code_image.decode("utf-8") 
            return base64_code_string
    except FileNotFoundError:
        print("file not found")
        return None
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
image_path = '/home/mmd/Captcha.jpg'
en = Encode_to_base64(image_path)
print(en)



