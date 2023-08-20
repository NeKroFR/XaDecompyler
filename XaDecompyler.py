import sys,base64,zlib, io


def decompile(code_list):
    """
    Decompile the code obfuscated by XaCompyle: https://github.com/XaDanX/XaCompyle
    """
    code = ""
    for l in code_list:
        code+=l
    code = code.replace("exec","print")
    code = getoutput(code)
    print(code)
    code = code.replace(";","\n").replace('exec','print')[2:-2]
    code = getoutput(code)[2:-2]
    print(code)
    return code

def getoutput(code):
    """
    return code output
    """
    output = io.StringIO()
    sys.stdout = output
    exec(code)
    sys.stdout = sys.__stdout__
    return output.getvalue()



def gui():
    banner = """
██╗  ██╗ █████╗         ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗   ██╗██╗     ███████╗██████╗ 
╚██╗██╔╝██╔══██╗        ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗ ████║██╔══██╗╚██╗ ██╔╝██║     ██╔════╝██╔══██╗
 ╚███╔╝ ███████║        ██║  ██║█████╗  ██║     ██║   ██║██╔████╔██║██████╔╝ ╚████╔╝ ██║     █████╗  ██████╔╝
 ██╔██╗ ██╔══██║        ██║  ██║██╔══╝  ██║     ██║   ██║██║╚██╔╝██║██╔═══╝   ╚██╔╝  ██║     ██╔══╝  ██╔══██╗
██╔╝ ██╗██║  ██║███████╗██████╔╝███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║██║        ██║   ███████╗███████╗██║  ██║██╗
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝        ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝
"""
    print(banner)
    filename = input("""\033[1;35mDrag the file to be desobfuscated here : \033[0m""")
    if filename[0] == filename[-1]:
        if filename[0] == "'" or filename[0] == '"':
            filename = filename[1:-1]

    return filename

def open_file(filename):
    if filename[-3:] != ".py":
        print("\033[91mError: \033[0myou need to choose a python file!")
        sys.exit()
    try:
        f = open(filename, "r", encoding='utf-8')
        content = f.read()
        cuted_file = content.splitlines()
        return cuted_file 
    except:
        print("\033[91mError: \033[0mfile doesn't exist!")
        sys.exit()

def save_file(code, filename):
    f = open(filename, "w",encoding="utf-8")
    f.write(code.replace('\\n', '\n'))
    print("\033[1;32mSuccess:\033[0m the file has been successfully desobfuscated")


if __name__ == "__main__":
    a = len(sys.argv)
    if a == 1:
        filename = gui()
        desobfuscated_filename = filename[:-3]+"_desobfuscated.py"        
    elif a == 2:
        filename = sys.argv[1]
        desobfuscated_filename = filename[:-3]+"_desobfuscated.py"
    elif a == 3:
        filename = sys.argv[1]
        desobfuscated_filename = sys.argv[2]
    else:
        print("Error: too many arguments")
        exit()
    desobfuscated = decompile(open_file(filename))
    save_file(desobfuscated, desobfuscated_filename)