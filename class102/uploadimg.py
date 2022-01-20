import cv2
import dropbox
import time
import random

start_time = time.time()


def capture_image():
    number = random.randint(0,100)
    #init the cv2 with the object
    capture_picture = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = capture_picture.read()
        image_name = "img"+str(number)+".png"
        cv2.imwrite(image_name, frame)
        start_time = time.time
        result = False
    
   
    #releaseing the object
    capture_picture.release()
    cv2.DestroyAllWindows()
    return image_name

#capture_image()

def upload_file(img_name):
    access_token = "vvFasVSIxVkAAAAAAAAAATebr-guDg4qCJTXBF4pDg4b9hZW33WmV1HmZ58BNwmQ"
    file =img_name
    file_from = file
    file_to="/c101cs/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = capture_image()
            upload_file(name)

main()
