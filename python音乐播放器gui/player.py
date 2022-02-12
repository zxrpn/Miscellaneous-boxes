from playsound import playsound
import easygui
import os
files = os.listdir()
play = easygui.choicebox("你要播放哪个音频文件?",
choices = files)
playsound(play)