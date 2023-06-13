from bs4 import BeautifulSoup
import requests
from datetime import datetime
from selenium import webdriver

driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver")
driver.implicitly_wait(3)
driver.get("https://www.daum.net")
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
results = soup.findAll("a", "link_favorsch")

search_rank_file = open("rankresult.txt","a")

rank = 1

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1
