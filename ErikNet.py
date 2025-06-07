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
      escolha = int(input("escolha > "))
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
    print("[1] busca vunerabilidade")
    print("[2] banco de dados")
    print("[3] tabelas")
    print("[4] extrair dados")
    print("[0] exit")
    try:
      escolha = int(input("escolha > "))
      url = input("url > ")
      banco_de_dados = input("banco de dados > ")
      tabela = input("a tabela > ")
      if escolha == 1:
        os.chdir("sqlmap")
        os.system('python sqlmap.py -u {url} --dbs')
        os.system("")
      elif escolha == 2:
        os.chdir("sqlmap")
        os.system('python sqlmap.py -u {url} -D {banco_de_dados} --tables')
        os.chdir("")
      elif escolha == 3:
        os.chdir("sqlmap")
        os.system('python sqlmap.py -u {url} -D {banco_de_dados} -T {tabela} --columns')
        os.chdir("")
      elif escolha == 4:
        os.chdir("sqlmap")
        os.system('python sqlmap.py -u {url} -D {banco_de_dados} -T {tabela} --dump')
        os.chdir("")
      elif escolha == 5:
        os.chdir("")
        clear()
        menu()
    except:
      print("invalido ou a ferramenta nao esta abaiaxada")

def nmap():
  while True:
    banner()
    print("[1] scanner basico(nmap 127.0.0.1)")
    print("[2] scanner ip ativo(nmap -sn 127.0.0.1)")
    print("[3] scanner versao(nmap -sV 127.0.0.1)")
    print("[4] scanner portas(nmap -p- 127.0.0.1)")
    print("[5] scanner geral(nmap -A -v 127.0.0.1)")
    escolha = input("escolha > ")
    if escolha == 1:
      

