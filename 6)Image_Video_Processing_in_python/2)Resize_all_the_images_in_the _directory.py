#Exercise: Batch image resizing.
"""
import cv2
import os 

for file in os.listdir("sample_images"):
    img=cv2.imread('sample_images\\'+ file,1)
    img_resized=cv2.resize(img,(100,100))
    cv2.imwrite(str("sample_images\\resized_images"+ file),img_resized)
"""
    
#this zip sample images are extracted into a folder called sample images and they are called as folder to make the code short.
#And resized everything present in the whole folder.
#And renamed them to resized images. 
#There is another method which is revealed in solution of this problem.
#Solution:Batch image Resizing.

import cv2
import glob

images=glob.glob("sample_images\\*.jpg")

for image in images:
    img=cv2.imread(image,1)
    re=cv2.resize(img,(500,500))
    cv2.imshow("Hey",re)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)

#the 27th line makes sure that after renaming the new file the name of the old file stays with the new file.
#The 22th line decides to use grey scales or colour scale.
# I  first created a list containing the image file paths and then iterated through the aforementioned list.
#The loop: reads each image, resizes, displays the image, waits for the user input key, closes the window once the key is pressed,
# and writes the resized image. The name of the resized image will be "resized" plus the existing file name of the original image. 