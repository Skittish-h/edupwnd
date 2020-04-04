#Script for pwding edupage from the cookie XSS vunerability cookies
#Usage: 
''' Example header 

{"Response Headers (508 B)":
    {"headers":
        [
            {"name":"Cache-Control","value":"no-store, no-cache, must-revalidate"},
            {"name":"Cache-Control","value":"post-check=0, pre-check=0"},
            {"name":"Connection","value":"Keep-Alive"},
            {"name":"Content-Length","value":"0"},
            {"name":"Content-Type","value":"text/html; charset=UTF-8"},
            {"name":"Date","value":"Fri, 03 Apr 2020 16:47:51 GMT"},
            {"name":"Expires","value":"Mon, 26 Jul 1997 05:00:00 GMT"},
            {"name":"Keep-Alive","value":"timeout=1, max=100"},
            {"name":"Last-Modified","value":"Fri, 03 Apr 2020 16:47:51 GMT"},
            {"name":"Location","value":"https://ssnovohradska.edupage.org/user/?ESID=d65b85bf621eea0f787c9c0fb801c65b&hsid=b27dfb1bcc26345250300d80536304f4db9c0a0e"},
            {"name":"Pragma","value":"no-cache"},{"name":"Server","value":"Apache"}]}}
'''
import requests
import sys
import webbrowser
import getopt


#functinality
#-generate js -> url option
#-translate cookie string from link into valid edupage link
#-create flask server n listen at port x, wait for cookie n translate

#list of all possible usage cases and flags
possibilities = {
    "generate" : {
        "desc":"Generates malicious url + js for sniffing use, built for specific port & user url",
        "flags": {
            "-r":"url where listening server will be set up (default: localhost)",
            "-p":"port of listening server (default: 80)",
            "-n":"name of js script (default: 4 random characters)"
        }
    },
    "translate": {
        "desc":"Generates output cookie based on provided input cookie",
        "flags": {
            "-c":"cookie input"
        }
    },
    "server"   : {
        "desc":"Hosts local server on select port listning to",
        "flags": {
            "-p":"listening port",
            "-l":"log file"
        }
    },
    "genserve"     : {
        "desc":"generates malicious link and then creates listning server",
        "flags": {
            "-r":"url where listening server will be set up (default: localhost)",
            "-p":"port of listening server (default: 80)",
            "-n":"name of js script (default: random characters)",
            "-l":"log file"
        }
    }
}


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




def print_warning(msg):
    print(f"[{bcolors.WARNING}!{bcolors.OKWHITE}] {bcolors.WARNING}WARNING:{bcolors.OKWHITE} {msg}")

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
    print("HELP: --help / -h")




def main(argv):
   print_logo()
   print_help()
   #for()

if __name__ == "__main__":
   main(sys.argv[1:])
