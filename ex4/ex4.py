import subprocess

def change_audio():
    subprocess.call(["ffmpeg","-i","BBB_short.mp4","-ac", "1", "-c:a","aac",
                     "BBB_audio.mp4"])

def main():
    change_audio()

if __name__=="__main__":
    main()