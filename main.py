from time import sleep
import win32api
from win32con import VK_MEDIA_PLAY_PAUSE, KEYEVENTF_EXTENDEDKEY

from run import RasaSpeaker

def media_play_pause():
    if True:
        pass
    else:    
        win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)


def main():
    media_play_pause()

    RasaSpeaker().speak()

    sleep(2)
    media_play_pause()


if __name__ == "__main__":
    main()
