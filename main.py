try:
    from sys import argv, exit

    # Importing components
    import copy_lib

    if "-v" in argv[1:] or "--version" in argv[1:]:
        print("Copy Version 1.0.0")
    if "-h" in argv[1:] or "--help" in argv[1:]:
        print("""
-v, --version                                   Prints the current version of copy
-h, --help                                      Gives you help.
          
[source] [destination-1] [destination-2]        Copy data from source file to all given destinations
""")
          
    copyargs = argv[1:]

    def argCleaner(clean):
        while True:
            try:
                copyargs.remove(clean)
            except ValueError:
                break

    argCleaner("-v")
    argCleaner("-h")
    argCleaner("--version")
    argCleaner("--help")

    if len(copyargs) < 2:
        print("copy: Not enough arguments.")
        exit()
except KeyboardInterrupt:
    print(f"copy: Keyboard Interrupt received during preload.")
    exit()
except EOFError:
    print(f"copy: Keyboard Interrupt received during preload.")
    exit()
except Exception as x:
    print(f"copy: Unknown exception during preload. \ncopy: Given information: {x}")
    exit()

try:
    copy_lib.copy_paste(file=copyargs[0], outfiles=copyargs[1:])
except FileNotFoundError as x:
    print(f"copy: Not able to find source file. \ncopy: Given information: {x}")
except PermissionError as x:
    print(f"copy: Not enough permissions to read and/or write to/from files. \ncopy: Given information: {x}")
except UnicodeError as x:
    print(f"copy: Unicode-related error. \ncopy: Given information: {x}")
except KeyboardInterrupt:
    print(f"copy: Keyboard Interrupt received.")
except EOFError:
    print(f"copy: Keyboard Interrupt received.")
except Exception as x:
    print(f"copy: Unknown exception. \ncopy: Given information: {x}")
