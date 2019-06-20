import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt

options = {
    "model": "/home/pyrop/Documents/YOLO/cfg/yolo.cfg",
    "load": "/home/pyrop/Documents/YOLO/bin/yolov2.weights",
    "threshold": 0.3,
    "gpu": 1.0,
}

tfnet = TFNet(options)
img = cv2.imread("index.jpeg", cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
result = tfnet.return_predict(img)
tl = result[0]["topleft"]["x"], result[0]["topleft"]["y"]
br = result[0]["bottomright"]["x"], result[0]["bottomright"]["y"]
label = result[0]["label"]

img = cv2.rectangle(img, tl, br, (0, 255, 0), 5)
img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 0), 1)
plt.imshow(img)
plt.show()
