#onemotion.com
import cv2
import numpy as np
import imutils
from playsound import playsound

def play(key):
	if key == 'SNAP':
		playsound('./sounds/Snap-1.wav')
	elif key == 'CLAP':
		playsound('./sounds/Clap.wav')
	elif key == 'CHANT':
		playsound('./sounds/Chant.wav')
	elif key == 'CRASH':
		playsound('./sounds/Crash.wav')
	elif key == 'SNARE':
		playsound('./sounds/Snare.wav')
	elif key == 'BASS':
		playsound('./sounds/BASS.wav')
	elif key == 'HIT HAT':
		playsound('./sounds/Hit-Hat.wav')
	elif key == 'HIT HAT OPEN':
		playsound('./sounds/Hit-Hat-Open.wav')
	elif key == 'KICK-2':
		playsound('./sounds/Kick-2.wav')
	elif key == 'KICK-1':
		playsound('./sounds/Kick-1.wav')
	elif key == 'TOM HI':
		playsound('./sounds/Tom-hi.wav')
	elif key == 'TOM LOW':
		playsound('./sounds/Tom-low.wav')

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)
    frame = imutils.resize(frame,height=700, width=900)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowred = np.array([131,90,106])
    highred = np.array([255,255,255])

    lowblue = np.array([40,150,116])
    highblue = np.array([255,255,255])

    red_mask = cv2.inRange(hsv, lowred, highred)
    blue_mask = cv2.inRange(hsv, lowblue, highblue)

    # image/frame, start_point, end_point, color, thickness
    cv2.rectangle(frame, (0,0), (200,150), (255,0,0),1)
    cv2.putText(frame,'SNAP',(70,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
    cv2.rectangle(frame, (210,0), (430,150), (0,0,255),1)
    cv2.putText(frame,'CLAP',(245,80),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv2.LINE_AA)
    cv2.rectangle(frame, (440,0), (650,150), (255,0,0),1)
    cv2.putText(frame,'CHANT',(445,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
    cv2.rectangle(frame, (660,0), (900,150), (0,0,255),1)
    cv2.putText(frame,'CRASH',(730,80),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv2.LINE_AA)

    cv2.rectangle(frame, (0,160), (50,370), (255,0,0),1)
    cv2.putText(frame,'SNARE',(10,290),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
    cv2.rectangle(frame, (0,380), (50,570), (0,0,255),1)
    cv2.putText(frame,'BASS',(10,500),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv2.LINE_AA)
    cv2.rectangle(frame, (850,160), (900,370), (255,0,0),1)
    cv2.putText(frame,'HIT HAT',(770,290),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
    cv2.rectangle(frame, (850,380), (900,570), (0,0,255),1)
    cv2.putText(frame,'HIT HAT OPEN',(670,500),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv2.LINE_AA)

    cv2.rectangle(frame, (440,580), (650,700), (255,0,0),1)
    cv2.putText(frame,'KICK-2',(480,640),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
    cv2.rectangle(frame, (660,580), (900,700), (0,0,255),1)
    cv2.putText(frame,'KICK-1',(740,640),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv2.LINE_AA)
    cv2.rectangle(frame, (0,580), (200,700), (255,0,0),1)
    cv2.putText(frame,'TOM HI',(50,640),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
    cv2.rectangle(frame, (210,580), (430,700), (0,0,255),1)
    cv2.putText(frame,'TOM LOW',(250,640),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3,cv2.LINE_AA)

    #for the red Object
    contours,hierachy=cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    for cnt in contours:
	    #startpoint, endpoint, color, thickness
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),2)
        print((x,y))   
        if x > 0 and y > 0 and x < 200 and y < 150:
            play('SNAP')      
        elif x > 210 and y > 0  and x < 430 and y < 150:
            play('CLAP')      
        elif x > 440 and y > 0 and x < 650 and y < 150:
            play('CHANT')      
        elif x > 660 and y > 0 and x < 900 and y < 150:
            play('CRASH')      
        
        elif x > 0 and y > 160 and x < 50 and y < 370:
            play('SNARE')      
        elif x > 0 and y > 380 and x < 50 and y < 570:
            play('BASS')      
        elif x > 850 and y > 160 and x < 900 and y < 370:
            play('HIT HAT')      
        elif x > 850 and y > 380 and x < 900 and y < 570:
            play('HIT HAT OPEN')      
        
        elif x > 440 and y > 580 and x < 650 and x < 700:
            play('KICK-2')      
        elif x > 660 and y > 580 and x < 900 and y < 700:
            play('KICK-1')      
        elif x > 0 and y > 580 and x < 200 and y < 700:
            play('TOM HI')      
        elif x > 210 and y > 580 and x < 430 and y < 700:
            play('TOM LOW')      
        break
    
    #for the blue Object
    contours,hierachy=cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    #startpoint, endpoint, color, thickness
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),2)
        print((x,y))
        if x > 0 and y > 0 and x < 200 and y < 150:
            play('SNAP')      
        elif x > 210 and y > 0  and x < 430 and y < 150:
            play('CLAP')      
        elif x > 440 and y > 0 and x < 650 and y < 150:
            play('CHANT')      
        elif x > 660 and y > 0 and x < 900 and y < 150:
            play('CRASH')      
        
        elif x > 0 and y > 160 and x < 50 and y < 370:
            play('SNARE')      
        elif x > 0 and y > 380 and x < 50 and y < 570:
            play('BASS')      
        elif x > 850 and y > 160 and x < 900 and y < 370:
            play('HIT HAT')      
        elif x > 850 and y > 380 and x < 900 and y < 570:
            play('HIT HAT OPEN')      
        
        elif x > 440 and y > 580 and x < 650 and x < 700:
            play('KICK-2')      
        elif x > 660 and y > 580 and x < 900 and y < 700:
            play('KICK-1')      
        elif x > 0 and y > 580 and x < 200 and y < 700:
            play('TOM HI')      
        elif x > 210 and y > 580 and x < 430 and y < 700:
            play('TOM LOW')      
        break
    
    
    cv2.imshow("frame", frame)
 
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()