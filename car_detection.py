import cv2

cap = cv2.VideoCapture('traffic.mp4')
cc = cv2.CascadeClassifier('cars.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if len(cc.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 1.1, 9)) > 0:
        print("Vehicle detected at: " + str(cap.get(cv2.CAP_PROP_POS_MSEC)) + " ms")
