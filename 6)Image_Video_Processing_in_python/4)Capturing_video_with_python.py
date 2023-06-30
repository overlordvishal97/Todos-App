import cv2, time
from cv2 import cvtColor
video=cv2.VideoCapture(0)
a=1
while True:
    a=a+1
    check, frame = video.read()
#'check' is a boolean type and frame is a numpy array.
#you check it by printing them seprately.
    print(check)
    print(frame)
#you can even make it to show in gray.
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#you just have to replace the frame in imshow for it to show the grey image.
    #time.sleep(2)
    #you just have to comment out the time.sleep for it to turn into video.
#makes the video to stop running for the required amount of time.
    cv2.imshow("Capturing",gray)
#this shows the video which being recorded.
    key=cv2.waitKey(1)
    
    if key ==ord('q'):
        break
    #if you press 'q' key when the code is running then it will break the code.
#2000 milli seconds which is 2 seconds.
#0 in waitkey means it will drop with any key.
#this gives the option to exit all windows with a press of a button.
print(a)
#how many frames or iterations are being generated. can be known using this method.
video.release()
cv2.destroyAllWindows() 
#closes the webcam or cancels the video.