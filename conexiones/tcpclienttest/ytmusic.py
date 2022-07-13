import subprocess
from subprocess import PIPE
import time


def main():
    cmd = "C:\\Users\\Claudio\\Programas y demas\\mpv-x86_64-20220626-git-3a2838c\\mpv.com"
    # url = "https://music.youtube.com/watch?v=DNOuancg5RY&feature=share"
    url = "https://music.youtube.com/watch?v=8l0tk_sEhPs&feature=share"
    # output = subprocess.run([cmd, "--no-video", url])
    # print(output)
    # time.sleep(3)

    p = subprocess.Popen([cmd, "--no-video", url], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=False)
    time.sleep(5)
    p.communicate(input=b'q')


if __name__ == '__main__':
    main()
