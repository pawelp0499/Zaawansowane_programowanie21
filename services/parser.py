import argparse
from detectors.file_path import *
from detectors.video_capture import *


def selector():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-i", "--image", type=str,
                           help="full path to Image File")
    arg_parse.add_argument("-v", "--video", type=str,
                           help="full path to Video File")
    arg_parse.add_argument("-c", "--camera", type=str,
                           help="any name of camera window")

    args = vars(arg_parse.parse_args())
    return args


def assigner(args):
    image_path = args["image"]
    video_path = args['video']
    name = args['camera']

    if image_path is not None:
        image_detector(image_path)

    elif video_path is not None:
        video_detector(video_path)

    elif name is not None:
        camera_detector(name)
