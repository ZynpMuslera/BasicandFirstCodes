import requests
from bs4 import BeautifulSoup
import sys

url="https://www.boxofficemojo.com/chart/ww_top_lifetime_gross/?area=XWW&ref_=bo_cso_ac"
response=requests.get(url)

html_content= response.content
soup= BeautifulSoup(html_content,"html.parser")

worldwide= input("Please write the movie which you want to see its gross : ")

movies=soup.find_all("td",{"class":"a-text-left mojo-field-type-title"})
gross=soup.find_all("td",{"class":"a-text-right mojo-field-type-money"})

for movie,gro in zip(movies,gross):
    movie=movie.text
    gro=gro.text
    if worldwide==movie:
        print("Movie Gross is: ",gro)
        break
    else:
        sys.stderr.write("Please write the name of the movie correctly")
        sys.stderr.flush()
        break
