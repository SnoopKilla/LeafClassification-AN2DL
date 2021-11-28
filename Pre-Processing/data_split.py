import os
import random

path = "./GitHub/LeafClassification-AN2DL/Data/dataset_no_corrupted"
training = path + "/training"
validation = path + "/validation"
seed = 69
random.seed(seed)

if not os.path.exists(validation):
    os.mkdir(validation)

# For each folder (Apple, Blueberry, ...) we sample 110 images to move in the validation directory and then move them
for label in os.listdir(training):
    total_images = len(os.listdir(training + "/" + label))
    to_move = random.sample(range(0, total_images-1), 110)
    if not os.path.exists(validation + "/" + label):
        os.mkdir(validation + "/" + label)
    for i, datum in enumerate(os.listdir(training + "/" + label)):
        if i in to_move:
            os.rename(training + "/" + label + "/" + datum, validation + "/" + label + "/" + datum)
