import os
import glob
import time

def create_dir(dirName, subdirName, source_path):

    if subdirName == None:
        new_path_dir = os.path.join(source_path,dirName)
        if os.path.isdir(new_path_dir):
            print(f"{new_path_dir} already exists")
        else:
            os.makedirs(new_path_dir)

    else:
        new_path_subdir = os.path.join(source_path,dirName,subdirName)

        if os.path.isdir(new_path_subdir):
            print(f"{new_path_subdir} already exists")
        else:
            os.makedirs(new_path_subdir)

def locateLastFile():
    list_of_files = glob.glob('C:/Users/seifa/Downloads/*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file.replace("\\","/")

def moveFile(dirName, subdirName, file, source_path):
    file_name = file.split("/")[-1]
    todest = os.path.join(source_path,dirName,subdirName, file_name)
    if os.path.isfile(todest):
        print(f"{file_name} is already in your folders" )
    else:

        os.replace(file, todest)
       





def setup(courses, source_path):
    for course in courses:
        create_dir(course, None, source_path)
        for sub in courses[course]:
            create_dir(course, sub,source_path)

sp = "C:/Users/seifa/Documents/KrayaTest"




