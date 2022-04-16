
import cv2
from gaze_tracking import GazeTracking
from gaze_tracking.eye import Eye
import numpy as np

import os

gaze = GazeTracking()
# webcam = cv2.VideoCapture(0)

for i in range(380, 759, 1):  #tên tấm hình muốn lấy
    link =  "E:\BIO-ID Dataset\BioID_0760.jpg";
    file_name = "BioID_0";
    link = link[0:18]
    name = file_name + str(i)
    link = link+name+".jpg"
    print(name)
    webcam = cv2.imread(link) 
    gaze.refresh(webcam)

    frame = gaze.annotated_frame() #Vẽ dấu cộng tâm mắt
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(frame, text, (30, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (40, 90), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (40, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
   

    trai = str(left_pupil)
    phai = str(right_pupil)
    trai = trai[1:-1]
    phai = phai[1:-1]
    title = str(trai.replace(",", "    ")+"   "+phai.replace(",", "    "))
    print(title)

    tentxt = 'F:\hihi\BioID_0385.txt' # sau khi chạy cái tạo file thì mọi người đưa 1 file bất kì vào đây
    tentxt = tentxt[0:8] # chỗ này tui tách ra chỉ còn => "F:\hihi\" nên có gì mng xem lại chỗ này
    tentxt = tentxt+name+".txt" # này cộng thêm đuôi txt để có gì mở tệp hoy nhe

    f = open(tentxt,"w")

    with open(tentxt,"a") as f:
        print(type(f))

    f = open(tentxt, 'r+', encoding='UTF-8')   
 

    path_w = tentxt
    
    title2 = "#LX	LY	RX	RY\n"

    with open(path_w, mode='w') as f:
        f.write(title2)
        f.write(title)
    with open(path_w) as f:
        print(f.read())


    cv2.imshow("Demo", frame)
   
    if cv2.waitKey(1) == 27:
        break

# webcam.release()
cv2.destroyAllWindows()
# webcam = cv2.imread(link)

# link = "E:\Thi\ResFres\BIO-ID Dataset\BioID_0000.jpg";

