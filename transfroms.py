import torch
import numpy as np
import PIL
import cv2
import random

# TODO: implementation transformations for task3;
# You cannot directly use them from pytorch, but you are free to use functions from cv2 and PIL
class Padding(object):
    def __init__(self, padding):
        self.padding = padding

    def __call__(self, img, **kwargs):
        pass
        
        return img


class RandomCrop(object):
    def __init__(self, size):
        self.size = size

    def __call__(self, img, **kwargs):
        pass

        return img


class RandomFlip(object):
    def __init__(self,):
        pass
    def __call__(self, img, **kwargs):
        
        pass
        return img
