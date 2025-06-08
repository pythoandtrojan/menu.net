import re
import requests
from bs4 import BeautifulSoup
import json
import sqlite3
from datetime import datetime

class SistemaBusca:
    def __init__(self):
        self.conn = sqlite3.connect('dados_busca.db')
        self.criar_tabelas()
        
    def criar_tabelas(self):
        cursor = self.conn.cursor()
        
        # Tabela para armazenar resultados de IP
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS ip_busca (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT NOT NULL,
            cidade TEXT,
            pais TEXT,
            provedor TEXT,
            data_busca TIMESTAMP
        )
        ''')
        
        # Tabela para armazenar resultados de e-mails
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS email_busca (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            usuario TEXT,
            dominio TEXT,
            links TEXT,  # JSON com lista de URLs onde foi encontrado
            data_busca TIMESTAMP
        )
        ''')
        
        # Tabela para armazenar resultados de usuários
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuario_busca (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            plataformas TEXT,  # JSON com plataformas onde foi encontrado
            links TEXT,        # JSON com links associados
            data_busca TIMESTAMP
        )
        ''')
        
        self.conn.commit()

    # --- Busca por IP ---
    def buscar_ip(self, ip):
        try:
            # Simulação de API de geolocalização por IP
            url = f"http://ip-api.com/json/{ip}"
            response = requests.get(url)
            dados = response.json()
            
            if dados['status'] == 'success':
                # Armazenar no banco de dados
                cursor = self.conn.cursor()
                cursor.execute('''
                INSERT INTO ip_busca (ip, cidade, pais, provedor, data_busca)
                VALUES (?, ?, ?, ?, ?)
                ''', (ip, dados.get('city'), dados.get('country'), dados.get('isp'), datetime.now()))
                self.conn.commit()
                
                return {
                    'ip': ip,
                    'cidade': dados.get('city'),
                    'pais': dados.get('country'),
                    'provedor': dados.get('isp'),
                    'latitude': dados.get('lat'),
                    'longitude': dados.get('lon')
                }
            return None
        except Exception as e:
            print(f"Erro na busca por IP: {e}")
            return None

    # --- Busca por E-mail (holehe) ---
    def buscar_email(self, email):
        try:
            # Simulação de verificação em plataformas (holehe-like)
            plataformas_conhecidas = {
                'gmail.com': ['google', 'youtube', 'drive'],
                'outlook.com': ['microsoft', 'office', 'linkedin'],
                'yahoo.com': ['flickr', 'tumblr']
            }
            
            dominio = email.split('@')[-1]
            plataformas = plataformas_conhecidas.get(dominio, [])
            
            # Simular busca por vazamentos (usando haveibeenpwned API)
            url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
            headers = {'User-Agent': 'Python-SistemaBusca'}
            response = requests.get(url, headers=headers)
            
            vazamentos = []
            if response.status_code == 200:
                vazamentos = [v['Name'] for v in response.json()]
            
            # Armazenar no banco de dados
            cursor = self.conn.cursor()
            cursor.execute('''
            INSERT INTO email_busca (email, usuario, dominio, links, data_busca)
            VALUES (?, ?, ?, ?, ?)
            ''', (email, email.split('@')[0], dominio, json.dumps(plataformas + vazamentos), datetime.now()))
            self.conn.commit()
            
            return {
                'email': email,
                'usuario': email.split('@')[0],
                'dominio': dominio,
                'plataformas': plataformas,
                'vazamentos': vazamentos
            }
        except Exception as e:
            print(f"Erro na busca por e-mail: {e}")
            return None

    # --- Busca por Usuário (gabyfi-like) ---
    def buscar_usuario(self, usuario):
        try:
            # Simular busca em redes sociais
            redes_sociais = {
                'twitter': f"https://twitter.com/{usuario}",
                'instagram': f"https://instagram.com/{usuario}",
                'github': f"https://github.com/{usuario}"
            }
            
            resultados = {}
            for rede, url in redes_sociais.items():
                response = requests.get(url)
                if response.status_code == 200:
                    resultados[rede] = url
            
            # Armazenar no banco de dados
            cursor = self.conn.cursor()
            cursor.execute('''
            INSERT INTO usuario_busca (usuario, plataformas, links, data_busca)
            VALUES (?, ?, ?, ?)
            ''', (usuario, json.dumps(list(resultados.keys())), json.dumps(list(resultados.values())), datetime.now()))
            self.conn.commit()
            
            return {
                'usuario': usuario,
                'plataformas': list(resultados.keys()),
                'links': list(resultados.values())
            }
        except Exception as e:
            print(f"Erro na busca por usuário: {e}")
            return None

    # --- Função para gerar URLs (gabyfi) ---
    def gerar_urls(self, usuario):
        templates = {
            'Twitter': f'https://twitter.com/{usuario}',
            'Instagram': f'https://instagram.com/{usuario}',
            'GitHub': f'https://github.com/{usuario}',
            'Facebook': f'https://facebook.com/{usuario}',
            'LinkedIn': f'https://linkedin.com/in/{usuario}'
        }
        return templates

    # --- Fechar conexão ---
    def __del__(self):
        self.conn.close()

# Exemplo de uso
if __name__ == "__main__":
    sistema = SistemaBusca()
    
    # Busca por IP
    print("\nBusca por IP:")
    resultado_ip = sistema.buscar_ip("8.8.8.8")
    print(resultado_ip)
    
    # Busca por e-mail
    print("\nBusca por e-mail:")
    resultado_email = sistema.buscar_email("exemplo@gmail.com")
    print(resultado_email)
    
    # Busca por usuário
    print("\nBusca por usuário:")
    resultado_usuario = sistema.buscar_usuario("exemplo")
    print(resultado_usuario)
    
    # Gerar URLs
    print("\nGerar URLs:")
    urls = sistema.gerar_urls("exemplo")
    for plataforma, url in urls.items():
        print(f"{plataforma}: {url}")
