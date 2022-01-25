import cv2
import sys

"""Classifier to detection process"""
cascPath = sys.argv[0]
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                    'haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

"""Main function to detect and count person on camera image"""


def camera_detector(name: str):
    while True:
        ret, vision = video_capture.read()

        gray = cv2.cvtColor(vision, cv2.COLOR_BGR2GRAY)

        human = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        person = 1
        cv2.putText(vision, f'Number of person: ', (40, 70),
                    cv2.cv2.FONT_HERSHEY_TRIPLEX, 0.8, (0, 0, 0), 1)

        for (x, y, w, h) in human:

            cv2.rectangle(vision, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(vision, f'person {person}', (x, y),
                        cv2.cv2.FONT_HERSHEY_TRIPLEX,
                        0.63, (0, 0, 255), 1)
            person += 1

            cv2.putText(vision, f'{person - 1}', (305, 70),
                        cv2.cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0), 2)
        cv2.imshow(f'{name}', vision)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
