from customtkinter import *
from tkinter import *
from tkinter import ttk
from selenium import webdriver
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import  os, msvcrt
from random import *
from time import sleep
from threading import Thread
import threading
from selenium.webdriver.common.window import WindowTypes
from pystyle import *



def Two(s,chrs):
        user = ''.join(choices(chrs, k=6))
        with open('name.txt', 'r') as f:
                name = f.read().splitlines()
        S = 2
        bot = uc.Chrome()


        bot.get("https://outlook.live.com/owa/")

        button1 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div/section/div/div[2]/a/span")))
        button1.click()

        button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[1]/fieldset/div[1]/div[3]/div[2]/div/input")))
        button.send_keys(user)
        next = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[1]/div[2]/div/div/div/div[3]/input")))
        next.click()
        sleep(s)

        button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[3]/div/input[2]")))
        button.send_keys("01278675268k")
        next = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[7]/div/div/div[2]/input")))
        next.click()
        sleep(s)

        button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[1]/div[3]/div[1]/input")))
        button.send_keys(choice(name))
        sleep(s)
        button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[1]/div[3]/div[2]/input")))
        button.send_keys(choice(name))

        next = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[2]/div/div/div[2]/input")))
        next.click()
        sleep(s)

        button1 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[4]/div[3]/div[1]/select/option[{randrange(1,12)}]")))
        button1.click()
        sleep(s)
        button2 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[4]/div[3]/div[2]/select/option[{randrange(1,31)}]")))
        button2.click()
        sleep(s)
        button3 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[4]/div[3]/div[3]/input")))
        button3.send_keys("2001")
        sleep(s)
        next = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[7]/div/div/div[2]/input")))
        next.click()
        Write.Print(f"          [?] User : {user} \n", Colors.cyan_to_blue, interval=0.0001)
        Write.Input("          [?] Prees Enter...... \n", Colors.cyan_to_blue, interval=0.0001)
        with open('Account/outlook.txt', 'a') as f:
                f.write(f'{user}\n')

        bot.switch_to.new_window(WindowTypes.TAB)


        bot.switch_to.window(bot.window_handles[1])

        bot.get("https://www.facebook.com/")

        button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a")))
        button.click()

        button1 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[1]/div/input")))
        button1.send_keys(choice(name))
        sleep(s)
        button2 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[2]/div/div[1]/input")))
        button2.send_keys(choice(name))
        sleep(s)
        button2 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[2]/div/div[1]/input")))
        button2.send_keys(f'{user}@outlook.com')
        sleep(s)
        button2 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[3]/div/div/div[1]/input")))
        button2.send_keys(f'{user}@outlook.com')
        sleep(s)
        button3 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[4]/div/div[1]/input")))
        button3.send_keys("01278675268")
        sleep(s)
        button1 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[1]/option[{randrange(1,30)}]")))
        button1.click()
        sleep(s)
        button2 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[2]/option[{randrange(1,12)}]")))
        button2.click()
        sleep(s)
        button3 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[3]/option[23]")))
        button3.click()
        sleep(s)

        button3 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/input")))
        button3.click()
        sleep(s)
        button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[11]/button")))
        button.click()

        Write.Input("          [?] Prees Enter...... \n", Colors.cyan_to_blue, interval=0.0001)

        with open('Account/facebook.txt', 'a') as f:
                f.write(f'{user}@outlook.com\n')
