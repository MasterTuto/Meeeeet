from tests.logger import Logger
from tests.secrets import email, passwd

import browser.browser_manager as browser_manager    

def test_firefox(self):
    try:
        browser_manager.Browser('firefox')
    except Exception as e:
        print('Nao foi possivel criar instancia de navegador pelo Firefox')

def test_chrome(self):
    try:
        browser_manager.Browser('chrome')
    except Exception as e:
        print('Nao foi possivel criar instancia de navegador pelo Chrome')

def test_edge(self):
    try:
        browser_manager.Browser('edge')
    except Exception as e:
        print('Nao foi possivel criar instancia de navegador pelo Edge')

def test_firefox_headless(self):
    try:
        browser_manager.Browser('firefox', True)
    except Exception as e:
        print('Nao foi possivel criar instancia de navegador pelo Firefox')

def test_chrome_headless(self):
    try:
        browser_manager.Browser('chrome', True)
    except Exception as e:
        print('Nao foi possivel criar instancia de navegador pelo Chrome')

def test_edge_headless(self):
    try:
        browser_manager.Browser('edge', True)
    except Exception as e:
        print('Nao foi possivel criar instancia de navegador pelo Edge')

def test_login(self, meet_id):
    browser = browser_manager.Browser('firefox')

    browser.log_in(email, passwd)
    browser.access_reunion(meet_id)

    assert browser.get_title == f"Meet: {meet_id}", "[!] Nao foi possivel acessar o website"

    print("[*] Log in feito com sucesso")