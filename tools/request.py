import requests
import sys
import socket
import json
from pygments import highlight, lexers, formatters

def requesturl(i):
    url = requests.get("https://ipinfo.io/"+ i +"?token=4be917bcc42304")
    r = url.text

    # code to colour
    obj = json.loads(r)
    json_formatted_str = json.dumps(obj, indent=4)
    # colourful output
    colorful_json = highlight(json_formatted_str, lexers.JsonLexer(), formatters.TerminalFormatter())

    print(colorful_json)


def get_ip_address(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror:
        return None


def viewdns(i):
    url = requests.get(f"https://api.viewdns.info/reverseip/?host={i}&apikey=5b9f9f764c245bd510d9755a5990ecaf5299ae2b&output=json")
    r = str(url.text)
    obj = json.loads(r)
    json_formatted_str = json.dumps(obj, indent=4)
    # colourful output
    colorful_json = highlight(json_formatted_str, lexers.JsonLexer(), formatters.TerminalFormatter())

    print(colorful_json)

jd = viewdns(sys.argv[1])








ip = get_ip_address(sys.argv[1])

requesturl(ip)
