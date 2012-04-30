import os

if __name__ == "__main__":
    for file in os.listdir("."):
        i = file
        o = file.replace(".wav",".mp3")
        os.system("lame -V0 \"" + i + "\" \"" + o + "\"")
        
