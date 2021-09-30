from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import time


def get_kdr():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path='C:/bin/chromedriver.exe', options=chrome_options)

    driver.get("https://na.op.gg/summoner/userName=thefrylocks")
    while True:
        try:
            element = driver.find_element_by_css_selector("#SummonerRefreshButton")
            print("B4 CLICK UPDATED")
            element.click()
            print("CLICKED UPDATED")
            break
        except:
            continue

    while True:
        try:
            uid = driver.find_element_by_css_selector('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.RealContent > div > div.Content > div.GameItemList > div:nth-child(1) > div > div.Content > div.KDA > div.KDARatio > span').text
            kill_amount = driver.find_element_by_css_selector("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.RealContent > div > div.Content > div.GameItemList > div:nth-child(1) > div > div.Content > div.KDA > div.KDA > span.Kill").text
            death_amount = driver.find_element_by_css_selector("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.RealContent > div > div.Content > div.GameItemList > div:nth-child(1) > div > div.Content > div.KDA > div.KDA > span.Death").text
            break
        except:
            continue
    "#SummonerRefreshButton"
    ratio = int(kill_amount)/int(death_amount)
    with open("uid", "w") as f:
        f.write(uid)

    return ratio

if __name__ == "__main__":
    r = get_kdr()
    print(r)