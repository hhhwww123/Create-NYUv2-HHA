import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import h5py
import os
from PIL import Image

PATH = ['./nyu_image', './nyu_depths_16','./nyu_rawdepth_16','./label']

f=h5py.File("nyu_depth_v2_labeled.mat")
depths=f["depths"]
rawdepth=f["rawDepths"]

depths=np.array(depths)
rawdepth=np.array(rawdepth)

for path in PATH:
    if not os.path.isdir(path):
        os.makedirs(path)
'''
max=depths.max()
print (depths.shape)
print (depths.max())
print (depths.min())

depths=depths/max*255
'''
depths=depths.transpose((0,2,1))
rawdepth=rawdepth.transpose((0,2,1))
#print (depths.max())
#print (depths.min())

for i in range(len(depths)):
    #print (str(i)+'.png')
    depths_img=Image.fromarray(np.uint32(depths[i]*10000))
    rawdepth_img = Image.fromarray(np.uint32(rawdepth[i] * 10000))

    depths_img=depths_img.transpose(Image.FLIP_LEFT_RIGHT)
    rawdepth_img=rawdepth_img.transpose(Image.FLIP_LEFT_RIGHT)


    iconpath_1 = PATH[1]+'/image_' + str("%04d" % (i+1)) + '.png'
    iconpath_2 = PATH[2] + '/image_' + str("%04d" % (i + 1)) + '.png'

    depths_img.save(iconpath_1, 'PNG', optimize=True)
    rawdepth_img.save(iconpath_2, 'PNG', optimize=True)
    print("This is: ",("%04d" % (i+1)))
