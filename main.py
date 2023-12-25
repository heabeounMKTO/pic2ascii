import cv2
import os
import numpy as np
import common_utils
import argparse


def main():
    HEIGHT = int(arg.height)
    IMGFOLDER = str(arg.source)
    BW = arg.binary_color
    if os.path.isdir(arg.source):
        """
        if a directory is given
        """
        all_img = []
        for file in os.listdir(IMGFOLDER):
            if file.endswith((".jpeg", ".jpg", ".png")):
                all_img.append(file)
        for img in all_img:
            img = os.path.join(IMGFOLDER, img)
            scale_factor = common_utils.get_scaling_factor(cv2.imread(img))
            read_img = cv2.cvtColor(
                cv2.resize(cv2.imread(img), (int(HEIGHT * scale_factor), HEIGHT)),
                cv2.COLOR_BGR2GRAY,
            )
            common_utils.process_img(read_img, HEIGHT, binary=BW)
    if os.path.isfile(arg.source):
        """
        if a file is given
        """
        if arg.source.endswith((".jpeg", ".png", ".jpg")):
            """
            if image
            """
            img = IMGFOLDER
            scale_factor = common_utils.get_scaling_factor(cv2.imread(img))
            read_img = cv2.cvtColor(
                cv2.resize(cv2.imread(img), (int(HEIGHT * scale_factor), HEIGHT)),
                cv2.COLOR_BGR2GRAY,
            )
            common_utils.process_img(read_img, HEIGHT, binary=BW)
        if arg.source.endswith(".mp4"):
            """
            if video
            """
            vid = IMGFOLDER
            cap = cv2.VideoCapture(vid)
            while cap.isOpened():
                ret, frame = cap.read()
                scale_factor = common_utils.get_scaling_factor(frame)
                if ret == True:
                    frame = cv2.resize(
                        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),
                        (int(HEIGHT * scale_factor), HEIGHT),
                    )
                    common_utils.process_img(frame, HEIGHT, binary=BW)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source", type=str, help="source , can be a jpeg , mp4 or folder"
    )
    parser.add_argument(
        "--height", type=int, default=32, help="console rendering HEIGHT"
    )
    parser.add_argument(
        "--binary_color" , action="store_true", help="renders in binary color b/w"
    )
    arg = parser.parse_args()
    print(arg)
    main()
