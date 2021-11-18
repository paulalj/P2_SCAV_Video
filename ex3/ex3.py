import subprocess

def low_quality(option):
    if (option==1):
        subprocess.call(["ffmpeg", "-i", "BBB_short.mp4", "-vf",
                         "scale=-1:720", "BBB_720.mp4"])
    if (option==2):
        subprocess.call(["ffmpeg", "-i", "BBB_short.mp4", "-vf",
                         "scale=480:-1", "BBB_480.mp4"])
    if (option==3):
        subprocess.call(["ffmpeg", "-i", "BBB_short.mp4", "-s",
                         "360x240", "BBB_360x240.mp4"])
    if (option==4):
        subprocess.call(["ffmpeg", "-i", "BBB_short.mp4", "-s",
                         "160x120", "BBB_160x120.mp4"])

def main():
    option=0
    while(option!=8):
        option = int(input('Tria la qualitat que vulguis:\n'
                           '1-720p\n2-480p\n3-360x240\n4-160x120\n'
                           '\nPrem 8 si vols sortir\n'))
        low_quality(option);

if __name__ == "__main__":
    main()