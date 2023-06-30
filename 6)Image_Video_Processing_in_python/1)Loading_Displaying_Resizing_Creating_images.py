#You have to open image using opencv.
import cv2

img=cv2.imread("galaxy.jpg",1)
# 0 means it is grey scale and 1 means colour.

print(img)
print(img.shape)
#This shows the resolution of the image.
print(img.ndim)
#this checks the dimensions of the array

resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
#if you remove divided by 2 you will see the original image.
#with this resized image you can edit it to fit your screen.
#in order for to see original image but not streched image you can divide the shape by 2.

cv2.imshow("Galaxy",resized_image)
#this shows image on the screen whether it is grey scale or color.

cv2.waitKey(0)
#if you put zero next to waitkey this means if you press any button the window closes
#if you place time there in milliseconds which is 2000(2 secods.) then it automatically closes the window after two seconds.
#Lets save the new resized image
 
cv2.imwrite("Galaxy_resized.jpg",resized_image)
cv2.destroyAllWindows() 