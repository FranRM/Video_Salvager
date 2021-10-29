# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import subprocess
import signal
import vlc
import time
import ipdb


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def video_instance(source, video):
    print(video)
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(source)
    player.set_media(media)
    player.play()
    time.sleep(0.5)
    duration = player.get_length()
    # data = player.get_type()
    # print("Data : " + str(data))
    if duration == 0:
        print("Error en : " + str(video))
        player.stop()
        return False
    player.stop()
    return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Femio')
    list = os.listdir('/home/femio/recovered_videos')

    for video in list:
        # try:
        # video('/home/femio/recovered_videos/%s' % video)
        if video_instance('/home/femio/recovered_videos/%s' % video, video):
            with open('/home/femio/recovered_videos/%s' % video, "rb") as file_reading:
                with open('/home/femio/salvaged_videos/%s' % video, "wb") as binary_file:
                    binary_file.write(file_reading.read())
            os.remove('/home/femio/recovered_videos/%s' % video)
        # video('/home/femio/recovered_videos/[002127].mp4', player)
        # ipdb.set_trace()
        # media = vlc.MediaPlayer()
        # media.play()
        # except:
        #     print('ERROOOOOR: %s' % video)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
