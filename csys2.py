import sys
command = None
text = {}
if len(sys.argv) == 3 and sys.argv[1] == "-c":
    try:
        with open(sys.argv[2], encoding="utf-8") as file:
            command = file.read().split("\n")
            for a in range(len(command)):
                text[a] = command[a].split(" ")
        with open(sys.argv[2].replace(".csy",".asm"), encoding="utf-8","x") as file:
            file.write("")
    except FileNotFoundError:
        print("What is this file?")
        
    
