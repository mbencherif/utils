
import os, glob, dicom, scipy, pylab, h5py
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from scipy import ndimage


def validateDICOMRead(filename, saveto):
    dcm = dicom.read_file(filename)
    img = dcm.pixel_array #int16
    img = img.astype('float32')
    img = np.divide(img, img.max())
    
    print(img.dtype)
    print(img.shape) 
    print(img.min())
    print(img.max())

    #scipy.misc.toimage(img).save(saveto, mode='P', channel_axis=0)
    X = np.zeros((1, 1, 256, 256), dtype=np.float32)
    X[0,0,:,:] = img
    f = h5py.File('/home/rp14/log/img.h5', 'w')
    dset = f.create_dataset('data', shape=X.shape, dtype=X.dtype, data=X)
    f.close()

    # img = scipy.misc.toimage(ndarray, cmin = min_color_vlaue, cmax = max_color_value)
    scipy.misc.toimage(img).save(saveto)
    # View image
    pylab.imshow(dcm.pixel_array)
    pylab.show()

def saveDICOMImage(filename, saveto):
    dcm = dicom.read_file(filename)
    img = dcm.pixel_array #int16
    #img = img.astype('float32')
    
    print(img.dtype)
    print(img.shape) 
    print(img.min())
    print(img.max())

    #scipy.misc.toimage(img).save(saveto, mode='P', channel_axis=0)
    if len(img.shape)==3:
        print('Changing shape from CHW to HWC')
        img_new = np.zeros( (img.shape[1],img.shape[2],3), dtype=img.dtype)
        print(img_new.shape)
        img_new[:,:,0] = img[0,:,:]
        img_new[:,:,1] = img[1,:,:]
        img_new[:,:,2] = img[2,:,:]
        scipy.misc.toimage(img_new).save(saveto)
        
        # View image
        pylab.imshow(img_new)
        pylab.show()
    else:
        scipy.misc.toimage(img).save(saveto)
        # View image
        pylab.imshow(dcm.pixel_array)
        pylab.show()

def getFilelist(dataset_path):
    files = []
    for filename in glob.iglob(dataset_path):
        files.append(filename)
        # print filename
    return files

def readDICOMProperties(volume_name):
    files = getFilelist(os.path.join(volume_name, '*.dcm'))
    print('Num files: ' + str(len(files)))

    # for file_index in xrange(len(files)):
    for file_index in xrange(1):
        filename = files[file_index]
        
        dcm = dicom.read_file(filename)
        # print(dcm)
        
        if 'PixelData' in dcm:
            img = dcm.pixel_array #int16
            #img = img.astype('float32')
        else:
            print('PixelData: False')

        if 'SOPClassUID' in dcm:
            print(dcm.SOPClassUID)
        else:
            print('SOPClassUID: False')
        

        # # Read/display DCM properties
        # if True:
        #     print(dcm.SOPClassUID)
        #     print('--------------------')
        # else:
        #     if dcm.SOPClassUID != 'MR Image Storage':
        #         print(str(file_index) + ': ' + dcm.SOPClassUID)
        #     print('--------------------')
        
        # print(img.dtype)
        # print(img.shape) 
        # print(img.min())
        # print(img.max())

        # #scipy.misc.toimage(img).save(saveto, mode='P', channel_axis=0)
        # if len(img.shape)==3:
        #     print('Changing shape from CHW to HWC')
        #     img_new = np.zeros( (img.shape[1],img.shape[2],3), dtype=img.dtype)
        #     print(img_new.shape)
        #     img_new[:,:,0] = img[0,:,:]
        #     img_new[:,:,1] = img[1,:,:]
        #     img_new[:,:,2] = img[2,:,:]
        #     scipy.misc.toimage(img_new).save(saveto)
            
        #     # View image
        #     pylab.imshow(img_new)
        #     pylab.show()
        # else:
        #     scipy.misc.toimage(img).save(saveto)
        #     # View image
        #     pylab.imshow(dcm.pixel_array)
        #     pylab.show()
   
if __name__ == '__main__':
    # Test
    # saveDICOMImage('/montana-storage/shared/data/cardiac/segmentation/LV_MICCAI/challenge_training/SC-HF-I-40/IM-0132-0001.dcm',
    #                 '/home/rp14/log/img.jpg')

    # validateDICOMRead('/montana-storage/shared/data/cardiac/segmentation/LV_MICCAI/challenge_training/SC-HF-I-40/IM-0132-0001.dcm',
    #                 '/home/rp14/log/img.jpg')

    # readDICOMProperties('/home/rp14/projects/data/LV/Boxall_Wayne_19650116_RJ109960767')
    readDICOMProperties('/home/rp14/projects/data/LV/Boxall_Wayne_19650116_RJ109960767_storage')
    