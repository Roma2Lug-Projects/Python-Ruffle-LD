import os
import json
import shutil
from time import time
CONFIG_PATH = r"./config"
DISP_PATH = CONFIG_PATH + r"/premi.json"
def write(j):
    with open(DISP_PATH, "w") as f:
        f = json.dump(j,f)
def load():
    if not(os.path.exists(CONFIG_PATH)):
        os.makedirs(CONFIG_PATH)
    if not(os.path.exists(DISP_PATH)):
        with open(DISP_PATH, "w") as f: pass
    try:
        with open(DISP_PATH, "r+") as f:
            j = json.load(f)
            return j
    except Exception as E:
        print(E)
        return {}
def get_one_item(j: dict) -> str:
    while True:
        print("secgli uno dei seguenti item")
        print("".join(x + "\n" for x in j.keys() ))
        item = input("--->")
        if item in j.keys():
            break
        print("riprova l\'item non e\' presente")
    return item

if __name__=="__main__":
    while True:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print("1)inserire un nuovo prodotto")
        print("2)modificare un prodotto")
        print("3)eliminare un prodotto")
        print("0)uscire")
        j = load()
        option = int(input("--->"))
        match (option):
            case 1:
                name = str(input("dimmi il nome del nuovo prodotto\n--->"))
                amount = int(input("dammi il numero di prodotti da aggiungere\n--->"))
                percentage = int(input("dammi il numero di peso nel calcolo randomico che questo prodotto dovra avere\n--->"))
                j.update({name: {"amount": amount, "percentage": percentage}})
                write(j)
            case 2:
                item = get_one_item(j)
                option_2 = int(input("cosa vuoi modificare\n0)quantita\'\n1)il suo peso nella randomizzazione\n--->"))
                valore = int(input("ok dammi il valore da inserire al posto del vecchio\n--->"))
                if option_2:
                    j[item]["percentage"] = valore
                else:
                    j[item]["amount"] = valore
                write(j)
            case 3:
                item = get_one_item(j)
                j.pop(item)
                write(j)
            case 0:
                break
                
                
                    