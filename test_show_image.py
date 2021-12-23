#!/usr/bin/env python3
# Original: Copyright (c) 2019 Jarret Dyrbye
# Addded File Upload Capabilities giddyhup@github, 2021
# Distributed under the MIT software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php

import time
import sys

from waveshare.epaper import EPaper
from waveshare.epaper import Handshake
from waveshare.epaper import RefreshAndUpdate
from waveshare.epaper import SetPallet
from waveshare.epaper import SetCurrentDisplayRotation
from waveshare.epaper import DisplayImage
from waveshare.epaper import SetStorageMode

def showImage(fname):
    paper.send(SetStorageMode(b'\x01'))
    paper.send(DisplayImage(3, 3, fname.encode()))
    

if __name__ == '__main__':
    with EPaper() as paper:
        try:
            fname = sys.argv[1]
        except:
            print(f'Please supply a file to be displayed, e.g.\n'
            f'{sys.argv[0]} TEST.JPG')
            exit()
        paper.send(Handshake())
        time.sleep(2)
        paper.send(SetPallet(SetPallet.BLACK, SetPallet.WHITE))
        paper.send(SetCurrentDisplayRotation(SetCurrentDisplayRotation.FLIP))
        showImage(fname)
        time.sleep(6)
        paper.send(RefreshAndUpdate())
        time.sleep(4)
        