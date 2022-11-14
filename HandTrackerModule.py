import cv2
import mediapipe as mp
import time


class HandDetector():
    def __init__(self, mode = False, maxHands = 2, detectConfidence = 0.5, trackConfidence = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectConfidence = detectConfidence
        self.trackConfidence = trackConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectConfidence, self.trackConfidence)
        self.mpDraw = mp.solutions.drawing_utils


    def findHands(self, img, draw = True):

            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = self.hands.process(imgRGB)
            # print(results.multi_hand_landmarks)

            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    if draw:
                        self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)



                    # for id, lm in enumerate(handLms.landmark):
                    #     # print(id, lm)
                    #     h, w, c = img.shape
                    #     cx = int(lm.x*w)
                    #     cy = int(lm.y*h)
                    #     print(id, cx, cy)
                    #     if id == 4:
                    #     cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)



def main():
    pTime = 0
    cTime = 0

    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(f'FPS:{int(fps)}'), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)

        cv2.imshow("Aashish's Hand Tracker", img)
        key = cv2.waitKey(1)

        if key == 81 or key == 113:
            break


if __name__ == "__main__":
    main()