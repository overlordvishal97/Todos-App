import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("news.jpg")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.1,
minNeighbors=5)
#you can adjust the scale factor if you want to correct the program of face detection.
for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)
    #you have to change the gray image to img if you want to see the colour image in the imshow.

print(type(faces))
print(faces)

resized= cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
#with this you can resize the image for the image to display properly.
#And if you want to use the resized image then call it in imshow.

#you can resize the image if it doesn't fit the screen.
#you can use colour but using grey scale image increases accuracy.
#as opencv might not work well when the image has lot of features. 
cv2.imshow("Gray",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
#lets try testing this program with an image which doesn't have a clear distinction for python to recognise it as face.
#lets change the image to img.jpg -> news.jpg.