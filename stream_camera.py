"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
from gaze_tracking.eye import Eye


gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)
    # gaze.refresh(webcam)

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

    print(str(text))

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break

    
webcam.release()
cv2.destroyAllWindows()
