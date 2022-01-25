import imutils
from services.hogcv import *


"""Main detection function"""


def person_detector(source):

    scrap, weights = hogcv.detectMultiScale(source,
                                            winStride=(4, 4),
                                            padding=(16, 16),
                                            scale=1.07
                                            )

    person = 1
    for x, y, w, h in scrap:
        cv2.rectangle(source, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(source, f'person {person}', (x, y),
                    cv2.FONT_HERSHEY_TRIPLEX, 0.62, (0, 0, 255), 1)
        person += 1
    cv2.putText(source, f'Number of person: ', (40, 70),
                cv2.FONT_HERSHEY_TRIPLEX, 0.8, (0, 0, 0), 1)
    cv2.putText(source, f'{person - 1}', (305, 70),
                cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('result', source)
    return source


"""Function reads image from path and resizes before detecting process"""


def image_detector(path: str):
    image = cv2.imread(path)
    image = imutils.resize(image, width=min(700, image.shape[1]),
                           height=min(525, image.shape[1]))
    person_detector(image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


"""Function reads video from path and resizes before detecting process"""


def video_detector(path: str):
    video = cv2.VideoCapture(path)
    while video.isOpened():
        check, frame = video.read()
        if check:
            frame = imutils.resize(frame, width=min(800, frame.shape[1]),
                                   height=min(600, frame.shape[1]))
            person_detector(frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break
    video.release()
    cv2.destroyAllWindows()
