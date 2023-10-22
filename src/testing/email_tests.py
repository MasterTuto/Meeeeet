from .secrets import imap_email, imap_passwd

from emaillib.email import Email

from .logger import Logger

def test_imap_login():
    mail = Email()
    imap = mail.log_in(imap_email, imap_passwd)

    Logger.success("Log in feito com sucesso!")

    return imap

def test_imap_list_email(imap):
    emails = imap.get_emails()
    
    input("Me envie um email e aperte enteder para verificar")

    assert emails != imap.get_emails(), Logger.err("Email nao identificado!")

    Logger.success("Listagem de emails lida com sucesso")

def test_read_email(imap):
    emails = imap.get_emails()

    assert isinstance(emails[0].title, str) and len(emails[0].title) > 0, Logger.err("Leitura de e-mail com insucesso!")

    Logger.success("Leitura e e-mails com êxito!")


def test_get_link(imap):
    emails = imap.get_emails()

    last_email = emails[0]

    assert (last_email.is_meet_invitation and len(last_email.get_reunion_id) == 12) or \
           (not last_email.is_meet_invitation and len(last_email.get_reunion_id) == 0), \
           Logger.err("Nao foi possivel obter link de e-mail")
        
    Logger.success("Codigo da reuniao obtido com sucesso!")

def begin():
    pass
