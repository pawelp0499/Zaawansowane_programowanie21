import cv2
import sys

cascPath = sys.argv[0]
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                    'haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    person = 1
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 255), 1)
        person += 1

        cv2.putText(frame, 'Status: Detecting ', (40, 40),
                    cv2.FONT_HERSHEY_COMPLEX, 0.8,
                    (0, 255, 0), 2)
        cv2.putText(frame, f'Number of person: {person - 1}', (40, 70),
                    cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 0), 1)
    cv2.imshow('Output', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    count = 0

#cv2.waitKey(0)
video_capture.release()
cv2.destroyAllWindows()
