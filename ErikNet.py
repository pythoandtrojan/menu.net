
import os 
import time 

def limpar():
  os.system('cls' if os.name == 'nt' else 'clear')

def clear():
  os.system('clear')
  
def banner():
    print("  ______     _ _  _   _ _   _ ______ _   ")
    print(" |  ____|   (_) || \ | | \ | |  ____| |  ")
    print(" | |__   ___ _| ||  \| |  \| | |__  | |_ ")
    print(" |  __| / __| | || . ` | . ` |  __| | __|")
    print(" | |____\__ \ | || |\  | |\  | |____| |_ ")
    print(" |______|___/_|_||_| \_|_| \_|______|\__|")
    print("                                         ")
    print("              erikNEt                   ")

def menu():
  while True:
    print("[1] nmap   [2] sqlmap")
    print("[3] holehe [4] exit")
    try:
      escolha = int(input("escolha > ")
      if escolha == 1:
        clear()
        nmap()
      elif escolha == 2:
        clear()
        sqlmap()
      elif escolha == 3:
        nome = input("vitima: > ")
        os.system('holehe {nome}')
        limpar()
      elif escolha == 4:
        exit()
      else:
        print("invalido")
    except:
      print("voce teve um erro!")
      
def sqlmap():
  while True:
    banner()
    
