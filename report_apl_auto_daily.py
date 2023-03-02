"""
Created on Friday June, 25 21:22:16 2021
last updated september 23,  2021
Automation App: Data Extract / Ingestion Sales & Stock APL Data
@author: Rivo Henfri Wowiling
"""
from selenium import webdriver
import time
import os
from datetime import datetime
import pyautogui as py
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import sys
import logging
from logging.config import dictConfig
import urllib
from urllib.request import urlopen
from decouple import config
#logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
timestamp = datetime.now().strftime("%H:%M:%S")
#init setup selenium library - buat auto download report APL
driver= webdriver.Chrome(config('WEB_DRIVER')) #call library wedriver selenium chrome
#init setup user credential
username = config('USER_ID')
password = config('USER_PASSWORD')
#set define link reporting APL Custom dashboard
url_sales_report = config('URL_SALES')
url_stock_report = config('URL_STOCK')
#init setup: cek-internet-connection
def is_connected():
    try:
        urlopen('https://ziplivephid.zuelligpharma.com',timeout=1)
        return True
    except urllib.error.URLError as Error:#OSError:
        print(Error)
        #pass
        return False
if is_connected():
    print("init status code https..")
    print(urllib.request.urlopen("https://ziplivephid.zuelligpharma.com").getcode())
    print("Sipp...Koneksi internet aman!")
else:
    print("wah kayaknya ada masalah koneksi atau portal nya problem nih...gak bisa masuk ke portal APL..")
    print(Error)
#init setup: pyautogui handling mouse
py.FAILSAFE = False
#open sales report driver selenium
driver.get(url_sales_report) #open sales report
while True:
    logo = py.locateCenterOnScreen('A:\\APL_App\\img_rec\\init-logo.png') 
    if logo is not None:
        break
print("init login page...")
print(logo)
def login_sales_report():
    usernameInput=driver.find_element_by_id("userNameInput")
    usernameInput.send_keys(username)
    passw=driver.find_element_by_id("passwordInput")
    passw.send_keys(password)
    print("input username dan password sukses..")
    signin=driver.find_element_by_id("submitButton")
    signin.click()
    print("klik login sales report")
def init():
    time.sleep(10)
    while True:
        init=py.locateCenterOnScreen('A:\\APL_App\\img_rec\\init.png')
        #py.click(init)
        #py.move(177,322,2)
        py.click(177,322)
        if init is not None:
            break
    print(init)
def download_sales_daily():
    init()
    time.sleep(5)
    #click billing date 
    py.click(901,350)
    #click billing date > all
    py.click(712,392)
    #click billing data > apply
    py.click(865,689)
    #click_dowload
    while True:
        #click_updated_text_screen
        py.click(166,400)
        #time.sleep(5)
        wait_download = py.locateCenterOnScreen('A:\\APL_App\\img_rec\\init-download-branch.png')
        time.sleep(5)
        if wait_download is not None:
            py.click(166,400)
            py.click(820,195)
            time.sleep(5)
            print(wait_download)
            break
        else:
            print("init & waiting to download process ..")
    #click csv format download > data
    py.click(543,424)
    print("process click data sales csv format")
    #click download > view data > click download
    time.sleep(10)
    py.click(195,236)
    print("download daily sales (all) csv report success")
#flow download stock daily
def click_daily_stock():
    init()
    #Point(x=268, y=220)
    py.click(268,220)  
    time.sleep(5)
    #click disable download bottom bar
    py.click(1038,686)
def download_stock_daily():
    click_daily_stock()
    #time.sleep(5)
    #click_dowload
    while True:
        #click_updated_text_screen
        py.click(159,401)
        #time.sleep(5)
        wait_download1 = py.locateCenterOnScreen('A:\\APL_App\\img_rec\\init-download-item-stok.png')
        time.sleep(5)
        if wait_download1 is not None:
            py.click(822,205)
            time.sleep(5)
            print(wait_download1)
            break
        else:
            print("init & waiting to stock download process ..")
    #click csv format
    py.click(531,422)
    print("process click data stok csv format")
    #click > view data > click download
    time.sleep(10)
    py.click(169,232)
    print("downloaded Data csv daily H-1 stock report success")
#run function
login_sales_report()
print("berhasil login ...ke dashboard sales report...")
download_sales_daily()
print("berhasil download daily (select all) sales...")
download_stock_daily()
print("berhasil download daily stock by Date..")
time.sleep(30) 
driver.close()
driver.quit()
