"""!wd <action list/find> <subject deliveries/delivery> <criteria code/id for find, active/cancelled for list> will pull u info on wumdrop stored records """
import re
from urllib import quote
import requests

def ask_wumdrop(query):
    
    return ":crying_cat_face: Sorry, WumDrop doesn't have an answer for you :crying_cat_face:"

    return answer

def on_message(msg, server):
    text = msg.get("text", "")
    match = re.findall(r"!calc (.*)", text)
    if not match: return

    return calc(match[0])
