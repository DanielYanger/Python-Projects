import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
    # pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
    # pts = pts.reshape((-1,1,2))
    # img = cv2.polylines(img,[pts],True,(0,255,255))
    # rows,cols,something = img.shape

    # M = cv2.getRotationMatrix2D((cols/2,rows/2),-90,1)
    # dst = cv2.warpAffine(img,M,(cols,rows))

    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    #eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    ret,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, 1.1, 4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        # roi_gray = gray[y:y+h, x:x+w]
        # roi_color = img[y:y+h, x:x+w]
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex,ey,ew,eh) in eyes:
         #   cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    # Display the resulting frame
    cv2.imshow('frame',img)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()