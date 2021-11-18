import subprocess

def cut_ffmpeg(ini, fin):
    subprocess.call(
        ["ffmpeg", "-ss", str(ini), "-i", "BBB.mp4", "-c", "copy", "-t", str(fin),
         "BBB_short.mp4"])

def main():
    # Demanem a l'usuari que introdueixi una duració
    ini = int(input('Principi video:'))
    fin = int(input('Final video:'))

    #Cridem a la funció per tallar el vídeo
    cut_ffmpeg(ini, fin)

if __name__=="__main__":
    main()