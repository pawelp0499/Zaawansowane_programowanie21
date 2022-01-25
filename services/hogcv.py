import cv2

"""Import of HOG descriptor"""
hogcv = cv2.HOGDescriptor()
hogcv.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
