

import numpy as np
import face_recognition
import cv2
import time

cap= cv2.VideoCapture(0)
start_frame_number = 120
cap. set(cv2. CAP_PROP_POS_FRAMES, start_frame_number)
img=fr.load_image_file("Parsh.jpg")
img_encoding=fr.face_encodings(img)[0]

known_img_encoding=[img_encoding]
known_face_names = ["Parsh"]

while True:

    rval, frame = cap.read()



    rgb_frame= frame[:, :, ::-1]

    face_locations = fr.face_locations(rgb_frame)
    img_encoding= fr.face_encodings(rgb_frame,face_locations)

    for (top, right,bottom,left), img_encoding in zip(face_locations,img_encoding):

        matches = fr.compare_faces(known_img_encoding,img_encoding)

        name= "UNknown"

        face_distances = fr.face_distance(known_img_encoding,img_encoding)

        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name=known_face_names[best_match_index]

        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)

        cv2.rectangle(frame,(left,bottom-35),(right,bottom),(0,0,255),cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,name,(left+6,bottom-6),font,1.0,(255,255,255),1)

        cv2.imshow('TeamServerMonks', frame)
        if cv2.waitKey(1) & 0xFF == ord ('q'):
           break
cap.release()
cv2.destroyAllWindows()







