import cv2

def capture_image():
    #init the cv2 with the object
    capture_picture = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = capture_picture.read()
        cv2.imwrite("picture1.jpg", frame)
        result = False
    
    #releaseing the object
    capture_picture.release()
    cv2.DestroyAllWindows()


capture_image()