import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

html_doc = """http://18.206.38.144:8000/random_company"""


def webscraper(html_link):
    '''HTML scraper. Analysis of the html web text. Extrapolation of "Name" and "Purpose"
        of the company. it also remove a part of the string to make all the process readle.
        Aim :  get informations from a html text'''
                        
    page = requests.get(html_link)
    soup = BeautifulSoup(page.content, "html.parser")          
    li_line_name = soup.find_all('li')[0].get_text() 
    li_line_name = li_line_name.lstrip('Name: ') 
    li_line_purpose = soup.find(text = re.compile("Purpose"))
    li_line_purpose = li_line_purpose.lstrip('Purpose: ')
    dataset = {"NAME_company": li_line_name, "PURPOSE_company": li_line_purpose}
    return dataset

Data_final = pd.DataFrame(data= None, columns = ['NAME_company', 'PURPOSE_company'], index = range(0,50))

for i in range(0, 50):
    Data_final.iloc[i] = webscraper(html_doc)

print(Data_final)

# Data_final.to_csv('HTML_Scapper_FForner.csv')

if __name__ == "__main__":
    pass
    