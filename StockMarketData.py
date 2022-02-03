from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()                  #Creates a headless browser
chrome_options.add_argument("--headless")

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH, chrome_options=chrome_options)


def start():
    while True:

        user_start = input('Ticker: ')
        driver.get(f"https://finance.yahoo.com/quote/{user_start}?p={user_start}&.tsrc=fin-srch")
        commands = ['/price - Gives current price', '/marketcap - Gives Current Market Cap','/volume - Gives current trading volume']
        print(commands)
        user_option = input('Please type a command: ')

        if user_option == '/price':
            price = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[5]/div/div/div/div[3]/div[1]/div[1]/fin-streamer[1]')
            print(f'Current Price is {price.text}')

        if user_option == '/marketcap':
            cap = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[2]')
            print(f'Market cap is {cap.text}')

        if user_option == '/volume':
            vol = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[7]/td[2]')
            print(f'Volume is {vol.text}')

start()












