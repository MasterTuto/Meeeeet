from .logger import Logger
from .secrets import email, passwd

import browser.browser_manager as browser_manager    

def test_firefox():
    try:
        browser = browser_manager.Browser('firefox')
        browser.quit()
        Logger.success('Teste de navegador Firefox com exito.')
    except Exception as e:
        print('Nao foi possivel criar instancia de navegador pelo Firefox')

def test_chrome():
    try:
        browser = browser_manager.Browser('chrome')
        browser.quit()
        Logger.success('Teste de navegador Chrome com exito.')
    except Exception as e:
        print('Nao foi possivel criar instancia de navegador pelo Chrome')

def test_edge():
    try:
        browser = browser_manager.Browser('edge')
        browser.quit()
        Logger.success('Teste de navegador Edge com exito.')
    except Exception as e:
        print('Nao foi possivel criar instancia de navegador pelo Edge')

def test_firefox_headless():
    try:
        browser = browser_manager.Browser('firefox', True)
        browser.quit()
        Logger.success('Teste de navegador Firefox Headless com exito.')
    except Exception as e:
        print('Nao foi possivel criar instancia de navegador pelo Firefox')

def test_chrome_headless():
    try:
        browser = browser_manager.Browser('chrome', True)
        browser.quit()
        Logger.success('Teste de navegador Chrome Headless com exito.')
    except Exception as e:
        print('Nao foi possivel criar instancia de navegador pelo Chrome')

def test_edge_headless():
    try:
        browser = browser_manager.Browser('edge', True)
        browser.quit()
        Logger.success('Teste de navegador Edge Headless com exito.')
    except Exception as e:
        Logger.err('Nao foi possivel criar instancia de navegador pelo Edge')


def test_login(browser):
    browser.log_in(email, passwd)

    Logger.success("Log in feito com sucesso")

def test_navigation(browser, meet_id):
    browser.access_reunion(meet_id)

    assert browser.get_title == f"Meet: {meet_id}", Logger.get_err("Nao foi possivel acessar o website")

    Logger.success("Navegacao com sucesso")

def test_read_message(browser, right_message):
    message = browser.wait_until_message()

    assert message == right_message, Logger.get_err("Nao li a mensagem correta")

    print("Leu mensagem sem existo!")

def test_read_command(browser, is_command):
    message = browser.wait_until_command()

    assert message.is_command and is_command, Logger.get_err("[Nao] comando interpretado errado!")

    print("Teste de comando com exito")

def test_change_input_device(browser):
    browser.set_device_to_ab_audio()

    print("Teste de comando com exito!")


def begin():
    browser = browser_manager.Browser('firefox')

