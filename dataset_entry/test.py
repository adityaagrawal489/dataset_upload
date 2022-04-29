import base64
import os
def save_img(name):
    print(os.getcwd())
    with open('sanju.txt', 'r') as file:
        imgstring = file.read().replace('\\n', '').replace('\\','').replace("b'",'')
        imgstring = imgstring + '=' * (4 - len(imgstring) % 4)
    #take care of padding
    

    imgstring = bytes(imgstring,'utf8')
    # print(imgstring)
    filename = 'some_image5.jpg' 
    # with open(filename, 'wb') as f:
    #     f.write(imgstring)
        
    imgdata = base64.b64decode(imgstring)
   
    with open(filename, 'wb') as f:
        f.write(imgdata) 

save_img('sanju')