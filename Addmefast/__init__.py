import requests , random , os , queue ,json , sys , webbrowser , logging , pygame , sqlite3 , re
from customtkinter import *
import undetected_chromedriver as uc
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from os.path import normpath, join
import random 
import pyautogui 
import pyperclip as py
from selenium.webdriver.common.window import WindowTypes
import  urllib
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
from pystyle import *
from threading import Thread
from time import sleep ,time
from pystyle import *
from configparser import ConfigParser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt , pyqtSignal , QThread 
from datetime import datetime


def Header():
    headers = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en,en-US;q=0.9,ar;q=0.8,ar-EG;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.140", "Chromium";v="121.0.6167.140"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }
    return headers


