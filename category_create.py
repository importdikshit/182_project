import os

if __name__ == "__main__":

    this_file = open("./data/labels/list_category_cloth.txt", "r").read()
    this_file = this_file.split('\n')
    this_file = this_file[2:]
    this_file = [this_one.split(' ')[0] for this_one in this_file][:-1]
    assert(len(this_file)==50)

    directories = ["./data/images/" + this_root + "/" for this_root in this_file]
    os.system("sudo mkdir ./data/images/")


    # Create all the subdirectories
    for this_dir in directories:
        os.system("sudo mkdir " + this_dir)

    type_counts = {}


    for this_dir in os.listdir("./data/img/"):

        if this_dir[0] != ".":

            type_article = this_dir.split("_")[-1]

    #         if "&" in this_dir:
    #             this_dir = this_dir.replace("&", "\&")
    #             this_dir = this_dir.replace(";", "\;")
    # #             this_dir = this_dir.replace("'", "\\'")

            if type_article in type_counts:
                type_counts[type_article] += 1
            else:
                type_counts[type_article] = 0


            tack_on = type_article + str(type_counts[type_article])

            path = "./data/img/" + this_dir + "/"

            for this_file in os.listdir(path):
                 os.rename(os.path.join(path,this_file), os.path.join(path, tack_on + this_file))
    #             print(os.path.join(path, tack_on + this_file))
    #         print(tack_on)


    # Move all the files by category
    for this_dir in os.listdir("./data/img/"):

        if this_dir[0] != ".":

            type_article = this_dir.split("_")[-1]

            if "&" in this_dir:
                this_dir = this_dir.replace("&", "\&")
                this_dir = this_dir.replace(";", "\;")
    #             this_dir = this_dir.replace("'", "\\'")

            os.system("sudo mv ./data/img/" + this_dir + "/* ./data/images/" + type_article + "/")


    for this_dir in os.listdir("./data/images/"):

        # Print the number of files in each directory
        print(this_dir, len(os.listdir("./data/images/" + this_dir + "/")))
