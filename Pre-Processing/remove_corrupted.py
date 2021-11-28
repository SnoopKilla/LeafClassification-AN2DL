import os
import cv2
import numpy as np

path = "./GitHub/LeafClassification-AN2DL/Data/dataset_no_corrupted"
training = path + "/training"

# First we look for images with an anomalous number of black pixels and manually inspect them to identify the corrupted ones
for label in os.listdir(training):
    for i, datum in enumerate(os.listdir(training + "/" + label)):
        img = cv2.imread(training + "/" + label + "/" + datum)
        if np.sum(img==0) >= 0.8*256*256*3:
            print(training + "/" + label + "/" + datum)
            cv2.imshow('image', img)
            cv2.waitKey()

# We now delete the corrupted images
to_delete = ["28213.jpg","28435.jpg","11220.jpg","11284.jpg","31401.jpg","11488.jpg",
"11601.jpg","11897.jpg","14170.jpg","14219.jpg","14371.jpg","18905.jpg","37919.jpg",
"40004.jpg","40112.jpg","40691.jpg","41394.jpg","42067.jpg","42249.jpg","42717.jpg",
"43292.jpg"]
for label in os.listdir(training):
    for i, datum in enumerate(os.listdir(training + "/" + label)):
        if datum in to_delete:
            os.remove(training + "/" + label + "/" + datum)
