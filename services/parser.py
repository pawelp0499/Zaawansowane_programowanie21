from detectors.file_path import *
import argparse


def selector():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-i", "--image", type=str,
                           help="full path to Image File")
    arg_parse.add_argument("-v", "--video", type=str,
                           help="full path to Video File")

    args = vars(arg_parse.parse_args())
    return args


def assigner(args):
    image_path = args["image"]
    video_path = args['video']

    if image_path is not None:
        image_detector(image_path)
    elif video_path is not None:
        video_detector(video_path)
