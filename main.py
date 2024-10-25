import json
import os
from sys import maxsize
import random
from time import time
import shutil
CONFIG_PATH = r"./config"
DISP_PATH = CONFIG_PATH + r"/premi.json"

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def load():
#load up the file with the prizes for the raffler
#@return : dictionary
	if not (os.path.exists(CONFIG_PATH)): #check if file path to config exists
		os.makedirs(CONFIG_PATH)
	if not (os.path.exists(DISP_PATH)):
		with open(DISP_PATH, "w") as f: f.write("")
	with open(DISP_PATH, "r+") as f: #open file with prizes
		try:
			j = json.load(f) #load the file in a json object
		except json.decoder.JSONDecodeError as E:
			print("il tuo json file e' vuoto!!!!!!!!!!!")
			input("")
			os._exit(0)
		except:
			raise Exception("something went wrong and I have no idea what")
	shutil.copy(DISP_PATH, CONFIG_PATH + "\\copy_premi"+ str(int(time())) +".json")
	return j

def get_nr_product(j: dict):
#return the nr of product
#@par1 j: dict; dictionary with all product
#@return :tuple: int, dict
	temp = 0
	for item in j:
		if j[item]["amount"] != 0:
			temp += j[item]["percentage"]
	return temp

def random_number(seed: int, max_product: int) -> int:
#@par1 seed: int; seed used in random  function
#@return : int
	random.seed(seed + int(time()))
	return random.randint(1, max_product)

def get_product(j: dict,nr:int) ->str:
#decide the product to give based on the number and the program
#@par1 j: dict;
#@par2 nr: int;
#@return: str;
	for item in j:
		if j[item]["amount"] != 0:
			if j[item]["percentage"] >= nr:
				j[item]["amount"] -= 1
				with open (DISP_PATH, "w") as f:
					json.dump(j, f)
				return item
			else:
				nr -= j[item]["percentage"]


if __name__ == '__main__':
	print("Sistema di estrazione dei premi per il Linux Day 2024\n")
	print("Caricamento dei dati")
	clear()
	#loading up the prizes
	j = load()
	#ask the user for the numbero for the seed of the rand function
	while True:
		print(f"Inserisci un numero compreso tra 0 e infinito")
		while True:
			try:
				seed = int(input("--->"))
				break
			except ValueError as E:
				print("inserisci un numero per favore")
			except:
				raise Exception("something went wrong and I have no idea what")
		#get max nr of product
		max_prod= get_nr_product(j)
		print(max_prod, j)
		#get random number from max product and seed
		nr = random_number(seed, max_prod)
		print(f"Complimenti hai estratto  il numero {nr}")
		#get the product
		print("complimenti hai vinto: " + get_product(j, nr))
		input()
		clear()
