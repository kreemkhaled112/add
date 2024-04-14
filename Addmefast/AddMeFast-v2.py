<<<<<<< HEAD:AddMeFast-v2.py
from __init__ import * 
from Follow import *
from Like import *
from Share import *
class Tiktok(CTk):
    def __init__(self, window_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Follow')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 230) // 2
        y = (screen_height - 100) // 2
        self.geometry(f"230x100+{x}+{y}")
        self.resizable(False,False)
        CTkLabel(self,text=window_name ).place(x=85,y=15)
        self.value = StringVar()
        ok = CTkButton(self, text="Ok", width=100, command=self.Ok)
        cancel = CTkButton(self, text="Cancel", width=100, command=self.Cancel)
        ok.place(x=10, y=55)
        cancel.place(x=120, y=55)

    def Ok(self):
        self.value.set("Ok")
        self.destroy()

    def Cancel(self):
        self.value.set("Cancel")
        self.destroy()

class AMFBot:
    def __init__(self,crazy):
        self.crazy = crazy
        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")
        self.crazy.geometry('400x400+500+150')
        self.crazy.resizable(False,False)
        self.crazy.title("                        Crazy")
        self.n = 0
        self.is_running = False
        self.check_list = []
        self.befor = random.randrange(3,6)
        self.after = random.randrange(5,10)
        self.dlay = random.randrange(5,10)
        self.cookie = 'sb=V8UWZplReEw7vE__luuANZwA;datr=V8UWZiILQViftY8LIvCKANDh;ps_n=0;ps_l=0;c_user=61553425026843;presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1712939933058%2C%22v%22%3A1%7D;wd=958x951;xs=1%3ANSf9wFAM5mIqmw%3A2%3A1712939235%3A-1%3A-1%3A%3AAcXJPRDDJC3V2ze76ZmkW4m3DlFoMz8TTtrnEctdxw;fr=19CLBlaQTM3Im8wIx.AWUg2NZWrUk4ujKDmCFhCRa1gvk.BmGiTC..AAA.0.0.BmGiTC.AWWaKTnyBQQ;'
        self.api_token = '6286940046:AAFrut4rAMEfmcAdRTwPZpe0OHMidgeC9Qw'
        self.chat_id = '1733472658'
        Bot = "Bot!"
        self.text = f'Bypass CloudFlare successfully, {Bot}'
        self.text1 = f'Bypass CloudFlare Faild, {Bot}'
        self.text2 = f' Error, {Bot}'
        self.text3 = f' Faild No.screens, {Bot}'
        self.Facebook_text = f'Facebook Problem, {Bot}'
        self.Insta_text = f'Insta Problem, {Bot}'
        self.Twitter_text = f'Twitter problem, {Bot}'
        self.Youtube_text = f'Youtube problem, {Bot}'
        
        self.Facebook_Post = IntVar()
        self.Facebook_Page = IntVar()
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
        

        Facebook_Post = CTkCheckBox(self.crazy, text="Facebook Post", variable=self.Facebook_Post)
        Facebook_Page = CTkCheckBox(self.crazy, text="Facebook Page", variable=self.Facebook_Page)
        Facebook_Share = CTkCheckBox(self.crazy, text="Facebook Share", variable=self.Facebook_Share)
        Twiter_Follower = CTkCheckBox(self.crazy, text="Twiter Follower", variable=self.Twiter_Follower)
        Twiter_Retweet = CTkCheckBox(self.crazy, text="Twiter Retweet", variable=self.Twiter_Retweet)
        Twiter_Like = CTkCheckBox(self.crazy, text="Twiter Like", variable=self.Twiter_Like)
        Insta_Follower = CTkCheckBox(self.crazy, text="Insta Follower", variable=self.Insta_Follower)
        Insta_Like = CTkCheckBox(self.crazy, text="Insta Like", variable=self.Insta_Like)
        Youtube_Subscribe = CTkCheckBox(self.crazy, text="Youtube Subscribe", variable=self.Youtube_Subscribe)
        Youtube_Like = CTkCheckBox(self.crazy, text="Youtube Like", variable=self.Youtube_Like)
        Pinterest_Follower = CTkCheckBox(self.crazy, text="Pinterest Follower", variable=self.Pinterest_Follower)
        Pinterest_Save = CTkCheckBox(self.crazy, text="Pinterest Save", variable=self.Pinterest_Save)
        Soundcloud_Follower = CTkCheckBox(self.crazy, text="Soundcloud Follow",state="disabled", variable=self.Soundcloud_Follower)
        Soundcloud_Like = CTkCheckBox(self.crazy, text="Soundcloud Like",state="disabled", variable=self.Soundcloud_Like)
        Reddit_Members = CTkCheckBox(self.crazy, text="Reddit Members",state="disabled", variable=self.Reddit_Members)
        Reddit_Upvote = CTkCheckBox(self.crazy, text="Reddit Upvote", variable=self.Reddit_Upvote)
        Tiktok_Follower = CTkCheckBox(self.crazy, text="Tiktok Follower", variable=self.Tiktok_Follower)
        Tiktok_Like = CTkCheckBox(self.crazy, text="Tiktok Like", variable=self.Tiktok_Like)

        Facebook_Post.place(x=10,y=10)
        Facebook_Page.place(x=150,y=10)
        Facebook_Share.place(x=275,y=10)
        Twiter_Follower.place(x=10,y=50)
        Twiter_Retweet.place(x=150,y=50)
        Twiter_Like.place(x=275,y=50)
        Insta_Follower.place(x=10,y=90)
        Insta_Like.place(x=150,y=90)
        Youtube_Subscribe.place(x=10,y=130)
        Youtube_Like.place(x=150,y=130)
        Pinterest_Follower.place(x=10,y=170)
        Pinterest_Save.place(x=150,y=170)
        Soundcloud_Follower.place(x=10,y=210)
        Soundcloud_Like.place(x=150,y=210)
        Reddit_Members.place(x=10,y=250)
        Reddit_Upvote.place(x=150,y=250)
        Tiktok_Follower.place(x=10,y=290)
        Tiktok_Like.place(x=150,y=290)

        

        self.Open = CTkButton(self.crazy, text="Open",width=100,state="disabled",command=lambda: Thread(target=self.open).start())
        self.Open.place(x=10,y=350)

        self.Start = CTkButton(self.crazy, text="Start",width=100,state="disabled",hover=False,command=lambda: Thread(target=self.checkbox_state).start())
        self.Start.place(x=145,y=350)

        self.Close = CTkButton(self.crazy, text="Close",state="disabled",width=100,command=lambda: Thread(target=self.close).start())
        self.Close.place(x=280,y=350)

        self.radio_var = IntVar()

        self.radio1 = CTkRadioButton(self.crazy, text="Laptop",height=28,command=lambda: self.Open.configure(state="normal"),variable= self.radio_var, value=1)
        self.radio1.place(x=290,y=290)
        self.load_settings()
    def checkbox_state(self):
        self.Save_settings()
        if not self.is_running:
            sleep(2)
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
        else:
            self.is_running = False
            self.Start.configure(text="Wait")
            self.Start.configure(state="disabled")
            crazy.update()
            sleep(30)
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
                    if name == "Facebook Post":
                        bot.get("https://addmefast.com/free_points/facebook_post_like")
                        sleep(1)
                        ed.facebook_post()
                    if name == "Facebook Page":
                        bot.get("https://addmefast.com/free_points/facebook_likes")
                        sleep(1)
                        ed.facebook_page()
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
            if self.is_running:
                self.crazy.title("                        Crazy Wait 100")
                sleep(100)
                self.crazy.title("                        Crazy")
    def login(self):
        self.bot.find_element(By.NAME, 'login_button').click()
        print("successfully logged in")

    def open(self):
        self.Open.configure(state="disabled")
        print("Lodaing......")
        chrome_options = uc.ChromeOptions()
        pro = "C://Users//kreem//AppData//Local//Google//Chrome//User Data//"
        chrome_options.add_argument("--profile-directory=Profile 5")
        chrome_options.add_argument(f"user-data-dir={pro}")
        self.bot = uc.Chrome(options=chrome_options)
        bot = self.bot
        print("Done")

        bot.get("https://addmefast.com/login")
        sleep(5)
        try:ed.login()
        except:
            try:
                ed.Bypass_Cloudflare()
                sleep(2)
                try:ed.login() 
                except:print("successfully logged in")
            except:print("successfully logged in")
        
        self.Start.configure(state="normal")
        self.Close.configure(state="normal")
    def facebook_post(self):
        while self.is_running:
            bot = self.bot 
            try:
                try:  WebDriverWait(bot,5).until(EC.presence_of_element_located((By.LINK_TEXT, "Like"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,5).until(EC.presence_of_element_located((By.LINK_TEXT, "Like"))).click()
                            ed.facebook_post() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])  
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.facebook_post() 
                    break
                try:
                    url = bot.current_url
                    Like(url,"Like",self.cookie).Start()
                except:
                    ed.Telgram(self.Facebook_text)
                    self.Confirm()
                    ed.facebook_post()
                    break
                ed.Confirm()
                ed.facebook_post()
                break
            except : 
                try: ed.Bypass_Cloudflare() ; ed.facebook_post() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.facebook_post()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break                
    def facebook_page(self):
        while self.is_running:
            bot = self.bot 
            try:
                try:  WebDriverWait(bot,5).until(EC.presence_of_element_located((By.LINK_TEXT, "Like/Follow"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,5).until(EC.presence_of_element_located((By.LINK_TEXT, "Like/Follow"))).click()
                            ed.facebook_page() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])  
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.facebook_page() 
                    break
                try:
                    url = bot.current_url
                    Follow(url,self.cookie).Start()
                except:
                    ed.Telgram(self.Facebook_text)
                    self.Confirm()
                    ed.facebook_page()
                    break
                ed.Confirm()
                ed.facebook_page()
                break
            except : 
                try: ed.Bypass_Cloudflare() ; ed.facebook_page() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.facebook_page()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break               
    def facebook_Share(self):
        while self.is_running :
            bot = self.bot
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Share"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Share")))
                            ed.facebook_Share() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])  
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.facebook_Share() 
                    break
                try:
                    url = bot.current_url
                    Share(url,'',self.cookie).Start()
                except :

                    ed.Telgram(self.Facebook_text)
                    ed.Confirm()
                    ed.facebook_Share()
                    break
                ed.Confirm()
                ed.facebook_Share()
                break
            except : 
                try: ed.Bypass_Cloudflare() ; ed.facebook_Share() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.facebook_Share()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break
                    
    def twiter_Follow(self):
        while self.is_running:
            bot = self.bot 
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Follow"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Follow")))
                            ed.twiter_Follow() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.twiter_Follow() 
                    break
                try:
                    sleep(self.befor)
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span"))).click()
                    sleep(self.after)
                except:
                    self.n += 1
                    if self.n == 2 :
                        ed.Telgram(self.Twitter_text)
                        self.n = 0
                    ed.Confirm()
                    ed.twiter_Follow()
                    break
                self.n = 0
                ed.Confirm()
                ed.twiter_Follow()
                break
            except : 
                try: ed.Bypass_Cloudflare(); ed.twiter_Follow() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.twiter_Follow()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break                   
    def twiter_Retweet(self):
        while self.is_running:
            bot = self.bot 
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Retweet"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Retweet")))
                            ed.twiter_Retweet() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.twiter_Retweet() 
                    break
                try:
                    sleep(self.befor)
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span"))).click()
                    sleep(self.after)
                except:
                    self.n += 1
                    if self.n == 5 :
                        ed.Telgram(self.Twitter_text)
                        self.n = 0 
                    ed.Confirm()
                    ed.twiter_Retweet()
                    break
                self.n = 0
                ed.Confirm()
                ed.twiter_Retweet()
                break
            except : 
                try: ed.Bypass_Cloudflare(); ed.twiter_Retweet() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.twiter_Retweet()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break                   
    def twiter_Like(self):
        while self.is_running:
            bot = self.bot 
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Like"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Like")))
                            ed.twiter_Like() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.twiter_Like()
                    break
                try:
                    sleep(self.befor)
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span"))).click()
                    sleep(self.after)
                except:
                    self.n += 1
                    if self.n == 5 :
                        ed.Telgram(self.Twitter_text)
                        self.n = 0 
                    ed.Confirm()
                    ed.twiter_Like()
                    break
                self.n = 0
                ed.Confirm()
                ed.twiter_Like()
                break
            except : 
                try: ed.Bypass_Cloudflare(); ed.twiter_Like() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.twiter_Like()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break
    def instagram_Follow(self):
        while self.is_running:
            bot = self.bot 
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Follow"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Follow")))
                            ed.instagram_Follow() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])  
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.instagram_Follow()
                    break 
                try:
                    sleep(self.befor)
                    try:WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class=' _acan _acap _acat _aj1- _ap30']"))).click()
                    except :WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='_ap3a _aaco _aacw _aad6 _aade']"))).click()

                    sleep(self.after)
                except:
                    self.n += 1
                    if self.n == 3 :
                        ed.Telgram(self.Insta_text)
                        self.n = 0
                    ed.Confirm()
                    ed.instagram_Follow()
                    break
                self.n = 0
                ed.Confirm()
                ed.instagram_Follow()
                break
            except : 
                try: ed.Bypass_Cloudflare(); ed.instagram_Follow() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.instagram_Follow()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break         
    def instagram_Like(self):
        bot = self.bot 
        while self.is_running:
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Like"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Like")))
                            ed.instagram_Like() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.instagram_Like() 
                    break
                try:
                    sleep(self.befor)
                    try: WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class='xp7jhwk']"))).click()
                    except: WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class='_aamw']"))).click()
                    sleep(self.after)
                except:
                    self.n += 1
                    if self.n == 5 :
                        ed.Telgram(self.Insta_text)
                        self.n = 0     
                    ed.Confirm()
                    ed.instagram_Like()
                    break
                self.n = 0
                ed.Confirm()
                ed.instagram_Like()
                break
            except : 
                try: ed.Bypass_Cloudflare(); ed.instagram_Like() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.instagram_Like()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break
    
    def youtube_subscribe(self):
        while self.is_running :
            bot = self.bot 
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Subscribe"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Subscribe")))
                            ed.youtube_subscribe() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])
                
                sleep(5)
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.youtube_subscribe()
                    break
                try:
                    sleep(self.befor)
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH,
                        '//*[@id="visibility-button"]/ytd-button-renderer'))).click()
                    sleep(1)
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH,
                        '//*[@id="subscribe-button"]/ytd-subscribe-button-renderer'))).click()
                    sleep(self.after)
                except:
                    self.n += 1
                    if self.n == 1 :
                        self.Bypass_youtube()
                        self.n = 0
                    ed.Confirm()
                    ed.youtube_subscribe()
                    break
                
                ed.Confirm()
                ed.youtube_subscribe()
                break
            except : 
                try: ed.Bypass_Cloudflare() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.youtube_subscribe()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break                   
    def youtube_Like(self):
        bot = self.bot 
        while self.is_running:
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Like"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Like")))
                            ed.youtube_Like() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.youtube_Like()
                    break
                try:
                    sleep(self.befor)
                    WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH,
                        "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/segmented-like-dislike-button-view-model/yt-smartimation/div/div/like-button-view-model/toggle-button-view-model/button-view-model/button"))).click()
                    sleep(random.randrange(5,10))
                except:
                    self.n += 1
                    if self.n == 1 :
                        self.Bypass_youtube()
                        self.n = 0
                    ed.Confirm()
                    ed.youtube_Like()
                    break
                self.n = 0
                ed.Confirm()
                ed.youtube_Like()
                break
            except : 
                try: ed.Bypass_Cloudflare() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.youtube_Like()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break
                    
    def pinterest_followers(self):
        bot = self.bot 
        while self.is_running:
            try:
                try: WebDriverWait(bot, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Follow"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Follow")))
                            ed.pinterest_followers() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.pinterest_followers()
                    break
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Follow')]"))).click()
                    sleep(self.after)
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
                try: ed.Bypass_Cloudflare() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.pinterest_followers()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break                   
    def pinterest_save(self):
        bot = self.bot 
        while self.is_running:
            try:
                try: WebDriverWait(bot, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Save"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Save")))
                            ed.pinterest_save() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.pinterest_save()
                    break
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Profile')]"))).click()
                    sleep(1)
                    try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save')]"))).click() ;sleep(self.after)
                    except: pass    
                except:
                    bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.pinterest_save()
                    break
                self.n = 0 
                bot.close()
                bot.switch_to.window(bot.window_handles[0])
                sleep(5)
                ed.pinterest_save()
                break
            except : 
                try: ed.Bypass_Cloudflare() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.pinterest_save()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break
    
    def tiktok_Follow(self):
        while self.is_running:
            bot = self.bot 
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Follow"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Follow")))
                            ed.tiktok_Follow() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])
                bot.minimize_window()
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.tiktok_Follow()
                    break
                try:
                    # sleep(self.befor)
                    # WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-e2e='follow-button']"))).click()
                    # sleep(random.randrange(5,10))
                    url = bot.current_url
                    requests.post(f'https://api.telegram.org/bot{self.api_token}/sendMessage', json={'chat_id': self.chat_id, 'text': url})
                    username = re.search(r'@(\w+)', url).group(0)
                    Tiktok(username).mainloop()
                    sleep(10)
                except:
                    self.bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.tiktok_Follow()
                    break
                self.bot.close()
                bot.switch_to.window(bot.window_handles[0])
                sleep(5)
                ed.tiktok_Follow()
                break
            except : 
                try: ed.Bypass_Cloudflare() ; ed.tiktok_Follow() ;break
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    ed.tiktok_Follow()
                    break
    def tiktok_like(self):
        while self.is_running:
            bot = self.bot 
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Like"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Like")))
                            ed.tiktok_like() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])
                bot.minimize_window()
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.tiktok_like()
                    break
                try:
                    url = bot.current_url
                    requests.post(f'https://api.telegram.org/bot{self.api_token}/sendMessage', json={'chat_id': self.chat_id, 'text': url})
                    username = re.search(r'@(\w+)', url).group(0)
                    Tiktok(username).mainloop()
                    sleep(5)
                except:
                    self.bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.tiktok_like()
                    break
                self.bot.close()
                bot.switch_to.window(bot.window_handles[0])
                sleep(5)
                ed.tiktok_like()
                break
            except : 
                try: ed.Bypass_Cloudflare(); ed.tiktok_like() ;break
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    ed.tiktok_like()
                    break
    
    def reddit_Upvote(self):
        while self.is_running:
            bot = self.bot 
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Upvote"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Upvote")))
                            ed.reddit_Upvote() 
                            break
                        except: ed.Check_items() ; break
                bot.switch_to.window(bot.window_handles[1])
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.reddit_Upvote()
                    break
                
                try:
                    sleep(self.befor)
                    try : WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[1]/div/div[1]/div/button[1]/span"))).click()
                    except : WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/shreddit-app/dsa-transparency-modal-provider/report-flow-provider/div/main/shreddit-post//div[2]/span/span/button[1]/span"))).click()
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
                try: ed.Bypass_Cloudflare() ; ed.reddit_Upvote() ; break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.reddit_Upvote()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break

                        
    def Bypass_youtube(self):
        self.bot.switch_to.window(self.bot.window_handles[0])
        pyautogui.leftClick(290, 18, 1)
        sleep(2)
        pyautogui.write("https://kepondo.com/?http://www.youtube.com/watch?v=-LCSl3pYkkU")
        pyautogui.press('enter')
        sleep(10)
        pyautogui.leftClick(45, 375, 1)
        sleep(10)
        pyautogui.leftClick(495, 21, 1)
        self.bot.switch_to.window(self.bot.window_handles[1])
    def Bypass_Cloudflare(self):
        a = 0
        WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/iframe")))
        ed.position()
        for _ in range(2):
            if int(self.radio_var.get()) == 1:
                pyautogui.leftClick(290, 18, 1)
                sleep(2)
                pyautogui.leftClick(71, 101, 1)
                sleep(2)
                pyautogui.leftClick(71, 101, 1)
                sleep(10)
                pyautogui.leftClick(45, 375, 1)
                sleep(10)
                self.bot.switch_to.window(self.bot.window_handles[1])
                self.bot.close()
                self.bot.switch_to.window(self.bot.window_handles[0])
                sleep(5)
                self.bot.refresh()
                try:
                    WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/iframe")))
                    a += 1
                except: self.bot.switch_to.window(self.bot.window_handles[0]) ;break
        if a == 2:
            ed.Telgram(self.text1)
            input("Error Cloudflare.........")
        
    # def Bonus(self):
    #     bot = self.bot
    #     if  self.is_running:
    #         bot.execute_script("window.open()")

    #         bot.switch_to.window(bot.window_handles[-1])
    #         bot.get("https://addmefast.com/bonus_points")
    #         try:
    #             subscribe = WebDriverWait(bot, 10).until(
    #                         EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[3]/center/div[2]/center/div[3]/input"))
    #                     )
    #             subscribe.click()
    #             bot.close()
    #             bot.switch_to.window(bot.window_handles[0])
    #         except:
    #             print("NO Bonus Today")
    #             bot.close()
    #             bot.switch_to.window(bot.window_handles[0])


    def Check_page(self):
        for _ in range(10):
            self.bot.switch_to.window(self.bot.window_handles[1]) 
            self.bot.close()
            self.bot.switch_to.window(self.bot.window_handles[0])

    def Check_items(self):
        WebDriverWait(self.bot,10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'No items in this network for now. Please try later.')]")))
        sleep(self.dlay)

    def Check_items1(self):
        WebDriverWait(self.bot,10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Unfortunately an error occurred in the system. In order to try again please reload the page.')]")))

    def position(self):
        x, y = pyautogui.position()
        if x == 0 and y == 0:
            ed.Telgram(self.text3)
            input("No.screens......")
    
    def Telgram(self,text):
        url = f'https://api.telegram.org/bot{self.api_token}/sendMessage'
        payload = {'chat_id': self.chat_id, 'text': text}
        response = requests.post(url, json=payload)
        input(f"{text},Enter....")
    def Confirm(self):
        self.bot.close()
        self.bot.switch_to.window(self.bot.window_handles[0])
        WebDriverWait(self.bot, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Confirm"))).click()
        sleep(self.befor)

    def Save_settings(self):
        config = ConfigParser()
        config['contact'] = {
            'Facebook_Post': self.Facebook_Post.get(),
            'Facebook_Page': self.Facebook_Page.get(),
            'Facebook_Share': self.Facebook_Share.get(),
            'Twiter_Follower': self.Twiter_Follower.get(),
            'Twiter_Retweet': self.Twiter_Retweet.get(),
            'Twiter_Like': self.Twiter_Like.get(),
            'Insta_Follower': self.Insta_Follower.get(),
            'Insta_Like': self.Insta_Like.get(),
            'Youtube_Subscribe': self.Youtube_Subscribe.get(),
            'Youtube_Like': self.Youtube_Like.get(),
            'Pinterest_Follower': self.Pinterest_Follower.get(),
            'Pinterest_Save': self.Pinterest_Save.get(),
            'Tiktok_Follower': self.Tiktok_Follower.get(),
            'Tiktok_Like': self.Tiktok_Like.get(),
            }
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)
    def load_settings(self):
        try:
            config = ConfigParser()
            config.read('settings.ini')
            self.Facebook_Post.set(config.get('contact', 'Facebook_Post'))
            self.Facebook_Page.set(config.get('contact', 'Facebook_Page'))
            self.Facebook_Share.set(config.get('contact', 'Facebook_Share'))
            self.Twiter_Follower.set(config.get('contact', 'Twiter_Follower'))
            self.Twiter_Retweet.set(config.get('contact', 'Twiter_Retweet'))
            self.Twiter_Like.set(config.get('contact', 'Twiter_Like'))
            self.Insta_Follower.set(config.get('contact', 'Insta_Follower'))
            self.Insta_Like.set(config.get('contact', 'Insta_Like'))
            self.Youtube_Subscribe.set(config.get('contact', 'Youtube_Subscribe'))
            self.Youtube_Like.set(config.get('contact', 'Youtube_Like'))
            self.Pinterest_Follower.set(config.get('contact', 'Pinterest_Follower'))
            self.Pinterest_Save.set(config.get('contact', 'Pinterest_Save'))
            self.Tiktok_Follower.set(config.get('contact', 'Tiktok_Follower'))
            self.Tiktok_Like.set(config.get('contact', 'Tiktok_Like'))
            
        except Exception as e:
            pass
            # messagebox.showwarning("Error", f"An error occurred while loading settings:\n{e}") 

    def close (self):
        try:
            self.Save_settings()
            self.bot.quit()
            crazy.destroy()
        except:pass 
if __name__ == '__main__':
    crazy = CTk()
    ed = AMFBot(crazy)
    crazy.mainloop()
=======
from __init__ import * 
from Follow import *
from Like import *
from Share import *
class Tiktok(CTk):
    def __init__(self, window_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Follow')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 230) // 2
        y = (screen_height - 100) // 2
        self.geometry(f"230x100+{x}+{y}")
        self.resizable(False,False)
        CTkLabel(self,text=window_name ).place(x=85,y=15)
        self.value = StringVar()
        ok = CTkButton(self, text="Ok", width=100, command=self.Ok)
        cancel = CTkButton(self, text="Cancel", width=100, command=self.Cancel)
        ok.place(x=10, y=55)
        cancel.place(x=120, y=55)

    def Ok(self):
        self.value.set("Ok")
        self.destroy()

    def Cancel(self):
        self.value.set("Cancel")
        self.destroy()

class AMFBot:
    def __init__(self,crazy):
        self.crazy = crazy
        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")
        self.crazy.geometry('400x400+500+150')
        self.crazy.resizable(False,False)
        self.crazy.title("                        Crazy")
        self.n = 0
        self.is_running = False
        self.check_list = []
        self.befor = random.randrange(3,6)
        self.after = random.randrange(5,10)
        self.dlay = random.randrange(5,10)
        self.cookie = 'ps_n=0;sb=9vjdZcIbN_1FBlBL-qUMC9DW;datr=9vjdZWZMGF4JZuuFse6Fd9_i;c_user=61550782617657;i_user=61557453324574;m_ls=%7B%2261550782617657%22%3A%7B%22c%22%3A%7B%221%22%3A%22HCwAABbWARbQhd8pEwUW8uDEiN3-GwA%22%2C%222%22%3A%22GSwVQBxMAAAWARbkvtjgDBYAABV-HEwAABYAFt6-2OAMFgAAFigA%22%2C%2295%22%3A%22HCwAABZSFsbo96cNEwUW8uDEiN3-GwA%22%7D%2C%22d%22%3A%222d6a4028-9260-4407-909c-e45f1a70fc62%22%2C%22s%22%3A%220%22%2C%22u%22%3A%22ux4zkp%22%7D%7D;xs=44%3Az0dIIEN-Ox1sww%3A2%3A1712000933%3A-1%3A13657%3A%3AAcVY-QJVHcKIRswJK4rVPHZQXlk836_ZoT9XesZtTA;fr=1PClvRp2ioClQYGlM.AWUp3o_HwixJeczKhQBMmtFTFMI.BmDP9u..AAA.0.0.BmDP9u.AWWTttcwZ9M;wd=942x943;presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1712127857383%2C%22v%22%3A1%7D;'
        self.api_token = '6286940046:AAFrut4rAMEfmcAdRTwPZpe0OHMidgeC9Qw'
        self.chat_id = '1733472658'
        Bot = "Bot!"
        self.text = f'Bypass CloudFlare successfully, {Bot}'
        self.text1 = f'Bypass CloudFlare Faild, {Bot}'
        self.text2 = f' Error, {Bot}'
        self.text3 = f' Faild No.screens, {Bot}'
        self.Facebook_text = f'Facebook Problem, {Bot}'
        self.Insta_text = f'Insta Problem, {Bot}'
        self.Twitter_text = f'Twitter problem, {Bot}'
        self.Youtube_text = f'Youtube problem, {Bot}'
        
        self.Facebook_Post = IntVar()
        self.Facebook_Page = IntVar()
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
        

        Facebook_Post = CTkCheckBox(self.crazy, text="Facebook Post", variable=self.Facebook_Post)
        Facebook_Page = CTkCheckBox(self.crazy, text="Facebook Page", variable=self.Facebook_Page)
        Facebook_Share = CTkCheckBox(self.crazy, text="Facebook Share", variable=self.Facebook_Share)
        Twiter_Follower = CTkCheckBox(self.crazy, text="Twiter Follower", variable=self.Twiter_Follower)
        Twiter_Retweet = CTkCheckBox(self.crazy, text="Twiter Retweet", variable=self.Twiter_Retweet)
        Twiter_Like = CTkCheckBox(self.crazy, text="Twiter Like", variable=self.Twiter_Like)
        Insta_Follower = CTkCheckBox(self.crazy, text="Insta Follower", variable=self.Insta_Follower)
        Insta_Like = CTkCheckBox(self.crazy, text="Insta Like", variable=self.Insta_Like)
        Youtube_Subscribe = CTkCheckBox(self.crazy, text="Youtube Subscribe", variable=self.Youtube_Subscribe)
        Youtube_Like = CTkCheckBox(self.crazy, text="Youtube Like", variable=self.Youtube_Like)
        Pinterest_Follower = CTkCheckBox(self.crazy, text="Pinterest Follower", variable=self.Pinterest_Follower)
        Pinterest_Save = CTkCheckBox(self.crazy, text="Pinterest Save", variable=self.Pinterest_Save)
        Soundcloud_Follower = CTkCheckBox(self.crazy, text="Soundcloud Follow",state="disabled", variable=self.Soundcloud_Follower)
        Soundcloud_Like = CTkCheckBox(self.crazy, text="Soundcloud Like",state="disabled", variable=self.Soundcloud_Like)
        Reddit_Members = CTkCheckBox(self.crazy, text="Reddit Members",state="disabled", variable=self.Reddit_Members)
        Reddit_Upvote = CTkCheckBox(self.crazy, text="Reddit Upvote", variable=self.Reddit_Upvote)
        Tiktok_Follower = CTkCheckBox(self.crazy, text="Tiktok Follower", variable=self.Tiktok_Follower)
        Tiktok_Like = CTkCheckBox(self.crazy, text="Tiktok Like", variable=self.Tiktok_Like)

        Facebook_Post.place(x=10,y=10)
        Facebook_Page.place(x=150,y=10)
        Facebook_Share.place(x=275,y=10)
        Twiter_Follower.place(x=10,y=50)
        Twiter_Retweet.place(x=150,y=50)
        Twiter_Like.place(x=275,y=50)
        Insta_Follower.place(x=10,y=90)
        Insta_Like.place(x=150,y=90)
        Youtube_Subscribe.place(x=10,y=130)
        Youtube_Like.place(x=150,y=130)
        Pinterest_Follower.place(x=10,y=170)
        Pinterest_Save.place(x=150,y=170)
        Soundcloud_Follower.place(x=10,y=210)
        Soundcloud_Like.place(x=150,y=210)
        Reddit_Members.place(x=10,y=250)
        Reddit_Upvote.place(x=150,y=250)
        Tiktok_Follower.place(x=10,y=290)
        Tiktok_Like.place(x=150,y=290)

        

        self.Open = CTkButton(self.crazy, text="Open",width=100,state="disabled",command=lambda: Thread(target=self.open).start())
        self.Open.place(x=10,y=350)

        self.Start = CTkButton(self.crazy, text="Start",width=100,state="disabled",hover=False,command=lambda: Thread(target=self.checkbox_state).start())
        self.Start.place(x=145,y=350)

        self.Close = CTkButton(self.crazy, text="Close",state="disabled",width=100,command=lambda: Thread(target=self.close).start())
        self.Close.place(x=280,y=350)

        self.radio_var = IntVar()

        self.radio1 = CTkRadioButton(self.crazy, text="Laptop",height=28,command=lambda: self.Open.configure(state="normal"),variable= self.radio_var, value=1)
        self.radio1.place(x=290,y=290)
        self.load_settings()
    def checkbox_state(self):
        self.Save_settings()
        if not self.is_running:
            sleep(2)
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
        else:
            self.is_running = False
            self.Start.configure(text="Wait")
            self.Start.configure(state="disabled")
            crazy.update()
            sleep(30)
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
                    if name == "Facebook Post":
                        bot.get("https://addmefast.com/free_points/facebook_post_like")
                        sleep(1)
                        ed.facebook_post()
                    if name == "Facebook Page":
                        bot.get("https://addmefast.com/free_points/facebook_likes")
                        sleep(1)
                        ed.facebook_page()
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
            if self.is_running:
                self.crazy.title("                        Crazy Wait 100")
                sleep(100)
                self.crazy.title("                        Crazy")
    def login(self):
        self.bot.find_element(By.NAME, 'login_button').click()
        print("successfully logged in")

    def open(self):
        self.Open.configure(state="disabled")
        print("Lodaing......")
        chrome_options = uc.ChromeOptions()
        pro = "C://Users//kreem//AppData//Local//Google//Chrome//User Data//"
        chrome_options.add_argument("--profile-directory=Profile 2")
        chrome_options.add_argument(f"user-data-dir={pro}")
        self.bot = uc.Chrome(options=chrome_options)
        bot = self.bot
        print("Done")

        bot.get("https://addmefast.com/login")
        sleep(5)
        try:ed.login()
        except:
            try:
                ed.Bypass_Cloudflare()
                sleep(2)
                try:ed.login() 
                except:print("successfully logged in")
            except:print("successfully logged in")
        
        self.Start.configure(state="normal")
        self.Close.configure(state="normal")
    def facebook_post(self):
        while self.is_running:
            bot = self.bot 
            try:
                try:  WebDriverWait(bot,5).until(EC.presence_of_element_located((By.LINK_TEXT, "Like"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,5).until(EC.presence_of_element_located((By.LINK_TEXT, "Like"))).click()
                            ed.facebook_post() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])  
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.facebook_post() 
                    break
                try:
                    url = bot.current_url
                    Like(url,"Like",self.cookie).Start()
                except:
                    ed.Telgram(self.Facebook_text)
                    self.Confirm()
                    ed.facebook_post()
                    break
                ed.Confirm()
                ed.facebook_post()
                break
            except : 
                try: ed.Bypass_Cloudflare() ; ed.facebook_post() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.facebook_post()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break                
    def facebook_page(self):
        while self.is_running:
            bot = self.bot 
            try:
                try:  WebDriverWait(bot,5).until(EC.presence_of_element_located((By.LINK_TEXT, "Like/Follow"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,5).until(EC.presence_of_element_located((By.LINK_TEXT, "Like/Follow"))).click()
                            ed.facebook_page() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])  
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.facebook_page() 
                    break
                try:
                    url = bot.current_url
                    Follow(url,self.cookie).Start()
                except:
                    ed.Telgram(self.Facebook_text)
                    self.Confirm()
                    ed.facebook_page()
                    break
                ed.Confirm()
                ed.facebook_page()
                break
            except : 
                try: ed.Bypass_Cloudflare() ; ed.facebook_page() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.facebook_page()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break               
    def facebook_Share(self):
        while self.is_running :
            bot = self.bot
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Share"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Share")))
                            ed.facebook_Share() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])  
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.facebook_Share() 
                    break
                try:
                    url = bot.current_url
                    Share(url,'',self.cookie).Start()
                except :

                    ed.Telgram(self.Facebook_text)
                    ed.Confirm()
                    ed.facebook_Share()
                    break
                ed.Confirm()
                ed.facebook_Share()
                break
            except : 
                try: ed.Bypass_Cloudflare() ; ed.facebook_Share() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.facebook_Share()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break
                    
    def twiter_Follow(self):
        while self.is_running:
            bot = self.bot 
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Follow"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Follow")))
                            ed.twiter_Follow() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.twiter_Follow() 
                    break
                try:
                    sleep(self.befor)
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span"))).click()
                    sleep(self.after)
                except:
                    self.n += 1
                    if self.n == 2 :
                        ed.Telgram(self.Twitter_text)
                        self.n = 0
                    ed.Confirm()
                    ed.twiter_Follow()
                    break
                self.n = 0
                ed.Confirm()
                ed.twiter_Follow()
                break
            except : 
                try: ed.Bypass_Cloudflare(); ed.twiter_Follow() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.twiter_Follow()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break                   
    def twiter_Retweet(self):
        while self.is_running:
            bot = self.bot 
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Retweet"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Retweet")))
                            ed.twiter_Retweet() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.twiter_Retweet() 
                    break
                try:
                    sleep(self.befor)
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span"))).click()
                    sleep(self.after)
                except:
                    self.n += 1
                    if self.n == 5 :
                        ed.Telgram(self.Twitter_text)
                        self.n = 0 
                    ed.Confirm()
                    ed.twiter_Retweet()
                    break
                self.n = 0
                ed.Confirm()
                ed.twiter_Retweet()
                break
            except : 
                try: ed.Bypass_Cloudflare(); ed.twiter_Retweet() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.twiter_Retweet()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break                   
    def twiter_Like(self):
        while self.is_running:
            bot = self.bot 
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Like"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Like")))
                            ed.twiter_Like() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.twiter_Like()
                    break
                try:
                    sleep(self.befor)
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span"))).click()
                    sleep(self.after)
                except:
                    self.n += 1
                    if self.n == 5 :
                        ed.Telgram(self.Twitter_text)
                        self.n = 0 
                    ed.Confirm()
                    ed.twiter_Like()
                    break
                self.n = 0
                ed.Confirm()
                ed.twiter_Like()
                break
            except : 
                try: ed.Bypass_Cloudflare(); ed.twiter_Like() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.twiter_Like()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break
    def instagram_Follow(self):
        while self.is_running:
            bot = self.bot 
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Follow"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Follow")))
                            ed.instagram_Follow() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])  
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.instagram_Follow()
                    break 
                try:
                    sleep(self.befor)
                    try:WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class=' _acan _acap _acat _aj1- _ap30']"))).click()
                    except :WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='_ap3a _aaco _aacw _aad6 _aade']"))).click()

                    sleep(self.after)
                except:
                    self.n += 1
                    if self.n == 3 :
                        ed.Telgram(self.Insta_text)
                        self.n = 0
                    ed.Confirm()
                    ed.instagram_Follow()
                    break
                self.n = 0
                ed.Confirm()
                ed.instagram_Follow()
                break
            except : 
                try: ed.Bypass_Cloudflare(); ed.instagram_Follow() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.instagram_Follow()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break         
    def instagram_Like(self):
        bot = self.bot 
        while self.is_running:
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Like"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Like")))
                            ed.instagram_Like() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.instagram_Like() 
                    break
                try:
                    sleep(self.befor)
                    try: WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class='xp7jhwk']"))).click()
                    except: WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class='_aamw']"))).click()
                    sleep(self.after)
                except:
                    self.n += 1
                    if self.n == 5 :
                        ed.Telgram(self.Insta_text)
                        self.n = 0     
                    ed.Confirm()
                    ed.instagram_Like()
                    break
                self.n = 0
                ed.Confirm()
                ed.instagram_Like()
                break
            except : 
                try: ed.Bypass_Cloudflare(); ed.instagram_Like() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.instagram_Like()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break
    
    def youtube_subscribe(self):
        while self.is_running :
            bot = self.bot 
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Subscribe"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Subscribe")))
                            ed.youtube_subscribe() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])
                
                sleep(5)
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.youtube_subscribe()
                    break
                try:
                    sleep(self.befor)
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH,
                        '//*[@id="visibility-button"]/ytd-button-renderer'))).click()
                    sleep(1)
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH,
                        '//*[@id="subscribe-button"]/ytd-subscribe-button-renderer'))).click()
                    sleep(self.after)
                except:
                    ed.Confirm()
                    ed.youtube_subscribe()
                    break
                
                ed.Confirm()
                ed.youtube_subscribe()
                break
            except : 
                try: ed.Bypass_Cloudflare() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.youtube_subscribe()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break                   
    def youtube_Like(self):
        bot = self.bot 
        while self.is_running:
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Like"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Like")))
                            ed.youtube_Like() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    bot.refresh()
                    sleep(5)
                    ed.youtube_Like()
                    break
                try:
                    sleep(self.befor)
                    WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH,
                        "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/segmented-like-dislike-button-view-model/yt-smartimation/div/div/like-button-view-model/toggle-button-view-model/button-view-model/button"))).click()
                    sleep(random.randrange(5,10))
                except:
                    self.n += 1
                    if self.n == 1 :
                        ed.Telgram(self.Youtube_text)
                        self.n = 0
                    ed.Confirm()
                    ed.youtube_Like()
                    break
                self.n = 0
                ed.Confirm()
                ed.youtube_Like()
                break
            except : 
                try: ed.Bypass_Cloudflare() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.youtube_Like()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break
                    
    def pinterest_followers(self):
        bot = self.bot 
        while self.is_running:
            try:
                try: WebDriverWait(bot, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Follow"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Follow")))
                            ed.pinterest_followers() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.pinterest_followers()
                    break
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Follow')]"))).click()
                    sleep(self.after)
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
                try: ed.Bypass_Cloudflare() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.pinterest_followers()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break                   
    def pinterest_save(self):
        bot = self.bot 
        while self.is_running:
            try:
                try: WebDriverWait(bot, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Save"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Save")))
                            ed.pinterest_save() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.pinterest_save()
                    break
                try:
                    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Profile')]"))).click()
                    sleep(1)
                    try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save')]"))).click() ;sleep(self.after)
                    except: pass    
                except:
                    bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.pinterest_save()
                    break
                self.n = 0 
                bot.close()
                bot.switch_to.window(bot.window_handles[0])
                sleep(5)
                ed.pinterest_save()
                break
            except : 
                try: ed.Bypass_Cloudflare() ;break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.pinterest_save()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break
    
    def tiktok_Follow(self):
        while self.is_running:
            bot = self.bot 
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Follow"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Follow")))
                            ed.tiktok_Follow() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])
                bot.minimize_window()
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.tiktok_Follow()
                    break
                try:
                    # sleep(self.befor)
                    # WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-e2e='follow-button']"))).click()
                    # sleep(random.randrange(5,10))
                    url = bot.current_url
                    requests.post(f'https://api.telegram.org/bot{self.api_token}/sendMessage', json={'chat_id': self.chat_id, 'text': url})
                    username = re.search(r'@(\w+)', url).group(0)
                    Tiktok(username).mainloop()
                    sleep(10)
                except:
                    self.bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.tiktok_Follow()
                    break
                self.bot.close()
                bot.switch_to.window(bot.window_handles[0])
                sleep(5)
                ed.tiktok_Follow()
                break
            except : 
                try: ed.Bypass_Cloudflare() ; ed.tiktok_Follow() ;break
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    ed.tiktok_Follow()
                    break
    def tiktok_like(self):
        while self.is_running:
            bot = self.bot 
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Like"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Like")))
                            ed.tiktok_like() 
                            break
                        except: ed.Check_items() ;break
                bot.switch_to.window(bot.window_handles[1])
                bot.minimize_window()
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.tiktok_like()
                    break
                try:
                    url = bot.current_url
                    requests.post(f'https://api.telegram.org/bot{self.api_token}/sendMessage', json={'chat_id': self.chat_id, 'text': url})
                    username = re.search(r'@(\w+)', url).group(0)
                    Tiktok(username).mainloop()
                    sleep(5)
                except:
                    self.bot.close()
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.tiktok_like()
                    break
                self.bot.close()
                bot.switch_to.window(bot.window_handles[0])
                sleep(5)
                ed.tiktok_like()
                break
            except : 
                try: ed.Bypass_Cloudflare(); ed.tiktok_like() ;break
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    ed.tiktok_like()
                    break
    
    def reddit_Upvote(self):
        while self.is_running:
            bot = self.bot 
            try:
                try: WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Upvote"))).click()
                except:
                    try: ed.Check_page()
                    except :
                        try:
                            bot.refresh()
                            WebDriverWait(bot,10).until(EC.presence_of_element_located((By.LINK_TEXT, "Upvote")))
                            ed.reddit_Upvote() 
                            break
                        except: ed.Check_items() ; break
                bot.switch_to.window(bot.window_handles[1])
                try: WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, "//body")))
                except:
                    bot.switch_to.window(bot.window_handles[0])
                    sleep(5)
                    ed.reddit_Upvote()
                    break
                
                try:
                    sleep(self.befor)
                    try : WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[1]/div/div[1]/div/button[1]/span"))).click()
                    except : WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/shreddit-app/dsa-transparency-modal-provider/report-flow-provider/div/main/shreddit-post//div[2]/span/span/button[1]/span"))).click()
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
                try: ed.Bypass_Cloudflare() ; ed.reddit_Upvote() ; break
                except:
                    try:
                        ed.Check_items1()
                        bot.refresh()
                        ed.reddit_Upvote()
                        break
                    except:
                        ed.Telgram(self.text2)
                        break


    def Bypass_Cloudflare(self):
        a = 0
        WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/iframe")))
        ed.position()
        for _ in range(2):
            if int(self.radio_var.get()) == 1:
                pyautogui.leftClick(290, 18, 1)
                sleep(2)
                pyautogui.leftClick(71, 101, 1)
                sleep(2)
                pyautogui.leftClick(71, 101, 1)
                sleep(10)
                pyautogui.leftClick(45, 375, 1)
                sleep(10)
                self.bot.switch_to.window(self.bot.window_handles[1])
                self.bot.close()
                self.bot.switch_to.window(self.bot.window_handles[0])
                sleep(5)
                self.bot.refresh()
                try:
                    WebDriverWait(self.bot, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/iframe")))
                    a += 1
                except: self.bot.switch_to.window(self.bot.window_handles[0]) ;break
        if a == 2:
            ed.Telgram(self.text1)
            input("Error Cloudflare.........")
        
    # def Bonus(self):
    #     bot = self.bot
    #     if  self.is_running:
    #         bot.execute_script("window.open()")

    #         bot.switch_to.window(bot.window_handles[-1])
    #         bot.get("https://addmefast.com/bonus_points")
    #         try:
    #             subscribe = WebDriverWait(bot, 10).until(
    #                         EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[3]/center/div[2]/center/div[3]/input"))
    #                     )
    #             subscribe.click()
    #             bot.close()
    #             bot.switch_to.window(bot.window_handles[0])
    #         except:
    #             print("NO Bonus Today")
    #             bot.close()
    #             bot.switch_to.window(bot.window_handles[0])


    def Check_page(self):
        for _ in range(10):
            self.bot.switch_to.window(self.bot.window_handles[1]) 
            self.bot.close()
            self.bot.switch_to.window(self.bot.window_handles[0])

    def Check_items(self):
        WebDriverWait(self.bot,10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'No items in this network for now. Please try later.')]")))
        sleep(self.dlay)

    def Check_items1(self):
        WebDriverWait(self.bot,10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Unfortunately an error occurred in the system. In order to try again please reload the page.')]")))

    def position(self):
        x, y = pyautogui.position()
        if x == 0 and y == 0:
            ed.Telgram(self.text3)
            input("No.screens......")
    
    def Telgram(self,text):
        url = f'https://api.telegram.org/bot{self.api_token}/sendMessage'
        payload = {'chat_id': self.chat_id, 'text': text}
        response = requests.post(url, json=payload)
        input(f"{text},Enter....")
    def Confirm(self):
        self.bot.close()
        self.bot.switch_to.window(self.bot.window_handles[0])
        WebDriverWait(self.bot, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Confirm"))).click()
        sleep(self.befor)

    def Save_settings(self):
        config = ConfigParser()
        config['contact'] = {
            'Facebook_Post': self.Facebook_Post.get(),
            'Facebook_Page': self.Facebook_Page.get(),
            'Facebook_Share': self.Facebook_Share.get(),
            'Twiter_Follower': self.Twiter_Follower.get(),
            'Twiter_Retweet': self.Twiter_Retweet.get(),
            'Twiter_Like': self.Twiter_Like.get(),
            'Insta_Follower': self.Insta_Follower.get(),
            'Insta_Like': self.Insta_Like.get(),
            'Youtube_Subscribe': self.Youtube_Subscribe.get(),
            'Youtube_Like': self.Youtube_Like.get(),
            'Pinterest_Follower': self.Pinterest_Follower.get(),
            'Pinterest_Save': self.Pinterest_Save.get(),
            'Tiktok_Follower': self.Tiktok_Follower.get(),
            'Tiktok_Like': self.Tiktok_Like.get(),
            }
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)
    def load_settings(self):
        try:
            config = ConfigParser()
            config.read('settings.ini')
            self.Facebook_Post.set(config.get('contact', 'Facebook_Post'))
            self.Facebook_Page.set(config.get('contact', 'Facebook_Page'))
            self.Facebook_Share.set(config.get('contact', 'Facebook_Share'))
            self.Twiter_Follower.set(config.get('contact', 'Twiter_Follower'))
            self.Twiter_Retweet.set(config.get('contact', 'Twiter_Retweet'))
            self.Twiter_Like.set(config.get('contact', 'Twiter_Like'))
            self.Insta_Follower.set(config.get('contact', 'Insta_Follower'))
            self.Insta_Like.set(config.get('contact', 'Insta_Like'))
            self.Youtube_Subscribe.set(config.get('contact', 'Youtube_Subscribe'))
            self.Youtube_Like.set(config.get('contact', 'Youtube_Like'))
            self.Pinterest_Follower.set(config.get('contact', 'Pinterest_Follower'))
            self.Pinterest_Save.set(config.get('contact', 'Pinterest_Save'))
            self.Tiktok_Follower.set(config.get('contact', 'Tiktok_Follower'))
            self.Tiktok_Like.set(config.get('contact', 'Tiktok_Like'))
            
        except Exception as e:
            pass
            # messagebox.showwarning("Error", f"An error occurred while loading settings:\n{e}") 

    def close (self):
        try:
            self.Save_settings()
            self.bot.quit()
            crazy.destroy()
        except:pass 
if __name__ == '__main__':
    crazy = CTk()
    ed = AMFBot(crazy)
    crazy.mainloop()
>>>>>>> c1b41eab505c6d8dc4721705bfeaee2b5f6164e1:Addmefast/AddMeFast-v2.py
