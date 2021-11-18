import subprocess

def cut_ffmpeg(ini, fin):
    subprocess.call(
        ["ffmpeg", "-ss", str(ini), "-i", "BBB.mp4", "-c", "copy", "-t",
         str(fin),"BBB_short.mp4"])

def YUV_hist():
    subprocess.call(["ffmpeg", "-i", "BBB_short.mp4", "-vf",
                     "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay",
                     "BBB_hist.mp4"])

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

def change_audio():
    subprocess.call(["ffmpeg","-i","BBB_short.mp4","-ac", "1", "-c:a","aac",
                     "BBB_audio.mp4"])

def main():
    opt = 0
    while (opt != 8):
        opt = int(input('Tria l\'exercici que vulguis:\n1-Tallar el vídeo\n'
                        '2-Fer l\'histograma\n3-Canviar la qualitat\n'
                        '4-Canviar l\'àudio\n\nPrem 8 si vols sortir\n'))
        if (opt==1):
            # Demanem a l'usuari que introdueixi una duració
            ini = int(input('Principi video:'))
            fin = int(input('Final video:'))

            # Cridem a la funció per tallar el vídeo
            cut_ffmpeg(ini, fin)

        if (opt==2):
            YUV_hist()

        if (opt==3):
            option = 0
            while (option != 8):
                option = int(input('Tria la qualitat que vulguis:\n'
                               '1-720p\n2-480p\n3-360x240\n4-160x120\n'
                               '\nPrem 8 si vols sortir\n'))
                low_quality(option);
        if (opt==4):
            change_audio()

if __name__=="__main__":
    main()