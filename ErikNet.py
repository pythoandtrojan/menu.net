import os
import requests
import json
import socket
import re
from datetime import datetime
import time
import sys
from urllib.parse import urlparse

# Cores para o terminal
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Banner da ferramenta
def banner():
    print(colors.BLUE + """
   ____                 _     __  __       _        _       
  / ___| ___   ___   __| |   |  \/  | __ _| |_ _ __(_)_  __ 
 | |  _ / _ \ / _ \ / _` |   | |\/| |/ _` | __| '__| \ \/ / 
 | |_| | (_) | (_) | (_| |   | |  | | (_| | |_| |  | |>  <  
  \____|\___/ \___/ \__,_|___|_|  |_|\__,_|\__|_|  |_/_/\_\ 
                     |_____|                                
    """ + colors.RESET)
    print(colors.YELLOW + "="*60 + colors.RESET)
    print(colors.GREEN + "Ferramenta de Busca de Informações Online" + colors.RESET)
    print(colors.YELLOW + "="*60 + colors.RESET)
    print(colors.CYAN + "Opções disponíveis:" + colors.RESET)
    print(colors.WHITE + "[1] Verificar onde um e-mail está cadastrado")
    print("[2] Buscar redes sociais por nome")
    print("[3] Verificar logins por nome de usuário")
    print("[4] Geolocalização por IP")
    print("[5] Verificar URL com Gabylfi")
    print("[6] Sair" + colors.RESET)
    print(colors.YELLOW + "="*60 + colors.RESET)

# Verificador de e-mail (simplificado)
def check_email(email):
    print(colors.BLUE + "\n[+] Verificando onde o e-mail está cadastrado..." + colors.RESET)
    
    # Lista de sites para verificar (simulada)
    sites = {
        "Google": f"https://accounts.google.com/signin/v1/lookup?continue=https://myaccount.google.com/&flowName=GlifWebSignIn&flowEntry=ServiceLogin&email={email}",
        "Facebook": f"https://www.facebook.com/login/identify/?ctx=recover&email={email}",
        "Twitter": f"https://twitter.com/account/begin_password_reset?email={email}",
        "Instagram": f"https://www.instagram.com/accounts/emailsignup/?email={email}",
        "LinkedIn": f"https://www.linkedin.com/uas/request-password-reset?email={email}",
        "Microsoft": f"https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct={int(time.time())}&email={email}"
    }
    
    for site, url in sites.items():
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            if response.status_code == 200:
                print(colors.GREEN + f"[+] Possível cadastro encontrado em: {site}" + colors.RESET)
            else:
                print(colors.RED + f"[-] Não encontrado em: {site}" + colors.RESET)
        except:
            print(colors.YELLOW + f"[!] Erro ao verificar: {site}" + colors.RESET)
    
    print(colors.BLUE + "\n[+] Verificação de e-mail concluída!" + colors.RESET)

# Buscar redes sociais por nome
def search_social_media(name):
    print(colors.BLUE + f"\n[+] Buscando perfis de {name} em redes sociais..." + colors.RESET)
    
    # Simulação de busca (na prática, usaria APIs ou web scraping)
    social_networks = {
        "Facebook": f"https://www.facebook.com/{name.replace(' ', '.')}",
        "Twitter": f"https://twitter.com/{name.replace(' ', '')}",
        "Instagram": f"https://www.instagram.com/{name.replace(' ', '')}",
        "LinkedIn": f"https://www.linkedin.com/in/{name.replace(' ', '-')}",
        "YouTube": f"https://www.youtube.com/user/{name.replace(' ', '')}"
    }
    
    for network, url in social_networks.items():
        try:
            response = requests.head(url, allow_redirects=False, timeout=5)
            if response.status_code in [200, 301, 302]:
                print(colors.GREEN + f"[+] Possível perfil encontrado em {network}: {url}" + colors.RESET)
            else:
                print(colors.RED + f"[-] Perfil não encontrado em {network}" + colors.RESET)
        except:
            print(colors.YELLOW + f"[!] Erro ao verificar {network}" + colors.RESET)
    
    print(colors.BLUE + "\n[+] Busca em redes sociais concluída!" + colors.RESET)

# Verificar logins por nome de usuário
def check_username(username):
    print(colors.BLUE + f"\n[+] Verificando o nome de usuário '{username}' em vários sites..." + colors.RESET)
    
    # Sites para verificar (simulação)
    sites = {
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}"
    }
    
    for site, url in sites.items():
        try:
            response = requests.head(url, allow_redirects=False, timeout=5)
            if response.status_code in [200, 301, 302]:
                print(colors.GREEN + f"[+] Possível conta encontrada em {site}: {url}" + colors.RESET)
            else:
                print(colors.RED + f"[-] Conta não encontrada em {site}" + colors.RESET)
        except:
            print(colors.YELLOW + f"[!] Erro ao verificar {site}" + colors.RESET)
    
    print(colors.BLUE + "\n[+] Verificação de nome de usuário concluída!" + colors.RESET)

