import cv2
import numpy as np
import os
import math


#ISTRING = "▓oahkbdpqwmZO0QLCJUYXf-_/\|()[]?░"
BINSTRING = "▓░"
ISTRING = "█@#W$9876543210?!abc;:+=-,._.:░▓"
def print_npyrow(row: any, spacing: any):
    print(f"{spacing}".join(map(str, row)))

def get_scaling_factor(img_arr: np.ndarray):
    return (img_arr.shape[1] / img_arr.shape[0] * 2)

def set_char(x: any, binary: bool=False):
    x /= 8
    x = int(math.ceil(x))
    if binary == False:
        if x <= len(ISTRING):
            try:
                return str(ISTRING[x]).upper()
            except IndexError:
                return "░"
        else:
            return "▓"
    if binary==True:
        if x > 0:
            return BINSTRING[0]
        if x == 0:
            return BINSTRING[1]

def process_img(img_arr: np.ndarray, height: int, binary: bool=False):
    vfunc = np.vectorize(set_char)
    print('''


    ''')
    for row in img_arr[:height]:
        row = vfunc(row, binary=binary)
        print_npyrow(row=row, spacing="")
    print('''


    ''')
