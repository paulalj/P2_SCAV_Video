import subprocess

def YUV_hist():
    subprocess.call(["ffmpeg", "-i", "BBB_short.mp4", "-vf",
                     "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay",
                     "BBB_hist.mp4"])

def main():
    YUV_hist();

if __name__=="__main__":
    main()