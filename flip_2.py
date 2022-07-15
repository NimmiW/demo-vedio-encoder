import os

def flip_vertically(in_file, out_file):
    os.system("ffmpeg -i "+in_file+" -vf \"vflip\"  -vcodec libx264 -acodec aac -strict experimental "+out_file+" -y")



out_file = 'out.mp4'
in_file = 'in_3.mp4'
flip_vertically(in_file, out_file)
