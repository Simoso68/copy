from sys import stdout
from os import get_terminal_size
from config_loader import *

conf = parseCFG()

def progress(cur, total):
    percent = cur / total * 100
    percent = float(percent)
    width = get_terminal_size().columns
    if percent == 0:
        stdout.write(f"\r{conf[2]}" + conf[1] * (int(width) - 9) + f"{conf[3]} | 0%")
    else:
        fill_multiplier = int((width - 9) / (100 / percent))
        stdout.write(f"\r{conf[2]}" + f"{conf[1] * (width - 11)}".replace(conf[1], conf[0], fill_multiplier) + f"{conf[3]} | XXX%".replace("XXX", str(round(percent, 2))))
    stdout.flush()

def copy_paste(file: str, outfiles: list):
    cache = open(file, "rb")
    length = len(cache.read()) * len(outfiles)
    progresscount = 0

    for outfile in outfiles:
        cache.seek(0, 0)
        chunksize = conf[4]
        with open(outfile, "wb") as o:
            while True:
                chunk = cache.read(chunksize)
                if not chunk:
                    break
                progress(progresscount, length)
                o.write(chunk)
                progresscount += chunksize
    stdout.write(f"\r{conf[2]}" + conf[0] * int(get_terminal_size().columns - 9) + f"{conf[3]} | 100%")
    stdout.flush()