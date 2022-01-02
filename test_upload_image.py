#!/usr/bin/env python3
# Original: Copyright (c) 2019 Jarret Dyrbye
# Addded File Upload Capabilities giddyhup@github, 2021
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php

import time
import sys

from waveshare.epaper import EPaper
from waveshare.epaper import Handshake
from waveshare.epaper import SetStorageMode

if __name__ == '__main__':
    with EPaper() as paper:
        try:
            fname = sys.argv[1]
            fullpath = sys.argv[2]
        except:
            print(f'Please supply a file for transfer (short name and full path) e.g.\n'
            f'{sys.argv[0]} TEST.JPG /home/pi/images/test.jpg')
            exit()
        paper.send(Handshake())
        time.sleep(2)
        paper.send(SetStorageMode(b'\x01'))
        time.sleep(2)
        paper.transmitImage(fname.encode(), fullpath.encode())
        time.sleep(1)
