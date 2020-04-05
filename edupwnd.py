#Script for pwding edupage from the XSS vunerability
#Usage: 

import requests
import sys
import webbrowser
import getopt
import flask


#functinality
#-generate js -> url option
#-translate cookie string from link into valid edupage link
#-create flask server n listen at port x, wait for cookie n translate

#list of all possible usage cases and flags
possibilities = {
    "download": {
        "desc":"downloads all nessecary files for setup",
        "flags": {
            "-d":"download dir"
        }  
    },
    "generate" : {
        "desc":"Generates malicious url + js for sniffing use, built for specific port & user url",
        "flags": {
            "-r":"url where listening server will be set up (default: localhost)",
            "-p":"port of listening server (default: 80)",
            "-n":"name of js script (default: 4 random characters)"
        }
    },
    "server"   : {
        "desc":"Hosts local server on select port listning to",
        "flags": {
            "-p":"listening port",
            "-l":"log file (default: none)"
        }
    },
    "genserve"     : {
        "desc":"generates malicious link and then creates listning server",
        "flags": {
            "-r":"url where listening server will be set up (default: localhost)",
            "-P":"port to which JS sends (same as '-P')",
            "-p":"port of listening server (default: 80)",
            "-n":"name of js script (default: random characters)",
            "-l":"log file"
            
        }
    }
}

#class arguments:
 #   def __init__(self, args):
        
    


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[50m'
    OKWHITE = '\033[0m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_help():
    print(f"\n{bcolors.BOLD}USAGE:{bcolors.OKWHITE}\n(python) edupwnd(.py) MODE [options]\n")
    print()
    print(f"{bcolors.BOLD}MODES:{bcolors.OKWHITE}")
    for mode in possibilities:
        print(f"\t{mode}: \t{possibilities[mode]['desc']}")
    print()
    print("Mode specific flags: ")
    print()
    for mode in possibilities:
        print(f"\t{bcolors.BOLD}{mode}{bcolors.OKWHITE}")
        for flag in possibilities[mode]["flags"]:
            print(f"\t  {flag}\t{possibilities[mode]['flags'][flag]}")

        print()
    


def print_log(msg):
    print(f"[{bcolors.OKWHITE}!] LOG: {msg}")


def print_warning(msg):
    print(f"[{bcolors.WARNING}!{bcolors.OKWHITE}] {bcolors.WARNING}WARNING:{bcolors.OKWHITE} {msg}")

def print_error(msg):
    print(f"[{bcolors.FAIL}!{bcolors.OKWHITE}] {bcolors.FAIL}ERROR:{bcolors.OKWHITE} {msg}")

def print_logo():
    print(f"""{bcolors.OKBLUE}
    ███████╗██████╗ ██╗   ██╗██████╗ ██╗    ██╗███╗   ██╗██████╗  
    ██╔═══ ╝██╔══██╗██║   ██║██╔══██╗██║    ██║████╗  ██║██╔══██╗ 
    █████╗  ██║  ██║██║   ██║██████╔╝██║ █╗ ██║██╔██╗ ██║██║  ██║ 
    ██╔══╝  ██║  ██║██║   ██║██╔═══╝ ██║███╗██║██║╚██╗██║██║  ██║ 
    ███████╗██████╔╝╚██████╔╝██║     ╚███╔███╔╝██║ ╚████║██████╔╝ 
    ╚══════╝╚═════╝  ╚═════╝ ╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝╚═════╝  
    {bcolors.OKWHITE}""")
    print()
    print(f"Edupage xss exploit tool by {bcolors.BOLD}skittish{bcolors.OKWHITE} 2020")
    print("")
    print_warning("""legal disclaimer, Usage of EDUPWND for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program""")
    print("")
    print("HELP: --help / -h\n\n")

def validate_flags(mode, flags):
    flag_output = []
    for i in range(len(flags)):
        if i%2==0:
            if not flags[i] in possibilities[mode]["flags"].keys():
                print_error(f"\"{flags[i]}\" is not a valid flag! To see valid flags use -h / --help")
            else:
                if i+1 == len(flags):
                    print_error(f"no argument provided for flag\"{flags[i]}\"  for help use: -h / --help")
                else:
                    flag_output += [flags[i],flags[i+1]]
    return flag_output




def generate():
    pass
def download():
    pass
def server():
    pass
def genserve():
    pass
def handleInputs(input):
    
    if ("-h" in input) or ("--help" in input):
        print_help()
        exit()
    if (len(input) < 2 or not input[1] in possibilities.keys()):
        print_error("NO mode provided, please use -h / --help for help")
        exit()
    mode = input[1]
    print_log(f"starting EDUPWND with mode {mode}")
    flags=input[2:]
    flag_pairs = validate_flags(mode,flags)
    print(flag_pairs)
    if mode == "download":
        pass
    elif mode == "generate":
        pass
    elif mode == "server":
        pass
    elif mode == "genserve":
        pass
    

def main(argv):
   print_logo()
   handleInputs(argv)
   #print_help()
   #for()

if __name__ == "__main__":
   main(sys.argv)
