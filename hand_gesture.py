# IMPORTING LIBRARIES
import numpy as np
import cv2
import os
import math
from random import seed
from random import randint
import threading
import time
import threading
import time
import vlc


p = vlc.MediaPlayer("Beat/Selena-Boyfriend.mp3")
p.play()

#window fit 
window_x = 340
window_y = 340
rows = 340
cols=340
channels=3

#cv2.namedWindow("Big picture")
#big_frame = m = np.zeros((window_y, window_x*3, 3), dtype=np.uint8)

#image function
num_list = ["sss"]
globalveriable = 1
def ImageDisplay():
    folder_path = 'display image/'
    for i in range (0,5):
        for path in os.listdir(folder_path):#loop to read one image at a time 
            imgpath = os.path.join(folder_path, path)
            num_list.insert(1, imgpath)
            frame = cv2.imread(imgpath, 1)
            '''width = 500
            height = 400
            dim = (width, height)
            frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)'''
            frame = cv2.resize(frame, (500, 400))
            cv2.imshow('Window', frame)
            #print(frame.shape)
            
            key = cv2.waitKey(6000)

def resizeFrame(frame):
    width = 500
    height = 400
    dim = (width, height)
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    return frame

threading.Thread(target=ImageDisplay).start()

            
#class
class hand(object):
		#LOADING HAND CASCADE
	hand_cascade = cv2.CascadeClassifier('hand_haar_cascade.xml')
	#threading.Thread(target=ImageChanger).start()

# VIDEO CAPTURE
	cap = cv2.VideoCapture(0)
	score = 0
	while 1:
		ret, img = cap.read()
		blur = cv2.GaussianBlur(img,(5,5),0) # BLURRING IMAGE TO SMOOTHEN EDGES
		#BGR->grey
		gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
		#threshold the image
		retval2,thresh1 = cv2.threshold(gray,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
		#detecting hand in threshold image
		hand = hand_cascade.detectMultiScale(thresh1, 1.3, 5)
		#create mask
		mask = np.zeros(thresh1.shape, dtype = "uint8")
		#detecting roi
		for (x,y,w,h) in hand:
			cv2.rectangle(img,(x,y),(x+w,y+h), (122,122,0), 2)
			cv2.rectangle(mask, (x,y),(x+w,y+h),255,-1)
		img2 = cv2.bitwise_and(thresh1, mask)
		final = cv2.GaussianBlur(img2,(7,7),0)
		contours, hierarchy = cv2.findContours(final, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

		cv2.drawContours(img, contours, 0, (255,255,0), 3)
		cv2.drawContours(final, contours, 0, (255,255,0), 3)
		#cv2.imshow('display',ImageDisplay(1))
		#print ("global",num_list)   


		if len(contours) > 0:
			cnt=contours[0]
			hull = cv2.convexHull(cnt, returnPoints=False)
			# finding convexity defects
			defects = cv2.convexityDefects(cnt, hull)
			count_defects = 0
			# applying Cosine Rule to find angle for all defects (between fingers)
			# with angle > 90 degrees and ignore defect
			if defects is not None:
				for i in range(defects.shape[0]):
					p,q,r,s = defects[i,0]
					finger1 = tuple(cnt[p][0])
					finger2 = tuple(cnt[q][0])
					dip = tuple(cnt[r][0])
					# find length of all sides of triangle
					a = math.sqrt((finger2[0] - finger1[0])**2 + (finger2[1] - finger1[1])**2)
					b = math.sqrt((dip[0] - finger1[0])**2 + (dip[1] - finger1[1])**2)
					c = math.sqrt((finger2[0] - dip[0])**2 + (finger2[1] - dip[1])**2)
					# apply cosine rule here
					angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57.29
					# ignore angles > 90 and highlight rest with red dots
					if angle <= 90:
						count_defects += 1
			# define actions required
			if count_defects == 1 and num_list[1]=="display image/two2.jpg":
				cv2.putText(img,"Correct!!! THIS IS 2", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
				score = score + 1
			elif count_defects==0 and num_list[1]=="display image/one.jpg":
				cv2.putText(img,"Correct!!! THIS IS 1", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
				score = score + 1
			elif count_defects == 2 and num_list[1]=="display image/three.jpg":
				cv2.putText(img, "Correct!!! THIS IS 3", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
				score = score + 1
			elif count_defects == 3 and num_list[1]=="display image/four.jpg":
				cv2.putText(img,"Correct!!! This is 4", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
				score = score + 1
			elif count_defects == 4 and num_list[1]=="display image/five.jpg":
				cv2.putText(img,"Correct!!! THIS IS 5", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
				score = score + 1
		#cv2.imshow('img',thresh1)
		#big_frame = m = np.zeros((window_y, window_x*3, 3), dtype=np.uint8)
		
		#cv2.imshow('img2',img2)

                #Adding 3rd channels to images
		cv2.imwrite('gray.jpg', img2)
		img2 = cv2.imread('gray.jpg')
		cv2.imwrite('img.jpg',thresh1)
		thresh1 = cv2.imread('img.jpg')
		
		#cv2.imshow('img1',img)
		#cv2.imshow('img',thresh1)
		#cv2.imshow('img2',img2)
		numpy_horizontal1  = np.hstack((resizeFrame(img2),resizeFrame(img)))
		numpy_horizontal2  = np.hstack((resizeFrame(img2),resizeFrame(thresh1)))
		numpy_vertical = np.concatenate((numpy_horizontal1, numpy_horizontal2))
                
		cv2.imshow("main",numpy_vertical)
		#cv2.imshow("maidcvn",numpy_horizontal2)
		#try fit 3 window
		'''frame1 = cv2.resize(img, (window_y, window_x))
		frame2 = cv2.resize(img2, (window_y, window_x))
		frame3 = cv2.resize(thresh1, (window_y, window_x))
		#rows,cols,channels = frame1.shape
		print (frame1.shape)

		#Add the first frame to the big picture
		roi = big_frame[0:cols, 0:rows]
		dst = cv2.add(roi,frame1)
		big_frame[0:cols, 0:rows] = dst

		#Add second frame to the big picture
		roi = big_frame[0:cols, rows:rows*2]
		dst = cv2.add(roi,frame2)
		big_frame[0:cols, rows:rows*2] = dst

		#Add third frame to the big picture
		roi = big_frame[0:cols, rows*2:rows*3]
		dst = cv2.add(roi,frame3)
		big_frame[0:cols, rows*2:rows*3] = dst

		#Add third frame to the big picture
		#roi = big_frame[0:cols, rows*3:rows*4]
		#dst = cv2.add(roi,frame3)
		#big_frame[0:cols, rows*3:rows*4] = dst
            

		cv2.imshow("Big picture", big_frame)'''
                
		print ("Game Score Counter",score)
		k = cv2.waitKey(30) & 0xff
                ##if k == 27:     
                ##break
	cap.release()
	cv2.destroyAllWindows()

