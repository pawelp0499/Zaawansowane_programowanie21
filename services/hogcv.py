import cv2


hogcv = cv2.HOGDescriptor()
hogcv.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
