import os
import shutil

fromdir ="C:/Users/HP/OneDrive/Desktop/C102_assets-main"
todir="C:/Users/HP/OneDrive/Desktop/C102_assets-main"
listoffiles=os.listdir(fromdir)
for file in listoffiles:
    name,ext = os.path.splitext(file)
    if ext=="":
        continue
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:

        path1=fromdir + '/' + file
        path2=todir+"/"+"imagefiles"
        path3=todir+"/"+"imagefiles" + '/' + file
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)


        

