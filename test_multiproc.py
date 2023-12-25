import common_utils
import os
from multiprocessing import Process
import cv2
import numpy as np
import time 
import sys


HEIGHT = 64 
IMG = "/home/hb/Videos/renai.mp4"

def test_print(continent= "penis"):
    print("the name of the conitnent is : ", continent) 


def split_img(input_img: np.ndarray,split: int):
    index = 0
    split_array = []
    for idx ,x  in enumerate(range(split)):
        _yea = input_img[int((HEIGHT/split) * (idx)):int((HEIGHT/split) * (idx+1))]
        split_array.append(_yea)
    return split_array
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
        # seg = 10 
        # ar1 = read_img[0:int(HEIGHT/seg)]
        # ar2 = read_img[int(HEIGHT/seg):(int(HEIGHT/seg)*2)]  
        # ar3 = read_img[(int(HEIGHT/seg)*2):(int(HEIGHT/seg)*3)]  
        # ar4 = read_img[(int(HEIGHT/seg)*3):(int(HEIGHT/seg)*4)]  
        # ar5 = read_img[(int(HEIGHT/seg)*4):(int(HEIGHT/seg)*5)]  
        # ar6 = read_img[(int(HEIGHT/seg)*5):(int(HEIGHT/seg)*6)]  
        # ar7 = read_img[(int(HEIGHT/seg)*7):(int(HEIGHT/seg)*8)]  
        # ar8 = read_img[(int(HEIGHT/seg)*8):(int(HEIGHT/seg)*9)]  
        # ar9 = read_img[(int(HEIGHT/seg)*9):(int(HEIGHT/seg)*10)]  
        # yea = [ar1, ar2,ar3,ar4,ar5,ar6,ar7,ar8,ar9]
        yea = split_img(read_img, 4)        
        for fuck in yea:
            proc = Process(target=common_utils.process_img, args=(fuck,HEIGHT)) 
            procs.append(proc)
            proc.start()
    for proc in procs:
            proc.join()
                    # os.system("clear")
                    # sys.stdout.flush()