# Geolocalização por IP
def ip_geolocation(ip):
    print(colors.BLUE + f"\n[+] Buscando informações de geolocalização para o IP: {ip}..." + colors.RESET)
    
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        
        if data["status"] == "success":
            print(colors.GREEN + "[+] Informações encontradas:" + colors.RESET)
            print(f"País: {data['country']}")
            print(f"Região: {data['regionName']}")
            print(f"Cidade: {data['city']}")
            print(f"CEP: {data['zip']}")
            print(f"Latitude: {data['lat']}")
            print(f"Longitude: {data['lon']}")
            print(f"Provedor: {data['isp']}")
            print(f"Organização: {data['org']}")
            print(f"AS: {data['as']}")
        else:
            print(colors.RED + "[-] Não foi possível obter informações para este IP." + colors.RESET)
    except:
        print(colors.RED + "[-] Erro ao buscar informações de geolocalização." + colors.RESET)
    
    print(colors.BLUE + "\n[+] Busca de geolocalização concluída!" + colors.RESET)

# Simulação do Gabylfi (simplificado)
def gabyfi_lfi(url):
    print(colors.BLUE + f"\n[+] Analisando URL para possíveis vulnerabilidades LFI: {url}" + colors.RESET)
    
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    
    # Padrões comuns de LFI
    lfi_patterns = [
        "/../../../../etc/passwd",
        "/..%2F..%2F..%2F..%2Fetc%2Fpasswd",
        "/?page=../../../../etc/passwd",
        "/index.php?page=../../../../etc/passwd",
        "/include.php?file=../../../../etc/passwd"
    ]
    
    vulnerable = False
    
    for pattern in lfi_patterns:
        test_url = base_url + pattern
        try:
            response = requests.get(test_url, timeout=5)
            if "root:" in response.text:
                print(colors.RED + f"[!] POSSÍVEL VULNERABILIDADE LFI ENCONTRADA: {test_url}" + colors.RESET)
                print(colors.YELLOW + "[*] Dados recuperados (exemplo):" + colors.RESET)
                print(response.text[:500] + "...")  # Mostra apenas parte do conteúdo
                vulnerable = True
                break
        except:
            continue
    
    if not vulnerable:
        print(colors.GREEN + "[+] Nenhuma vulnerabilidade LFI óbvia encontrada." + colors.RESET)
    
    print(colors.BLUE + "\n[+] Análise LFI concluída!" + colors.RESET)

# Menu principal
def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    banner()
    
    while True:
        try:
            option = input(colors.MAGENTA + "\n[?] Selecione uma opção (1-6): " + colors.RESET)
            
            if option == "1":
                email = input(colors.CYAN + "[?] Digite o e-mail para verificar: " + colors.RESET)
                if "@" in email and "." in email.split("@")[1]:
                    check_email(email)
                else:
                    print(colors.RED + "[!] E-mail inválido!" + colors.RESET)
            
            elif option == "2":
                name = input(colors.CYAN + "[?] Digite o nome completo para buscar: " + colors.RESET)
                if len(name) > 3:
                    search_social_media(name)
                else:
                    print(colors.RED + "[!] Nome muito curto!" + colors.RESET)
            
            elif option == "3":
                username = input(colors.CYAN + "[?] Digite o nome de usuário para verificar: " + colors.RESET)
                if len(username) > 2:
                    check_username(username)
                else:
                    print(colors.RED + "[!] Nome de usuário muito curto!" + colors.RESET)
            
            elif option == "4":
                ip = input(colors.CYAN + "[?] Digite o IP para geolocalização: " + colors.RESET)
                if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ip):
                    ip_geolocation(ip)
                else:
                    print(colors.RED + "[!] Formato de IP inválido!" + colors.RESET)
            
            elif option == "5":
                url = input(colors.CYAN + "[?] Digite a URL para verificar (ex: http://exemplo.com): " + colors.RESET)
                if url.startswith(('http://', 'https://')):
                    gabyfi_lfi(url)
                else:
                    print(colors.RED + "[!] URL deve começar com http:// ou https://" + colors.RESET)
            
            elif option == "6":
                print(colors.GREEN + "\n[+] Saindo da ferramenta..." + colors.RESET)
                break
            
            else:
                print(colors.RED + "[!] Opção inválida! Escolha de 1 a 6." + colors.RESET)
        
        except KeyboardInterrupt:
            print(colors.RED + "\n[!] Operação cancelada pelo usuário." + colors.RESET)
            break
        except Exception as e:
            print(colors.RED + f"[!] Ocorreu um erro: {str(e)}" + colors.RESET)

if __name__ == "__main__":
    # Verificar se o requests está instalado
    try:
        import requests
    except ImportError:
        print(colors.RED + "[!] A biblioteca 'requests' não está instalada." + colors.RESET)
        print(colors.YELLOW + "[*] Instale com: pip install requests" + colors.RESET)
        sys.exit(1)
    
    main()
