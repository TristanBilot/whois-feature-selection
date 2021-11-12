import requests
import re
import socket
import pandas as pd

from pythonwhois import get_whois
from preprocess import load_dataset

def get_ip_history(domain):
    req = requests.get("https://securitytrails.com/domain/" + domain + "/history/a")
    source = str(req.content)
    ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', source)
    unique_list = list(set(ip))
    sorted_ip = sorted(unique_list, key=lambda item: socket.inet_aton(item[0]))
    return sorted_ip

def parse_whois(domain):
    def parse_status(whois):
        parsed = [str(status).split(' ')[0] for status in whois['status']]
        whois['status'] = parsed
        return whois

    whois = get_whois(domain)
    whois = parse_status(whois)
    del whois['raw']
    return whois


if __name__ == '__main__':
    domain = 'mp3raids.xyz'
    # whois = parse_whois(domain)
    # hisory = get_ip_history(domain)

    # pprint(whois)
    # print(hisory)
    df = load_dataset()
