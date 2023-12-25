import common_utils
import os
from multiprocessing import Process
import cv2
import numpy as np
import time 
import sys


HEIGHT = 128 
IMG = "/home/hbpopos/console_vid_viewer/vid/renai.mp4"

def test_print(continent= "penis"):
    print("the name of the conitnent is : ", continent) 
   

if __name__ == "__main__":
    # names = ['h', 'uhhh', 'goofy ahh', 'ass']
    # procs = []
    # # proc = Process(target=test_print)
    # # procs.append(proc)
    # # proc.start()
    
    # for name in names:
    #     proc = Process(target=test_print, args=(name,))
    #     procs.append(proc)
    #     proc.start()
    
    # for proc in procs:
    #     proc.join()
    # read_img = cv2.resize(cv2.cvtColor(cv2.imread(IMG), cv2.COLOR_BGR2GRAY), (HEIGHT,HEIGHT))
    procs = []
    cap = cv2.VideoCapture(IMG)
    while cap.isOpened():
        ret , read_img = cap.read()       
        scale_factor = common_utils.get_scaling_factor(read_img)
        read_img = cv2.resize(cv2.cvtColor(read_img, cv2.COLOR_BGR2GRAY), (int(HEIGHT * scale_factor), HEIGHT))
        ar1 = read_img[0:int(HEIGHT/2)]
        ar2 = read_img[int(HEIGHT/2):HEIGHT]  
        yea = [ar1, ar2]
        for fuck in yea:
            proc = Process(target=common_utils.process_img, args=(fuck,HEIGHT)) 
            procs.append(proc)
            proc.start()
            for proc in procs:
                    proc.join()
                    # os.system("clear")
                    # sys.stdout.flush()
                    time.sleep(0.0005)