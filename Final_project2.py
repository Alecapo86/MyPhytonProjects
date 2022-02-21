import subprocess
import logging

maclist = []

logging.basicConfig(filename="Filelog.txt", format='%(asctime)s %(message)s',filemode="w")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


addresses = subprocess.check_output(['arp', '-a'])
addresses = maclist.append(addresses)


def print_duplicates():
    dup = [x for i, x in enumerate(maclist)if i != maclist.index(x)]
    for item in dup:
        if item.count("-")==5:          
            with open("Filelog.txt", "a") as out:
                out.write(item + "\n")
                out.close()

   

def log_duplicates():
    for elem in maclist:
        if maclist.count(elem)>1:
            
            logging.warning("Warning, there are duplicates in the MAC list. You might be under attack. \n The address is: \n")
            
        else:
            
            logging.debug("Everything is fine, there are no duplicates in the MAC list. ")
    

print_duplicates()
log_duplicates()
    
    
    






