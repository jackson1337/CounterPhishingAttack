import sys
from you_came_to_the_wrong_neighborhood import get_emails_and_passwords_tuple
from request_handler import send_request

filename="names.txt"

try:
    url = sys.argv[1]
except IndexError as idx:
    print("You have to provide a target for your weapon!")
    sys.exit(1)

tpl = get_emails_and_passwords_tuple(filename)

for item in tpl:
    send_request(item, url)

