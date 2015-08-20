"""
Rudra Poudel

Convert vtk to nrrd file format.
"""
import os, subprocess, glob

def getFilelist(dataset_path):
    files = []
    for filename in glob.iglob(dataset_path):
        files.append(filename)
        # print filename
    return files

def getLines(filename):
    files = []
    f = open(filename, "r")
    for afile in f:
        files.append(afile.strip('\n'))
    f.close()
    return files

def run(dirlist):
    dirs = []
    if os.path.isfile(dirlist):
        dirs = getLines(dirlist)
    elif os.path.exists(dirlist):
        dirs.append(dirlist)
    else:
        raise Exception('INVALID argument- accepts either dirs list or dir')

    for adir in dirs:
        filelist = getFilelist(os.path.join(adir, '*.vtk'))
        for afile in filelist:
            (root, ext) = os.path.splitext(afile)
            new_filename = root + '.nrrd'
            print('*************')
            print(afile)
            print(new_filename)
            
            cvt_command = '/home/rp14/libraries/teem-build/bin/unu save -f nrrd -e gzip -i ' + afile + ' -o ' + new_filename
            return_code = subprocess.call(cvt_command, shell=True)

if __name__ == '__main__':
    run('/montana-storage/shared/data/cardiac/segmentation/LV_Pablos/dirlist.txt')
    # run('/montana-storage/shared/data/cardiac/segmentation/LV_Pablos/EVS001')

