import os
from moviepy.editor import VideoFileClip


path = 'C:\\Clips' # you can write any folders, if you want to find entire disk, C:\\ enough
def clipBul(dosyaYolu,uzantısı):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if ('.'+uzantısı) in file:
                files.append(os.path.join(r, file))
    for f in files:
        single = f
        double = single.replace('\\', '\\\\')
        clip = VideoFileClip(double)
        if  5 < clip.duration <= 60.0 : 
            print(double)
    print(files)
    return files
