import cv2
import mediapipe as mp
import serial
import time

# Arduino / ESP COM port
ser = serial.Serial('COM15', 9600, timeout=1)
time.sleep(2)

# Mediapipe Hands
mp_hands = mp.solutions.hands
hands_detector = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

tipIds = [4, 8, 12, 16, 20]
prev_fingers = -1  # previous gesture

while True:
    success, img = cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands_detector.process(imgRGB)

    lmList = []

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append((cx, cy))
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    fingers = []
    if len(lmList) != 0:
        # Thumb
        if lmList[tipIds[0]][0] > lmList[tipIds[0]-1][0]:
            fingers.append(1)
        else:
            fingers.append(0)

        # Other fingers
        for id in range(1,5):
            if lmList[tipIds[id]][1] < lmList[tipIds[id]-2][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        totalFingers = fingers.count(1)

        # send only if gesture changed
        if totalFingers != prev_fingers:
            ser.write(str(totalFingers).encode())
            prev_fingers = totalFingers
            print("Sent:", totalFingers)

        cv2.putText(img, str(totalFingers), (50,100),
                    cv2.FONT_HERSHEY_SIMPLEX, 3, (0,255,0), 3)

    cv2.imshow("Gesture Control", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
ser.close()