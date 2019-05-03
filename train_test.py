import os
import re
import numpy as np

if __name__ == "__main__":

    this_file = open("./data/labels/list_category_cloth.txt", "r").read()
    this_file = this_file.split('\n')
    this_file = this_file[2:]
    this_file = [this_one.split(' ')[0] for this_one in this_file][:-1]
    assert(len(this_file)==50)

    directories = ["./data/train/" + this_root + "/" for this_root in this_file]
    directories += ["./data/val/" + this_root + "/" for this_root in this_file]

    for this_dir in directories:
        os.system("sudo mkdir " + this_dir)

    root_dir = "./data/images/"

    for this_folder in os.listdir(root_dir):

        if this_folder[0] != '.':

            all_images = np.array(os.listdir(os.path.join(root_dir, this_folder)))
            np.random.shuffle(all_images)

            first = int(len(all_images)*0.85)

            train_dat = all_images[:first]
            val_dat = all_images[first:]

            for this_image in train_dat:
                move_to = "./data/train/"
                os.system("sudo mv " + os.path.join(root_dir, this_folder, this_image) + " " + os.path.join(move_to, this_folder, this_image))


            for this_image in val_dat:
                move_to = "./data/val/"
                os.system("sudo mv " + os.path.join(root_dir, this_folder, this_image) + " " + os.path.join(move_to, this_folder, this_image))
