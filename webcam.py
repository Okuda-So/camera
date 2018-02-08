import cv2
import time

cap = cv2.VideoCapture(0)
print('Camera Opened: ' + str(cap.isOpened()))

for i in range(5):
    ret, frame = cap.read()

try:
    while True:
        ret, frame = cap.read()
        print(ret)

        cv2.imshow('WebCam_0', frame)
        key = cv2.waitKey(499) & 0xFF
        if key ==ord('s'):
                filename = 'cap_' + time.strftime('%y%m%d%H%M%S') + '.jpg'
                    cv2.imwrite(filename, frame)
                        print('Saved '+ filename)
        if key ==ord('q'):
                break

        # time.sleep(0.49)
        
except KeyboardInterrupt:
    filename = 'cap_' + time.strftime('%y%m%d%H%M%S') + '.jpg'
    cv2.imwrite(filename, frame)
    print('KeyboardInterrupt!')
    print('Saved ' + filename)
