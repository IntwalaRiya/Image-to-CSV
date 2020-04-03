from PIL import Image
import numpy as np
import os
import csv

for subdir, dirs, files in os.walk("E:/batch1/"):    
        for filename in files:
            #print(subdir)
            img_file = Image.open(os.path.join(subdir, filename))
            #img_file.show()
        
            # get original image parameters...
            width, height = img_file.size
            format = img_file.format
            mode = img_file.mode
        
            newsize = (160,160) 
            img_file1 = img_file.resize(newsize) 

            value = np.asarray(img_file1.getdata(), dtype=np.int).reshape((img_file1.size[1], img_file1.size[0]))
            value = value.flatten()
            #print(value)
            file = "E:/" + os.path.basename(subdir) + ".csv"
            #print(file)

            with open(file, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(value)
