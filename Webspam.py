from discord import Webhook, RequestsWebhookAdapter
import threading
from pystyle import Colorate, Colors
import os, sys, requests, json, random, time


def WebhookSend():
 url = input(Colorate.Horizontal(Colors.purple_to_blue, f"[$] [Crisis@User] -  Webhook URL: ",1))
 message = input(Colorate.Horizontal(Colors.purple_to_blue, f"[$] [Crisis@User] -  Message: ",1))
 os.system('cls')
 threading.Thread(target=WebhookSend).start()
 while True:
  webhook = Webhook.from_url(f"{url}", adapter=RequestsWebhookAdapter())
  webhook.send(f"{message}")
  print(Colorate.Horizontal(Colors.purple_to_blue, f"[$] [Crisis@User] -  Sent: {message}",1))

menu = """
 ██████╗██████╗ ██╗███████╗██╗███████╗
██╔════╝██╔══██╗██║██╔════╝██║██╔════╝
██║     ██████╔╝██║███████╗██║███████╗
██║     ██╔══██╗██║╚════██║██║╚════██║
╚██████╗██║  ██║██║███████║██║███████║
 ╚═════╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝╚══════╝

[01] Check Webhook           
[02] Webhook Info            
[03] Delete Webhook          
[04] Spam Webhook  
[05] Proxy Scraper
[06] Exit          
"""

# _____________________________________________________________________________________________________________________

def destroyer():
    os.system('cls && title Tower Spammer')
    print(Colorate.Horizontal(Colors.purple_to_blue, menu, 1))
    x = input("[?] Choice: ")
    if x == '1' or x == '01':
      hookcheck = input(Colorate.Horizontal(Colors.purple_to_blue, f'[$] [Crisis@User] -  Webhook Link: ',1))
      os.system('cls')
      r = requests.get(hookcheck)
      if r.status_code == 200:
        print(Colorate.Horizontal(Colors.green_to_blue, f"[$] [Crisis@User] -  Valid Webhook!",1))
        print(Colorate.Horizontal(Colors.purple_to_blue, f"[$] Press enter to come back to the menu",1))
        input()
        destroyer()
      else:
        print(Colorate.Horizontal(Colors.red_to_purple, f"[$] [Crisis@User] -  Valid Webhook!",1))
        print(Colorate.Horizontal(Colors.purple_to_blue, f"[$] Press enter to come back to the menu",1))
        input()
        destroyer()
    if x == '2' or x == '02':
      p = input(Colorate.Horizontal(Colors.purple_to_blue, f'[$] [Crisis@User] -  Webhook Link: ',1))
      r = requests.get(p)
      os.system('cls')
      print(Colorate.Horizontal(Colors.purple_to_blue, f'[$] [Crisis@User] -  Webhook Name: [{r.json()["name"]}]',1))
      print(Colorate.Horizontal(Colors.purple_to_blue, f'[$] [Crisis@User] -  Webhook ID: [{r.json()["id"]}]',1))
      print(Colorate.Horizontal(Colors.purple_to_blue, f'[$] [Crisis@User] -  Guild ID of Webhook: [{r.json()["guild_id"]}]',1))
      print(Colorate.Horizontal(Colors.purple_to_blue, f'[$] [Crisis@User] -  Channel ID of Webhook: [{r.json()["channel_id"]}]',1))
      if r.json()['avatar'] == 'null':
          print(Colorate.Horizontal(Colors.purple_to_blue, f'[$] [Crisis@User] -  Avatar: [Default]',1))
          print(Colorate.Horizontal(Colors.purple_to_blue, f"[$] Press enter to come back to the menu",1))
          input()
          destroyer()
      else:
          avatar = f'https://cdn.discordapp.com/avatars/{r.json()["id"]}/{r.json()["avatar"]}'
          print(Colorate.Horizontal(Colors.purple_to_blue, f'[$] [Crisis@User] -  Avatar: {avatar}',1))
      print(Colorate.Horizontal(Colors.purple_to_blue, f'[$] [Crisis@User] -  Token of Webhook: [{r.json()["token"]}]',1))
      print(Colorate.Horizontal(Colors.purple_to_blue, f"[$] [Crisis@User] -  Press enter to come back to the menu",1))
      input()
      destroyer()
    if x == '3' or x == '03':
      web = input(Colorate.Horizontal(Colors.purple_to_blue, f'[$] [Crisis@User] -  Webhook Link: ',1))
      os.system('cls')
      try:
        requests.delete(web)
        print(Colorate.Horizontal(Colors.purple_to_blue, f'[$] [Crisis@User] -  Webhook Deleted . . .',1))
      except:
        print(Colorate.Horizontal(Colors.purple_to_blue, f'[$] [Crisis@User] -  Failed to delete webhook . . .',1))
        time.sleep(1)
        destroyer()
    if x == '4' or x == '04':
        os.system('cls')
        WebhookSend()
    if x == '5' or x == '05':
        os.system('cls')
        print(Colorate.Horizontal(Colors.purple_to_blue, f"[$] [Crisis@User] -  Loading . . .",1))
        time.sleep(2)
        exec(open('proxy.py').read())
    if x == '6' or x == '06':
        os.system('cls')
        print(Colorate.Horizontal(Colors.purple_to_blue, f"[$] [Crisis@User] -  Exiting you shortly . . .",1))
        time.sleep(4)
        sys.exit()
destroyer()