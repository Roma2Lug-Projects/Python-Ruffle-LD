import json
import os
from sys import maxsize
import random
from time import time
CONFIG_PATH = r"./config"
DISP_PATH = CONFIG_PATH + r"/premi.json"

def load():
#load up the file with the prizes for the raffler
#@return : dictionary
	if not (os.path.exists(CONFIG_PATH)): #check if file path to config exists
		raise Exception("file path does not exists!")
	with open(DISP_PATH, "r+") as f: #open file with prizes
		j = json.load(f) #load the file in a json object
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

	#loading up the prizes
	j = load()
	#ask the user for the numbero for the seed of the rand function
	while True:
		print(f"Inserisci un numero compreso tra 0 e infinito")
		seed = int(input("--->"))
		#get max nr of product
		max_prod= get_nr_product(j)
		print(max_prod, j)
		#get random number from max product and seed
		nr = random_number(seed, max_prod)
		print(f"Complimenti hai estratto  il numero {nr}")
		#get the product
		print("complimenti hai vinto: " + get_product(j, nr))
