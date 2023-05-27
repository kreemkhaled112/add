from customtkinter import *
from tkinter import *
from tkinter import ttk
from selenium import webdriver
import undetected_chromedriver as uc
from undetected_chromedriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import  os, msvcrt,re
from random import *
from time import sleep
from threading import Thread
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.window import WindowTypes
from pystyle import *

def facebook(type):
        for _ in range(10):
                with open('Frist_name.txt', 'r', encoding='utf-8') as f:
                        first = f.read().splitlines()
                        first = choice(first)

                with open('Last_name.txt', 'r', encoding='utf-8') as f:
                        last = f.read().splitlines()
                        last = choice(last)
                                                                        
                s = 2
                chrs = 'abcdefghijklmnopqrstuvwxyz'
                user = ''.join(choices(chrs, k=8))

                options = uc.ChromeOptions()
                options.add_argument("--disable-popup-blocking")
                options.add_argument("--disable-notifications")
                options.add_argument("--lang=en")
                options.add_argument("--start-maximized")
                bot = uc.Chrome(options=options,use_subprocess=True) 

                bot.get('https://moakt.com/ar')

                bot.maximize_window()


                button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/span[3]/input")))
                button.send_keys(user)
                sleep(s)
                
                button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/input[2]")))
                button.click()
                sleep(s)

                bot.execute_script("window.open()")

                bot.switch_to.window(bot.window_handles[-1])
                if type == '1' :

                        bot.get("https://www.facebook.com/")
                        sleep(2)
                        
                        try:
                                try:
                                        button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div/div/div[4]/button[2]")))
                                        button.click()
                                        sleep(s)
                                except:
                                        pass
                                button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a")))
                                button.click()
                                
                                
                        except:
                                Write.Input("[?] Prees Enter...... \n", Colors.cyan_to_blue, interval=0.0001)
                        try:
                                button1 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[1]/div/input")))
                                button1.send_keys(first)
                                sleep(s)

                                button2 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[2]/div/div[1]/input")))
                                button2.send_keys(last)
                                sleep(s)
                        except:
                                Write.Input("[?] Prees Enter...... \n", Colors.cyan_to_blue, interval=0.0001)
                        try:
                        
                                button2 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[2]/div/div[1]/input")))
                                button2.send_keys(f'{user}@teml.net')
                                sleep(s)
                                button2 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[3]/div/div/div[1]/input")))
                                button2.send_keys(f'{user}@teml.net')
                                sleep(s)
                        except:
                                Write.Input("[?] Prees Enter...... \n", Colors.cyan_to_blue, interval=0.0001)
                        button3 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[4]/div/div[1]/input")))
                        button3.send_keys("01278675268")
                        sleep(s)
                        try:
                        
                                button1 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[1]/option[11]")))
                                button1.click()
                                sleep(s)
                                button2 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[2]/option[11]")))
                                button2.click()
                                sleep(s)
                                button3 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[3]/option[23]")))
                                button3.click()
                                sleep(s)
                        except:
                                Write.Input("[?] Prees Enter...... \n", Colors.cyan_to_blue, interval=0.0001)
                        button3 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[1]/input")))
                        button3.click()
                        sleep(s)
                        button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[11]/button")))
                        button.click()
                        
                        sleep(10)
                        try:
                                button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[1]/div[1]/label/div/input")))

                                bot.switch_to.window(bot.window_handles[0])

                                sleep(15)

                                bot.refresh()
                                
                                soup = BeautifulSoup(bot.page_source, 'html.parser')

                                message_elements = soup.find_all('div', class_='email-messages modal')

                                # Extract and print the messages
                                for element in message_elements:
                                        message = element.get_text().strip()
                                        code_pattern = r'FB-(\d+)'
                                        matches = re.findall(code_pattern, message)


                                bot.switch_to.window(bot.window_handles[-1])
                                sleep(s)

                                button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[1]/div[1]/label/div/input")))
                                button.send_keys(matches[0])
                                sleep(s)

                                button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div[2]/form/div[2]/div/button")))
                                button.click()
                                sleep(5)

                                button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[2]/div/div/div/div[3]/div/a")))
                                button.click()
                                sleep(5)
                        
                                bot.quit()

                                with open('Account/facebook.txt', 'a') as f:
                                        f.write(f'{user}@teml.net\n')
                
                        except:
                                Write.Input("[?] Error...... \n", Colors.cyan_to_blue, interval=0.0001)
                                bot.quit()

                elif type == '2' :
                        bot.get("https://m.facebook.com/")
                        sleep(5)
                        
                        try:
                                
                                button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div[2]/a")))
                                button.click()
                                
                        except:
                                Write.Input("[?] Prees Enter...... \n", Colors.cyan_to_blue, interval=0.0001)
                        try:
                                button1 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div/form/div[3]/div[3]/div/div/div[1]/div[1]/div[2]/div/input")))
                                button1.send_keys(first)
                                sleep(s)

                                button2 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div/form/div[3]/div[3]/div/div/div[1]/div[2]/div[2]/div/input")))
                                button2.send_keys(last)
                                sleep(s)
                                
                                next = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div/form/div[9]/div[2]/button[1]")))
                                next.click()
                        
                        except:
                                Write.Input("[?] Prees Enter...... \n", Colors.cyan_to_blue, interval=0.0001)
                        try:
                        
                                button1 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div/div[3]/div[2]/div/form/div[4]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/select/option[11]")))
                                button1.click()
                                sleep(s)
                                button2 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[1]/div/div[3]/div[2]/div/form/div[4]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/select/option[11]")))
                                button2.click()
                                sleep(s)
                                button3 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div/form/div[4]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/select/option[23]")))
                                button3.click()
                                sleep(s)
                                next = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div/form/div[9]/div[2]/button[1]")))
                                next.click()
                        except:
                                Write.Input("[?] Prees Enter...... \n", Colors.cyan_to_blue, interval=0.0001)
                        try:
                                
                                button2 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div/form/div[11]/div/a[1]")))
                                button2.click()
                                sleep(s)
                                button2 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div/form/div[5]/div[3]/div/div/div[1]/div[3]/div/input")))
                                button2.send_keys(f'{user}@teml.net')
                                sleep(s)
                                next = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div/form/div[9]/div[2]/button[1]")))
                                next.click()
                        except:
                                Write.Input("[?] Prees Enter...... \n", Colors.cyan_to_blue, interval=0.0001)

                        button3 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div/form/div[6]/div[3]/div/div/div[3]/div/label[2]/div/div/div[2]/input")))
                        button3.click()
                        sleep(s)
                        next = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div/form/div[9]/div[2]/button[1]")))
                        next.click()
                        try:

                                button3 = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div/form/div[7]/div[3]/div/div/div[1]/div[2]/div/input")))
                                button3.send_keys("01278675268")
                                sleep(s)
                                sign = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div/form/div[9]/div[2]/button[4]")))
                                sign.click()
                                sleep(10)
                        except:
                                Write.Input("[?] Prees Enter...... \n", Colors.cyan_to_blue, interval=0.0001)
                        

                        button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/form/div/button")))
                        button.click()
                        
                        sleep(5)
                        try:
                                button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[1]/div[1]/div/div/div/form/div/input")))

                                bot.switch_to.window(bot.window_handles[0])

                                sleep(15)

                                bot.refresh()
                
                        except:
                                Write.Input("[?] Error...... \n", Colors.cyan_to_blue, interval=0.0001)

                        Write.Input("[?] Prees Enter...... \n", Colors.cyan_to_blue, interval=0.0001)

                        bot.quit()

                        with open('Account/facebook.txt', 'a') as f:
                                f.write(f'{user}@teml.net\n')
def start():

    txt = """
        ╔═╗ ╗   ┌─┐┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐
        ╔═╬═╝   │  ├─┤├┤ │  ├┴┐├┤ ├┬┘
        ╚ ╚═╝   └─┘┴ ┴└─┘└─┘┴ ┴└─┘┴└─
            Made with <3 by Tekky       

       + - - - - -                              
           [1]  Start
           [2]  Documentation     
                           - - - - - +
    """     
    num = Write.Input("[?] Choice : ", Colors.cyan_to_blue, interval=0.000000005, hide_cursor=True)
    Thread(target=facebook, args=(num)).start()
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system(f"title Kreem @ 2022 - Xcrazyxx")
    start()