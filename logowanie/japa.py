'''
Wczytywanie z kamery
'''
import cv2

cap = cv2.VideoCapture(0)
#cap.set(3, 1200)
cap.set(3, 1024)
cap.set(cv2.CAP_PROP_BRIGHTNESS, 1)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    cv2.imshow("Live Maliniarz ReactionP", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
