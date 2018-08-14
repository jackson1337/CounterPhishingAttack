import random
import string

def _prepare_names(file_name):
    with open(file_name) as f:
        list_of_names = f.readlines()

    
    final = [name.lower().strip() for name in list(filter(lambda x: len(x)>2, list_of_names))]

    random.shuffle(final)

    return final

def _prepare_suffixes():
    with open("mails.txt") as mails:
        list_of_mails = mails.readlines()
    
    return [mail.strip() for mail in list(filter(lambda x: len(x)>2,list_of_mails))]


def _get_emails(file_name):
    list_of_suffixes = _prepare_suffixes()
    return [name+str(random.randint(1,20) * 15)+'@'+random.choice(list_of_suffixes) for name in _prepare_names(file_name)]

def get_emails_and_passwords_tuple(file_name):
    tpl = [(mail,_random_string()) for mail in _get_emails(file_name)]
    return tpl



def _random_string():
    return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase+string.digits) for _ in range(random.randint(6,15)))




