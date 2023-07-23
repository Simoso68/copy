# Copy

Fancier way to copy things around!

## Can copy everything

This can copy everything, even binary!

![image](https://github.com/Simoso68/copy/assets/87707341/d94feca5-b2e9-45db-a20f-0618b1f657bf)


## Installing

### Linux

```bash
sudo curl https://github.com/Simoso68/copy/raw/main/bin/copy -sS -L -o /usr/bin/copy && sudo chmod +x /usr/bin/copy
```

### Windows

Still baking, stay tuned! \
But it can be built using PyInstaller.

### MacOS

I don't know anything about MacOS, you need to build it yourself.

## Configuring

### Default Configuration

```json
{
    "progressbar": {
        "bar": {
            "completed":"#",
            "incomplete":"-"
        },
        "container": {
            "opening":"[",
            "closing":"]"
        }
    },
    "backend": {
        "chars-per-iteration":256
    }
}
```

### Progressbar

You can modify the progressbar, its completed element, the text shown for incomplete parts of the progress and the bar containers on each of the sides. \
Please keep those strings only one character large, if you don't want, that the progressbar bugs out.

### Backend

Currently, there is only one setting, chars-per-iteration, it means how many chars copy reads before writing them to the output. \
The default value is 256, but you can increase it to make your program faster, but the progress bar might bug out, when the value is to high or decreasing it, \
to make the process slower, but the progressbar more accurate. \
Setting the value to 0 will create the output files, but won't write to them.

### Automatic recreation

If no config file exists, copy will create one for you and let you know. \
The config file has the default format, which you can see under the Default Configuration section in this README file.

### Config Parsing Errors

If the configuration file is invalid, copy won't copy any file and instantly lets you know about the error and then exits.

### Location on your filesystem

#### Windows

```C:/Users/USERNAME/.copy.conf.json```

#### Linux or MacOS

```/home/USERNAME/.copy.conf.json```