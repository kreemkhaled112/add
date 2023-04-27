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
import  pyautogui,random,schedule,requests
from time import sleep
from threading import Thread
import threading

class AMFBot:
    def __init__(self,crazy):
        self.crazy = crazy
        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")
        self.crazy.geometry('400x400+500+150')
        self.crazy.resizable(True,True)
        self.crazy.minsize(400,400)
        self.crazy.maxsize(400,400)
        #self.crazy.maxsize(1680,1050)
        self.crazy.title("                        Crazy")
        
        self.n = 0
        self.stop = threading.Event()
        self.is_running = False
        self.check_list = []
        self.dlay = random.randrange(15,20)
        self.api_token = '6286940046:AAFrut4rAMEfmcAdRTwPZpe0OHMidgeC9Qw'
        self.chat_id = '1733472658'
        Bot = "Bot70!"
        self.text = f'Bypass CloudFlare successfully, {Bot}'
        self.text1 = f'Bypass CloudFlare Faild, {Bot}'
        self.text2 = f' Error, {Bot}'
        self.text3 = f' Faild No.screens, {Bot}'
        self.Facebook_text = f'Facebook Problem, {Bot}'
        self.Insta_text = f'Insta Problem, {Bot}'
        self.Twitter_text = f'Twitter problem, {Bot}'
        
        self.Facebook_Page = IntVar()
        self.Facebook_Post = IntVar()
        self.Facebook_Share = IntVar()
        self.Twiter_Follower = IntVar()
        self.Twiter_Retweet = IntVar()
        self.Twiter_Like = IntVar()
        self.Insta_Follower = IntVar()
        self.Insta_Like = IntVar()
        self.Youtube_Subscribe = IntVar()
        self.Youtube_Like = IntVar()
        self.Pinterest_Follower = IntVar()
        self.Pinterest_Save = IntVar()
        self.Soundcloud_Follower = IntVar()
        self.Soundcloud_Like = IntVar()
        self.Reddit_Members = IntVar()
        self.Reddit_Upvote = IntVar()
        self.Tiktok_Follower = IntVar()
        self.Tiktok_Like = IntVar()
        
        self.CheckBox = CTkCheckBox(self.crazy, text="Facebook Post", variable=self.Facebook_Post)
        self.CheckBox.place(x=10,y=10)
        self.CheckBox.select()
        self.CheckBox = CTkCheckBox(self.crazy, text="Facebook Page", variable=self.Facebook_Page)
        self.CheckBox.place(x=150,y=10)
        
        self.CheckBox = CTkCheckBox(self.crazy, text="Facebook Share", variable=self.Facebook_Share)
        self.CheckBox.place(x=275,y=10)
        self.CheckBox.select()
        
        self.CheckBox = CTkCheckBox(self.crazy, text="Twiter Follower", variable=self.Twiter_Follower)
        self.CheckBox.place(x=10,y=50)
        self.CheckBox.select()
        self.CheckBox = CTkCheckBox(self.crazy, text="Twiter Retweet", variable=self.Twiter_Retweet)
        self.CheckBox.place(x=150,y=50)
        self.CheckBox.select()
        self.CheckBox = CTkCheckBox(self.crazy, text="Twiter Like", variable=self.Twiter_Like)
        self.CheckBox.place(x=275,y=50)
        self.CheckBox.select()
        
        self.CheckBox = CTkCheckBox(self.crazy, text="Insta Follower", variable=self.Insta_Follower)
        self.CheckBox.place(x=10,y=90)
        self.CheckBox.select()
        self.CheckBox = CTkCheckBox(self.crazy, text="Insta Like", variable=self.Insta_Like)
        self.CheckBox.place(x=150,y=90)
        self.CheckBox.select()

        self.CheckBox = CTkCheckBox(self.crazy, text="Youtube Subscribe", variable=self.Youtube_Subscribe)
        self.CheckBox.place(x=10,y=130)
        
        self.CheckBox = CTkCheckBox(self.crazy, text="Youtube Like", variable=self.Youtube_Like)
        self.CheckBox.place(x=150,y=130)
        

        self.CheckBox = CTkCheckBox(self.crazy, text="Pinterest Follower", variable=self.Pinterest_Follower)
        self.CheckBox.place(x=10,y=170)
        
        self.CheckBox = CTkCheckBox(self.crazy, text="Pinterest Save", variable=self.Pinterest_Save)
        self.CheckBox.place(x=150,y=170)
        self.CheckBox.select()

        self.CheckBox = CTkCheckBox(self.crazy, text="Soundcloud Follow", variable=self.Soundcloud_Follower)
        self.CheckBox.place(x=10,y=210)
        self.CheckBox = CTkCheckBox(self.crazy, text="Soundcloud Like", variable=self.Soundcloud_Like)
        self.CheckBox.place(x=150,y=210)

        self.CheckBox = CTkCheckBox(self.crazy, text="Reddit Members", variable=self.Reddit_Members)
        self.CheckBox.place(x=10,y=250)
        self.CheckBox = CTkCheckBox(self.crazy, text="Reddit Upvote", variable=self.Reddit_Upvote)
        self.CheckBox.place(x=150,y=250)
        
        self.CheckBox = CTkCheckBox(self.crazy, text="Tiktok Follower", variable=self.Tiktok_Follower)
        self.CheckBox.place(x=10,y=290)
        self.CheckBox = CTkCheckBox(self.crazy, text="Tiktok Like", variable=self.Tiktok_Like)
        self.CheckBox.place(x=150,y=290)

        

        self.Open = CTkButton(self.crazy, text="Open",width=100,state="disabled",command=lambda: threading.Thread(target=self.open).start())
        self.Open.place(x=10,y=350)

        self.Start = CTkButton(self.crazy, text="Start",width=100,state="disabled",hover=False,command=lambda: threading.Thread(target=self.checkbox_state).start())
        self.Start.place(x=145,y=350)

        self.Close = CTkButton(self.crazy, text="Close",width=100,state="disabled",command=lambda: threading.Thread(target=self.close).start())
        self.Close.place(x=280,y=350)

        self.radio_var = IntVar()
        
        self.radio1 = CTkRadioButton(self.crazy, text="Android",height=28,command=lambda: self.Open.configure(state="normal"),
                                              variable= self.radio_var, value=1)
        self.radio1.place(x=290,y=250)

        self.radio2 = CTkRadioButton(self.crazy, text="Laptop",height=28,command=lambda: self.Open.configure(state="normal"),
                                              variable= self.radio_var, value=2)
        self.radio2.place(x=290,y=290)
            
    def checkbox_state(self):
        if not self.is_running:
            self.Start.configure(text="Stop")
            self.Start.configure(fg_color='#9b111e')
            
            self.check_list = []

            if self.Facebook_Page.get():
                self.check_list.append("Facebook Page")
            if self.Facebook_Post.get():
                self.check_list.append("Facebook Post")
            if self.Facebook_Share.get() :
                self.check_list.append("Facebook Share")
            if self.Twiter_Follower.get() :
                self.check_list.append("Twiter Follower")
            if self.Twiter_Retweet.get() :
                self.check_list.append("Twiter Retweet")
            if self.Twiter_Like.get() :
                self.check_list.append("Twiter Like")
            if self.Insta_Follower.get() :
                self.check_list.append("Insta Follower")
            if self.Insta_Like.get() :
                self.check_list.append("Insta Like")
            if self.Youtube_Subscribe.get() :
                self.check_list.append("Youtube Subscribe")
            if self.Youtube_Like.get() :
                self.check_list.append("Youtube Like")
            if self.Pinterest_Follower.get() :
                self.check_list.append("Pinterest Follower")
            if self.Pinterest_Save.get() :
                self.check_list.append("Pinterest Save")
            if self.Soundcloud_Follower.get() :
                self.check_list.append("Soundcloud Follow")
            if self.Soundcloud_Like.get() :
                self.check_list.append("Soundcloud Like")
            if self.Reddit_Members.get() :
                self.check_list.append("Reddit Members")
            if self.Reddit_Upvote.get() :
                self.check_list.append("Reddit Upvote")
            if self.Tiktok_Follower.get() :
                self.check_list.append("Tiktok Follower")
            if self.Tiktok_Like.get() :
                self.check_list.append("Tiktok Like")

            self.is_running = True
            Thread(target=self.checkbox_state1).start()
            Thread(target=self.schedule_job).start()
        else:
            self.is_running = False
            self.Start.configure(text="Wait")
            self.Start.configure(state="disabled")
            crazy.update()
            sleep(15)
            self.Start.configure(text="Start")
            self.Start.configure(fg_color='#1f538d')
            self.Start.configure(state="normal")          
    def checkbox_state1(self):
        bot = self.bot 
        while self.is_running :
            random.shuffle(self.check_list)
            for name in self.check_list:
                self.n = 0
                if self.is_running:
                    if name == "Facebook Page":
                        bot.get("https://addmefast.com/free_points/facebook_likes")
                        sleep(1)
                        ed.facebook_page()
                    if name == "Facebook Post":
                        bot.get("https://addmefast.com/free_points/facebook_post_like")
                        sleep(1)
                        ed.facebook_Post()
                    if name == "Facebook Share":
                        bot.get("https://addmefast.com/free_points/facebook_post_share")
                        sleep(1)
                        ed.facebook_Share()
                    
                    if name == "Twiter Follower" :
                        bot.get("https://addmefast.com/free_points/twitter")
                        sleep(1)
                        ed.twiter_Follow()
                    if name == "Twiter Retweet" :
                        bot.get("https://addmefast.com/free_points/twitter_retweets")
                        sleep(1)
                        ed.twiter_Retweet()
                    if name == "Twiter Like" :
                        bot.get("https://addmefast.com/free_points/twitter_likes")
                        sleep(1)
                        ed.twiter_Like()
                    
                    if name == "Insta Follower" :
                        bot.get("https://addmefast.com/free_points/instagram")
                        sleep(1)
                        ed.instagram_Follow()
                    if name == "Insta Like" :
                        bot.get("https://addmefast.com/free_points/instagram_likes")
                        sleep(1)
                        ed.instagram_Like()
                    
                    if name == "Youtube Subscribe" :
                        bot.get("https://addmefast.com/free_points/youtube_subscribe") 
                        sleep(1)
                        ed.youtube_subscribe()
                    if name == "Youtube Like" :
                        bot.get("https://addmefast.com/free_points/youtube_likes") 
                        sleep(1)
                        ed.youtube_Like()
                    
                    if name == "Pinterest Follower" :
                        self.bot.get("https://addmefast.com/free_points/pinterest")
                        sleep(1)
                        ed.pinterest_followers()
                    if name == "Pinterest Save" :
                        self.bot.get("https://addmefast.com/free_points/pinterest_save")
                        sleep(1)
                        ed.pinterest_save()
                    
                    if name == "Soundcloud Follow" :
                        self.bot.get("https://addmefast.com/free_points/soundcloud_follow")
                        sleep(1)
                        ed.soundcloud_follow()
                    if name == "Soundcloud Like" :
                        self.bot.get("https://addmefast.com/free_points/soundcloud_likes")
                        sleep(1)
                        ed.soundcloud_like()
                    
                    if name == "Reddit Members" :
                        self.bot.get("https://addmefast.com/free_points/reddit_members")
                        sleep(1)
                        ed.reddit_Members()
                    if name == "Reddit Upvote" :
                        self.bot.get("https://addmefast.com/free_points/reddit_upvotes")
                        sleep(1)
                        ed.reddit_Upvote()
                    
                    if name == "Tiktok Follower" :
                        self.bot.get("https://addmefast.com/free_points/tiktok_followers")
                        sleep(1) 
                        ed.tiktok_Follow()
                    if name == "Tiktok Like" :
                        self.bot.get("https://addmefast.com/free_points/tiktok_video_likes")
                        sleep(1) 
                        ed.tiktok_like()

    def login(self):
        button = self.bot.find_element(By.NAME, 'login_button')
        button.click()
        print("successfully logged in") 

    def open(self):
        self.Open.configure(state="disabled")
        print("Lodaing......")
        self.options = uc.ChromeOptions()
        pro = "C://Users//kreem//AppData//Local//Google//Chrome//User Data//"
        self.options.add_argument(f"user-data-dir={pro}")
        self.options.add_argument("--lang=en")
        self.options.add_argument("--start-maximized")
        self.bot = uc.Chrome(options=self.options,use_subprocess=True)
        bot = self.bot
        print("Done")

        bot.get("https://addmefast.com/login")
        sleep(5)
        try:
            ed.login()
        except:
            try:
                ed.Bypass_Cloudflare()
                bot.get("https://addmefast.com/login")
                sleep(2)
                try:
                    ed.login() 
                except:
                    print("successfully logged in")
            except:
                    print("successfully logged in")
            
        
        self.Start.configure(state="normal")
        self.Close.configure(state="normal")

    def facebook_Post(self):
        bot = self.bot
        while self.is_running :
            try:
                try:
                    subscribe = WebDriverWait(bot,5).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Like"))
                    )
                    subscribe.click()
                except:
                    try:
                        ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            subscribe = WebDriverWait(bot,10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, "Like"))
                            )
                            ed.facebook_Post() 
                            break
                        except:
                            ed.Check_items()
                            break
                bot.switch_to.window(bot.window_handles[1])  
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    # If the new tab does not exist, go back to the main tab and refresh
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.facebook_Post() 
                    break
                try:
                    bot.maximize_window()
                    button = WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Like')]")))
                    sleep(2)
                    button.click()
                    sleep(5)
                except:
                    self.n += 1
                    if self.n == 2 :
                        ed.Telgram(self.Facebook_text)
                        self.n = 0
                    
                    bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    confirm = WebDriverWait(bot, 5).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Confirm")))
                    confirm.click()
                    sleep(5)
                    ed.facebook_Post()
                    break
                self.n = 0
                bot.close()
                bot.switch_to.window(bot.window_handles[0])
                confirm = WebDriverWait(bot, 5).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Confirm")))
                confirm.click()
                sleep(5)
                ed.facebook_Post()
                break
            except : 
                try:
                    ed.Bypass_Cloudflare()
                    break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.facebook_Post()
                        break
                    except:
                        ed.Telgram(self.text2)
                        input("Error......")
                        break
                    break
                break
            break
    def facebook_page(self):
        while self.is_running:
            bot = self.bot 
            try:
                try:
                    subscribe = WebDriverWait(bot,10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Like/Follow"))
                    )
                    subscribe.click()
                except:
                    try:
                        ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            subscribe = WebDriverWait(bot,10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, "Like/Follow"))
                            )
                            ed.facebook_page() 
                            break
                        except:
                            ed.Check_items()
                            break
                bot.switch_to.window(bot.window_handles[1])  
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    # If the new tab does not exist, go back to the main tab and refresh
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.facebook_page() 
                    break
                try:
                    bot.maximize_window()
                    sleep(5)
                    try:
                        button = WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Like')]")))
                        sleep(2)
                        button.click()
                        sleep(5)
                    except:
                        button = WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Follow')]")))
                        sleep(2)
                        button.click()
                        sleep(5)
                except:
                    self.n += 1
                    if self.n == 2 :
                        ed.Telgram(self.Facebook_text)
                        self.n = 0
                        
                    sleep(5)
                    bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    confirm = WebDriverWait(bot, 5).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Confirm")))
                    confirm.click()
                    sleep(5)
                    ed.facebook_page()
                    break
                self.n = 0
                bot.close()
                bot.switch_to.window(bot.window_handles[0])
                confirm = WebDriverWait(bot, 5).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Confirm")))
                confirm.click()
                sleep(5)
                ed.facebook_page()
                break
            except : 
                try:
                    ed.Bypass_Cloudflare()
                    break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.facebook_page()
                        break
                    except:
                        ed.Telgram(self.text2)
                        input("Error......")
                        break
                    break
                break
            break
    def facebook_Share(self):
        while self.is_running :
            bot = self.bot
            try:
                try:
                    subscribe = WebDriverWait(bot,10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Share"))
                    )
                    subscribe.click()
                except:
                    try:
                        ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            subscribe = WebDriverWait(bot,10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, "Share"))
                            )
                            ed.facebook_Share() 
                            break
                        except:
                            ed.Check_items()
                            break
                bot.switch_to.window(bot.window_handles[1])  
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    # If the new tab does not exist, go back to the main tab and refresh
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.facebook_Share() 
                    break
                try:
                    bot.maximize_window()
                    sleep(2)
                    button = WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Share')]")))
                    button.click()
                    sleep(1)
                    try:
                        button = WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div/div[1]")))
                        button.click()
                        sleep(5)
                    except:
                        button = WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[3]/div/button")))
                        button.click()
                        sleep(5)
                except :
                    self.n += 1
                    if self.n == 5 :
                        ed.Telgram(self.Facebook_text)
                        self.n = 0
                        
                    bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    confirm = WebDriverWait(bot, 5).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Confirm")))
                    confirm.click()
                    sleep(5)
                    ed.facebook_Share()
                    break
                self.n = 0
                bot.close()
                sleep(5)
                bot.switch_to.window(bot.window_handles[0])
                confirm = WebDriverWait(bot, 5).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Confirm")))
                confirm.click()
                sleep(5)
                ed.facebook_Share()
                break
            except : 
                try:
                    ed.Bypass_Cloudflare()
                    break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.facebook_Share()
                        break
                    except:
                        ed.Telgram(self.text2)
                        input("Error......")
                        break
                    break
                break
            break
    
    def twiter_Follow(self):
        while self.is_running:
            bot = self.bot 
            try:
                try:
                    subscribe = WebDriverWait(bot,10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Follow"))
                    )
                    subscribe.click()
                except:
                    try:
                        ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            subscribe = WebDriverWait(bot,10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, "Follow"))
                            )
                            ed.twiter_Follow() 
                            break
                        except:
                            ed.Check_items()
                            break
                bot.switch_to.window(bot.window_handles[1])
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.twiter_Follow() 
                    break
                try:
                    button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span")))
                    sleep(2)
                    button.click()
                    sleep(5)
                except:
                    self.n += 1
                    if self.n == 2 :
                        ed.Telgram(self.Twitter_text)
                        self.n = 0
                        
                    bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    confirm = WebDriverWait(bot, 5).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Confirm")))
                    confirm.click()
                    sleep(5)
                    ed.twiter_Follow()
                    break
                self.n = 0
                bot.close()
                bot.switch_to.window(bot.window_handles[0])
                confirm = WebDriverWait(bot, 5).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Confirm")))
                confirm.click()
                sleep(5)
                ed.twiter_Follow()
                break
            except : 
                try:
                    ed.Bypass_Cloudflare()
                    break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.twiter_Follow()
                        break
                    except:
                        ed.Telgram(self.text2)
                        input("Error......")
                        break
                    break
                break
            break
    def twiter_Retweet(self):
        while self.is_running:
            bot = self.bot 
            try:
                try:
                    subscribe = WebDriverWait(bot,10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Retweet"))
                    )
                    subscribe.click()
                except:
                    try:
                        ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            subscribe = WebDriverWait(bot,10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, "Retweet"))
                            )
                            ed.twiter_Retweet() 
                            break
                        except:
                            ed.Check_items()
                            break
                bot.switch_to.window(bot.window_handles[1])
                bot.minimize_window()
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    # If the new tab does not exist, go back to the main tab and refresh
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.twiter_Retweet() 
                    break
                try:
                    button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span")))
                    sleep(2)
                    button.click()
                    sleep(5)
                except:
                    self.n += 1
                    if self.n == 5 :
                        ed.Telgram(self.Twitter_text)
                        self.n = 0
                        
                    bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    confirm = WebDriverWait(bot, 5).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Confirm")))
                    confirm.click()
                    sleep(5)
                    ed.twiter_Retweet()
                    break
                self.n = 0
                bot.close()
                bot.switch_to.window(bot.window_handles[0])
                confirm = WebDriverWait(bot, 5).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Confirm")))
                confirm.click()
                sleep(5)
                ed.twiter_Retweet()
                break
            except : 
                try:
                    ed.Bypass_Cloudflare()
                    break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.twiter_Retweet()
                        break
                    except:
                        ed.Telgram(self.text2)
                        input("Error......")
                        break
                    break
                break
            break
    def twiter_Like(self):
        while self.is_running:
            bot = self.bot 
            try:
                try:
                    sleep(5)
                    subscribe = WebDriverWait(bot,10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Like"))
                    )
                    subscribe.click()
                except:
                    try:
                        ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            subscribe = WebDriverWait(bot,10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, "Like"))
                            )
                            ed.twiter_Like() 
                            break
                        except:
                            ed.Check_items()
                            break
                bot.switch_to.window(bot.window_handles[1])
                bot.minimize_window()
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    # If the new tab does not exist, go back to the main tab and refresh
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.twiter_Like()
                    break
                try:
                    button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span")))
                    sleep(2)
                    button.click()
                    sleep(5)
                except:
                    self.n += 1
                    if self.n == 5 :
                        ed.Telgram(self.Twitter_text)
                        self.n = 0
                        
                    bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    confirm = WebDriverWait(bot, 5).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Confirm")))
                    confirm.click()
                    sleep(5)
                    ed.twiter_Like()
                    break
                self.n = 0
                bot.close()
                bot.switch_to.window(bot.window_handles[0])
                confirm = WebDriverWait(bot, 5).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Confirm")))
                confirm.click()
                sleep(5)
                ed.twiter_Like()
                break
            except : 
                try:
                    ed.Bypass_Cloudflare()
                    break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.twiter_Like()
                        break
                    except:
                        ed.Telgram(self.text2)
                        input("Error......")
                        break
                    break
                break
            break

    def instagram_Follow(self):
        while self.is_running:
            bot = self.bot 
            try:
                try:
                    subscribe = WebDriverWait(bot,10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Follow"))
                    )
                    subscribe.click()
                except:
                    try:
                        ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            subscribe = WebDriverWait(bot,10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, "Follow"))
                            )
                            ed.instagram_Follow() 
                            break
                        except:
                            ed.Check_items()
                            break
                bot.switch_to.window(bot.window_handles[1])  
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    # If the new tab does not exist, go back to the main tab and refresh
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.instagram_Follow()
                    break 
                try:
                    bot.maximize_window()
                    sleep(5)
                    button = WebDriverWait(bot, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//div[@class='_aacl _aaco _aacw _aad6 _aade']")))
                    button.click()
                except:
                    self.n += 1
                    if self.n == 2 :
                        ed.Telgram(self.Insta_text)
                        self.n = 0
                        
                    bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    confirm = WebDriverWait(bot, 10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Confirm")))
                    confirm.click()
                    sleep(5)
                    ed.instagram_Follow()
                    break
                self.n = 0
                bot.close()
                bot.switch_to.window(bot.window_handles[0])
                confirm = WebDriverWait(bot, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Confirm")))
                confirm.click()
                sleep(5)
                ed.instagram_Follow()
                break
            except : 
                try:
                    ed.Bypass_Cloudflare()
                    break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.instagram_Follow()
                        break
                    except:
                        ed.Telgram(self.text2)
                        input("Error......")
                        break
                    break
                break
            break
    def instagram_Like(self):
        bot = self.bot 
        while self.is_running:
            try:
                try:
                    subscribe = WebDriverWait(bot,10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Like"))
                    )
                    subscribe.click()
                except:
                    try:
                        ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            subscribe = WebDriverWait(bot,10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, "Like"))
                            )
                            ed.instagram_Like() 
                            break
                        except:
                            ed.Check_items()
                            break
                bot.switch_to.window(bot.window_handles[1])
                bot.minimize_window()
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    # If the new tab does not exist, go back to the main tab and refresh
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.instagram_Like() 
                    break
                try:
                    button = WebDriverWait(bot, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class='xp7jhwk']")))
                    button.click()
                    sleep(5)
                except:
                    self.n += 1
                    if self.n == 5 :
                        ed.Telgram(self.Insta_text)
                        self.n = 0
                        
                    bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    confirm = WebDriverWait(bot, 10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Confirm")))
                    confirm.click()
                    sleep(5)
                    ed.instagram_Like()
                    break
                self.n = 0
                bot.close()
                bot.switch_to.window(bot.window_handles[0])
                confirm = WebDriverWait(bot, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Confirm")))
                confirm.click()
                sleep(5)
                ed.instagram_Like()
                break
            except : 
                try:
                    ed.Bypass_Cloudflare()
                    break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.instagram_Like()
                        break
                    except:
                        ed.Telgram(self.text2)
                        input("Error......")
                        break
                    break
                break
            break
    
    def youtube_subscribe(self):
        while self.is_running :
            bot = self.bot 
            try:
                try:
                    subscribe = WebDriverWait(bot,10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Subscribe"))
                    )
                    subscribe.click()
                except:
                    try:
                        ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            subscribe = WebDriverWait(bot,10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, "Subscribe"))
                            )
                            ed.youtube_subscribe() 
                            break
                        except:
                            ed.Check_items()
                            break
                bot.switch_to.window(bot.window_handles[1])
                
                sleep(5)
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    # If the new tab does not exist, go back to the main tab and refresh
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.youtube_subscribe()
                    break
                try:
                    button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                        "button[class='yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m ']")))
                    button.click()
                    sleep(5)
                except:
                    bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    confirm = WebDriverWait(bot, 10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Confirm")))
                    confirm.click()
                    sleep(5)
                    ed.youtube_subscribe()
                    break
                
                bot.close()
                bot.switch_to.window(bot.window_handles[0])
                confirm = WebDriverWait(bot, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Confirm")))
                confirm.click()
                sleep(5)
                ed.youtube_subscribe()
                break
            except : 
                try:
                    ed.Bypass_Cloudflare()
                    break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.youtube_subscribe()
                        break
                    except:
                        ed.Telgram(self.text2)
                        input("Error......")
                        break
                    break
                break
            break
    def youtube_Like(self):
        bot = self.bot 
        while self.is_running:
            try:
                try:
                    subscribe = WebDriverWait(bot,10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Like"))
                    )
                    subscribe.click()
                except:
                    try:
                        ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            subscribe = WebDriverWait(bot,10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, "Like"))
                            )
                            ed.youtube_Like() 
                            break
                        except:
                            ed.Check_items()
                            break
                bot.switch_to.window(bot.window_handles[1])
                bot.minimize_window()
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    # If the new tab does not exist, go back to the main tab and refresh
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.youtube_Like()
                    break
                try:
                    button = WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-segmented-like-dislike-button-renderer/div[1]/ytd-toggle-button-renderer/yt-button-shape/button")))
                    button.click()
                    sleep(random.randrange(5,10))
                except:
                    bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    confirm = WebDriverWait(bot, 10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Confirm")))
                    confirm.click()
                    sleep(5)
                    ed.youtube_Like()
                    break
                
                bot.close()
                bot.switch_to.window(bot.window_handles[0])
                confirm = WebDriverWait(bot, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Confirm")))
                confirm.click()
                sleep(5)
                ed.youtube_Like()
                break
            except : 
                try:
                    ed.Bypass_Cloudflare()
                    break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.youtube_Like()
                        break
                    except:
                        ed.Telgram(self.text2)
                        input("Error......")
                        break
                    break
                break
            break
    
    def pinterest_followers(self):
        bot = self.bot 
        while self.is_running:
            try:
                try:
                    subscribe = WebDriverWait(bot, 10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Follow"))
                    )
                    subscribe.click()
                except:
                    try:
                        ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            subscribe = WebDriverWait(bot,10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, "Follow"))
                            )
                            ed.pinterest_followers() 
                            break
                        except:
                            ed.Check_items()
                            break
                bot.switch_to.window(bot.window_handles[1])
                bot.minimize_window()
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    # If the new tab does not exist, go back to the main tab and refresh
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.pinterest_followers()
                    break
                try:
                    button = WebDriverWait(bot, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Follow')]")))
                    button.click()
                    sleep(5)
                except:
                    bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.pinterest_followers()
                    break
                
                bot.close()
                bot.switch_to.window(bot.window_handles[0])
                sleep(5)
                ed.pinterest_followers()
                break
            except : 
                try:
                    ed.Bypass_Cloudflare()
                    break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.pinterest_followers()
                        break
                    except:
                        ed.Telgram(self.text2)
                        input("Error......")
                        break
                    break
                break
            break
    def pinterest_save(self):
        bot = self.bot 
        while self.is_running:
            try:
                try:
                    subscribe = WebDriverWait(bot, 10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Save"))
                    )
                    subscribe.click()
                except:
                    try:
                        ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            subscribe = WebDriverWait(bot,10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, "Save"))
                            )
                            ed.pinterest_save() 
                            break
                        except:
                            ed.Check_items()
                            break
                bot.switch_to.window(bot.window_handles[1])
                bot.minimize_window()
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    # If the new tab does not exist, go back to the main tab and refresh
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.pinterest_save()
                    break
                try:
                    button = WebDriverWait(bot, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Profile')]")))
                    button.click()
                    sleep(1)
                    try:
                        button = WebDriverWait(bot, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save')]")))
                        button.click()
                        sleep(5)
                    except:
                        pass    
                except:
                    bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.pinterest_save()
                    break
                
                bot.close()
                bot.switch_to.window(bot.window_handles[0])
                sleep(5)
                ed.pinterest_save()
                break
            except : 
                try:
                    ed.Bypass_Cloudflare()
                    break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.pinterest_save()
                        break
                    except:
                        ed.Telgram(self.text2)
                        input("Error......")
                        break
                    break
                break
            break
           
    def soundcloud_follow(self):
        while self.is_running:
            bot = self.bot 
            try:
                try:
                    subscribe = WebDriverWait(bot,10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Follow"))
                    )
                    subscribe.click()
                except:
                    try:
                        ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            subscribe = WebDriverWait(bot,10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, "Follow"))
                            )
                            ed.soundcloud_follow() 
                            break
                        except:
                            ed.Check_items()
                            break
                bot.switch_to.window(bot.window_handles[1])
                bot.minimize_window()
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    # If the new tab does not exist, go back to the main tab and refresh
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    ed.soundcloud_follow()
                    break
                try:
                    button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/button[1]")))
                    button.click()
                    sleep(5)
                except:
                    bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.soundcloud_follow()
                    break
                
                bot.close()
                bot.switch_to.window(bot.window_handles[0])
                sleep(5)
                ed.soundcloud_follow()
                break
            except : 
                try:
                    ed.Bypass_Cloudflare()
                    break
                except:
                    bot.refresh()
                    ed.soundcloud_follow()
                    break
                break
            break
    def soundcloud_like(self):
        while self.is_running:
            bot = self.bot 
            try:
                try:
                    subscribe = WebDriverWait(bot,10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Like"))
                    )
                    subscribe.click()
                except:
                    try:
                        ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            subscribe = WebDriverWait(bot,10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, "Like"))
                            )
                            ed.soundcloud_like() 
                            break
                        except:
                            ed.Check_items()
                            break
                bot.switch_to.window(bot.window_handles[1])
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    # If the new tab does not exist, go back to the main tab and refresh
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    ed.soundcloud_like()
                    break
                try:
                    button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[3]/div[1]/div/div[1]/div/div/div[2]/div/div/button[1]")))
                    button.click()
                    sleep(5)
                except:
                    bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.soundcloud_like()
                    break
                
                bot.close()
                bot.switch_to.window(bot.window_handles[0])
                sleep(5)
                ed.soundcloud_like()
                break
            except : 
                try:
                    ed.Bypass_Cloudflare()
                    break
                except:
                    bot.refresh()
                    ed.soundcloud_like()
                    break
                break
            break
            
    def reddit_Members(self):
        while self.is_running:
            bot = self.bot 
            try:
                try:
                    subscribe = WebDriverWait(bot,10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Join"))
                    )
                    subscribe.click()
                except:
                    try:
                        ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            subscribe = WebDriverWait(bot,10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, "Join"))
                            )
                            ed.reddit_Members() 
                            break
                        except:
                            ed.Check_items()
                            break
                bot.switch_to.window(bot.window_handles[1])
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    # If the new tab does not exist, go back to the main tab and refresh
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    ed.reddit_Members()
                    break
                
                try:
                    bot.minimize_window()
                    button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/button")))
                    button.click()
                    sleep(5)
                except:
                    bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.reddit_Members()
                    break
                
                bot.close()
                bot.switch_to.window(bot.window_handles[0])
                sleep(5)
                ed.reddit_Members()
                break
            except : 
                try:
                    ed.Bypass_Cloudflare()
                    break
                except:
                    bot.refresh()
                    ed.reddit_Members()
                    break
                break
            break
    def reddit_Upvote(self):
        while self.is_running:
            bot = self.bot 
            try:
                try:
                    subscribe = WebDriverWait(bot,10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Upvote"))
                    )
                    subscribe.click()
                except:
                    try:
                        ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            subscribe = WebDriverWait(bot,10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, "Upvote"))
                            )
                            ed.reddit_Upvote() 
                            break
                        except:
                            ed.Check_items()
                            break
                bot.switch_to.window(bot.window_handles[1])
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    # If the new tab does not exist, go back to the main tab and refresh
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    ed.reddit_Upvote()
                    break
                
                try:
                    bot.minimize_window()
                    button = WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[1]/div/div[1]/div/button[1]/span")))
                    button.click()
                    sleep(random.randrange(10,15))
                except:
                    bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.reddit_Upvote()
                    break
                
                bot.close()
                bot.switch_to.window(bot.window_handles[0])
                sleep(5)
                ed.reddit_Upvote()
                break
            except : 
                try:
                    ed.Bypass_Cloudflare()
                    break
                except:
                    bot.refresh()
                    ed.reddit_Upvote()
                    break
                break
            break
    
    def tiktok_Follow(self):
        while self.is_running:
            bot = self.bot 
            try:
                try:
                    subscribe = WebDriverWait(bot,10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Follow"))
                    )
                    subscribe.click()
                except:
                    try:
                        ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            subscribe = WebDriverWait(bot,10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, "Follow"))
                            )
                            ed.tiktok_Follow() 
                            break
                        except:
                            ed.Check_items()
                            break
                bot.switch_to.window(bot.window_handles[1])
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    # If the new tab does not exist, go back to the main tab and refresh
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    ed.tiktok_Follow()
                    break
                try:
                    button = WebDriverWait(bot, 6).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='button']")))
                    sleep(random.randrange(4,6))
                    button.click()
                    sleep(6)
                except:
                    bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.tiktok_Follow()
                    break
                
                bot.close()
                bot.switch_to.window(bot.window_handles[0])
                sleep(5)
                ed.tiktok_Follow()
                break
            except : 
                try:
                    ed.Bypass_Cloudflare()
                    break
                except:
                    bot.refresh()
                    ed.tiktok_Follow()
                    break
                break
            break
    def tiktok_like(self):
        while self.is_running:
            bot = self.bot 
            try:
                try:
                    subscribe = WebDriverWait(bot,10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Like"))
                    )
                    subscribe.click()
                except:
                    try:
                        ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            subscribe = WebDriverWait(bot,10).until(
                            EC.presence_of_element_located((By.LINK_TEXT, "Like"))
                            )
                            ed.tiktok_like() 
                            break
                        except:
                            ed.Check_items()
                            break
                bot.switch_to.window(bot.window_handles[1])
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    # If the new tab does not exist, go back to the main tab and refresh
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    ed.tiktok_like()
                    break
                try:
                    button = WebDriverWait(bot, 6).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-e2e="like-icon"]')))
                    sleep(random.randrange(4,6))
                    button.click()
                    sleep(random.randrange(6,10))
                except:
                    bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.tiktok_like()
                    break
                
                bot.close()
                bot.switch_to.window(bot.window_handles[0])
                sleep(5)
                ed.tiktok_like()
                break
            except : 
                try:
                    ed.Bypass_Cloudflare()
                    break
                except:
                    bot.refresh()
                    ed.tiktok_like()
                    break
                break
            break

    def Bonus(self):
        bot = self.bot
        if  self.is_running:
            bot.get("https://addmefast.com/bonus_points")
            try:
                subscribe = WebDriverWait(bot, 10).until(
                            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[3]/center/div[2]/center/div[3]/input"))
                        )
                subscribe.click()
                bot.back()
                
            except:
                print("NO Bonus Today")
                bot.back()

    def schedule_job(self):
        schedule.every().day.at("01:50").do(self.Bonus) 
        while True:
            schedule.run_pending()
            sleep(30)

    def Bypass_Cloudflare(self):
        WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/iframe")))
        ed.position()
        if int(self.radio_var.get()) == 1 :
            sleep(5)
            pyautogui.leftClick(642, 288, 1)
            sleep(10)
            try:
                WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/iframe")))
                ed.Telgram(self.text1)
                input("Press Enter.........")
            except:
                ed.Telgram(self.text)
        elif int(self.radio_var.get()) == 2:
            sleep(5)
            pyautogui.leftClick(166, 296, 1)
            sleep(10)
            try:
                WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/iframe")))
                ed.Telgram(self.text1)
                input("Press Enter.........")
            except:
                ed.Telgram(self.text)
        
    
    def Check_page(self):
        for _ in range(10):
            self.bot.switch_to.window(self.bot.window_handles[1]) 
            self.bot.close()
            self.bot.switch_to.window(self.bot.window_handles[0])

    def Check_items(self):
        subscribe = WebDriverWait(self.bot,10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'No items in this network for now. Please try later.')]"))
        )
        sleep(self.dlay)

    def Check_items1(self):
        subscribe = WebDriverWait(self.bot,10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Unfortunately an error occurred in the system. In order to try again please reload the page.')]"))
        )

    def position(self):
        x, y = pyautogui.position()
        if x == 0 and y == 0:
            ed.Telgram(self.text3)
            input("No.screens......")
    
    def Telgram(self,text):
        url = f'https://api.telegram.org/bot{self.api_token}/sendMessage'
        payload = {'chat_id': self.chat_id, 'text': text}
        response = requests.post(url, json=payload)
    def close (self):
        self.bot.quit()
        
if __name__ == '__main__':
    crazy = CTk()
    ed = AMFBot(crazy)
    crazy.mainloop()
