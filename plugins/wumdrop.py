"""!wd <action list/find> <subject deliveries/delivery> <criteria code/id for find, active/cancelled for list> will pull u info on wumdrop stored records """
import re
from urllib import quote
import requests

base_url = 'https://wumdrop.appspot.com/slack/do'
def send_request(message):
    argstr = quote(message)
    result = requests.get(base_url+'?text='+argstr)
    return result

def ask_wumdrop(query):
    result = send_request(query)
    if result.status_code != requests.codes.ok:
        return ":crying_cat_face: Sorry, WumDrop doesn't have an answer for you :crying_cat_face:"
    return result.text

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!wd (.*)", text)
    if not match: return

    return ask_wumdrop(match[0])
