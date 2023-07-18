from sys import stdout
from os import get_terminal_size

def progress(cur, total):
    percent = cur / total * 100
    percent = float(percent)
    minus = "-"
    width = get_terminal_size().columns
    if percent == 0:
        stdout.write("\r[" + "-" * (int(width) - 9) + "] | 0%")
    else:
        fill_multiplier = int((width - 9) / (100 / percent))
        stdout.write("\r[" + f"{minus * (width - 11)}".replace("-", "#", fill_multiplier) + "] | XXX%".replace("XXX", str(round(percent, 2))))
    stdout.flush()

def copy_paste(file: str, outfiles: list):
    cache = open(file, "rb")
    length = len(cache.read()) * len(outfiles)
    progresscount = 0

    for outfile in outfiles:
        cache.seek(0, 0)
        with open(outfile, "wb") as o:
            while True:
                chunk = cache.read(128)
                if not chunk:
                    break
                progress(progresscount, length)
                o.write(chunk)
                progresscount += 128
    stdout.write("\r[" + "#" * int(get_terminal_size().columns - 9) + "] | 100%")
    stdout.flush()

