from bs4 import BeautifulSoup
import requests
from datetime import datetime

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"}
url = "https://www.skku.edu/skku/index.do"
response = requests.get(url, headers=headers) 
soup = BeautifulSoup(response.text, "html.parser")
results = soup.findAll("span", "headLIneDesc")   
rank = 1

search_rank_file = open("rankresult.txt","a")

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1
