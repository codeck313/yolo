import cv2
from darkflow.net.build import TFNet
import numpy as np
import time

option = {
    "model": "/home/pyrop/Documents/YOLO/cfg/yolov2-tiny-voc-1c.cfg",
    "load": 1000,
    "threshold": 0.1,
    "gpu": 1.0,
}

tfnet = TFNet(option)

colors = [tuple(255*np.random.rand(3)) for i in range(10)]

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
frameRateNeeded = 60
prev = 0

while True:
    time_elapsed = time.time()-prev
    ret, frame = capture.read()
    if time_elapsed > (1/frameRateNeeded):
        results = tfnet.return_predict(frame)
        prev = time.time()
        fps = 1/time_elapsed

    if ret:
        for color, result in zip(colors, results):
            tl = result["topleft"]["x"], result["topleft"]["y"]
            br = result["bottomright"]["x"], result["bottomright"]["y"]
            label = result["label"]
            confidence = result["confidence"]
            fps_string = str(round(fps))+" FPS_YOLO"
            text = '{}: {:.0f}%'.format(label, (confidence*100))
            frame = cv2.rectangle(frame, tl, br, color, 5)
            frame = cv2.putText(
                frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2
            )
            frame = cv2.putText(
                frame, fps_string, (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2)
        cv2.imshow('Webcam-Procesing', frame)
        print('FPS {:.1f}'.format(fps))
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        capture.release()
        cv2.destroyAllWindows()
        break
