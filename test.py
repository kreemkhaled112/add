import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = uc.ChromeOptions()
pro = "C://Users//kreem//AppData//Local//Google//Chrome//User Data//"
options.add_argument("--profile-directory=Profile 2")
options.add_argument(f"user-data-dir={pro}")
options.add_argument("--lang=en")
options.add_argument("--start-maximized")
bot = uc.Chrome(options=options,use_subprocess=True)
bot = bot

bot.get("https://www.facebook.com/100057341692405/posts/pfbid02ihrmHkirv6NiRFx9LfceVwWWsUtesb68d621ka14gob8HMXB1Yr5CYCmaC145g8Sl?paipv=0&eav=AfYSoDr6nKkZbB8ePIqeaQFk2t0PDj6YeWElLMZ80weMEWtVU1vSvqS9hQLLM4QN2nw&_rdr")
input(".....")
WebDriverWait(bot, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Like')]"))).click()
# parent_div = driver.find_element_by_class_name('xq8finb')
# like_element = parent_div.find_element_by_xpath('.//div[@aria-label="Like"]')