def outlook(s,chrs):
        
        user = ''.join(choices(chrs, k=7))
        with open('name.txt', 'r') as f:
                name = f.read().splitlines()

        bot = uc.Chrome()

        try:
                bot.get("https://outlook.live.com/owa/")

                button1 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div/section/div/div[2]/a/span")))
                button1.click()

                button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[1]/fieldset/div[1]/div[3]/div[2]/div/input")))
                button.send_keys(user)
                next = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[1]/div[2]/div/div/div/div[3]/input")))
                next.click()
                sleep(s)

                button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[3]/div/input[2]")))
                button.send_keys("01278675268k")
                next = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[7]/div/div/div[2]/input")))
                next.click()
                sleep(s)

                button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[1]/div[3]/div[1]/input")))
                button.send_keys(choice(name))
                sleep(s)
                button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[1]/div[3]/div[2]/input")))
                button.send_keys(choice(name))

                next = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[2]/div/div/div[2]/input")))
                next.click()
                sleep(s)

                button1 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[4]/div[3]/div[1]/select/option[{randrange(1,12)}]")))
                button1.click()
                sleep(s)
                button2 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[4]/div[3]/div[2]/select/option[{randrange(1,31)}]")))
                button2.click()
                sleep(s)
                button3 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[4]/div[3]/div[3]/input")))
                button3.send_keys("2001")
                sleep(s)
                next = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[7]/div/div/div[2]/input")))
                next.click()
                Write.Print(f"          [?] User : {user} \n", Colors.cyan_to_blue, interval=0.0001)
                Write.Input("          [?] Prees Enter...... \n", Colors.cyan_to_blue, interval=0.0001)
                with open('Account/outlook.txt', 'a') as f:
                        f.write(f'{user}\n')  
        except Exception as s:
               input(f"{s}")
def facebook(s,user):
        
        with open('name.txt', 'r') as f:
                name = f.read().splitlines()

        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        bot = webdriver.Chrome(options=options)

        bot.get("https://www.facebook.com/")

        button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a")))
        button.click()

        button1 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[1]/div/input")))
        button1.send_keys(choice(name))
        sleep(s)
        button2 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[2]/div/div[1]/input")))
        button2.send_keys(choice(name))
        sleep(s)
        button2 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[2]/div/div[1]/input")))
        button2.send_keys(f'{user}')
        sleep(s)
        button2 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[3]/div/div/div[1]/input")))
        button2.send_keys(f'{user}')
        sleep(s)
        button3 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[4]/div/div[1]/input")))
        button3.send_keys("01278675268")
        sleep(s)
        button1 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[1]/option[{randrange(1,30)}]")))
        button1.click()
        sleep(s)
        button2 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[2]/option[{randrange(1,12)}]")))
        button2.click()
        sleep(s)
        button3 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[3]/option[23]")))
        button3.click()
        sleep(s)

        button3 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/input")))
        button3.click()
        sleep(s)
        button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[11]/button")))
        button.click()

        Write.Input("          [?] Prees Enter...... \n", Colors.cyan_to_blue, interval=0.0001)

        with open('Account/facebook.txt', 'a') as f:
                f.write(f'{user}@outlook.com\n')
def start():

    txt = """
        ╔═╗ ╗   ┌─┐┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐
        ╔═╬═╝   │  ├─┤├┤ │  ├┴┐├┤ ├┬┘
        ╚ ╚═╝   └─┘┴ ┴└─┘└─┘┴ ┴└─┘┴└─
            Made with <3 by Kreem       

       + - - - - -                              
           [1]  Outlook + Facebook
           [2]  Outlook
           [3]  Facebook  
                           - - - - - +
    """
    print(Colorate.DiagonalBackwards(Colors.cyan_to_blue, Center.XCenter(txt), 1))
    print('\n')

    Choice = int(Write.Input("          [?] Choice : ", Colors.cyan_to_blue, interval=0.0001))
    
    input_char = Choice

    if input_char == 1:
        chrs = 'abcdefghijklmnopqrstuvwxyz'
        s = 2
        Thread(target=Two, args=(s,chrs)).start()

    elif input_char == 2:
        chrs = 'abcdefghijklmnopqrstuvwxyz'
        s = 2
        Thread(target=outlook, args=(s,chrs)).start()

    elif input_char == 3:
        chrs = 'abcdefghijklmnopqrstuvwxyz'
        user = ''.join(choices(chrs, k=7))
        Write.Print(f"         [?] {user} \n", Colors.cyan_to_blue, interval=0.0001)
        Write.Print("          [?] Email ↓\n", Colors.cyan_to_blue, interval=0.0001)
        user = Write.Input("           >  ", Colors.cyan_to_blue, interval=0.000000005, hide_cursor=True)
        s = 2
        Thread(target=facebook, args=(s,user)).start()


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system(f"title Kreem @ 2022 - Xcrazyxx")
    start()