# Libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

###Set the link
html_doc = """http://18.206.38.144:8000/random_company"""


###function creation
def webscraper (html_link):
    '''HTML scraper. Analysis of the html web text. Extrapolation of "Name" and "Purpose"
        of the company. it also remove a part of the string to make all the process readle.
        Aim :  get informations from a html text'''
                        
    page = requests.get(html_link) #get request
    # print(f"Response  {page}")    #get the URL                   
    # print(f"Status page: {page.status_code}") #find response and status page

    # print(f"Page text: {page.text} \n") #find all the text of the page
    soup = BeautifulSoup(page.content, "html.parser") #analys the content of the page as html script

    ###find Name
    # print(f"find all the <li> phrase: {li_line} \n") #get all the purpose to undestand how it works              
    li_line_name = soup.find_all('li')[0].get_text() 
    li_line_name = li_line_name.lstrip('Name: ') #remove what you don't need from the string
    # print(f"Find Names: {li_line_name}")
    
    ###find Purpose
    li_line_purpose = soup.find(text = re.compile("Purpose"))
    li_line_purpose = li_line_purpose.lstrip('Purpose: ') #remove what you don't need from the string
    # print(f"Find Purpose: {li_line_purpose}\n")
    
    ###Save data inside a data set
    dataset = {"NAME_company": li_line_name, "PURPOSE_company": li_line_purpose}
    # print(f"Save result in dictionary:\n {dataset}") # save the result in a dictionari
    return dataset

### does it work?
#print(f"Function created: {webscraper(html_doc)}") 

Data_final = pd.DataFrame(data= None, columns = ['NAME_company', 'PURPOSE_company'], index = range(0,50)) #empty dataframe

###loop for etracting 50 times NAME and PURPOSE
for i in range(0, 50):
    Data_final.iloc[i] = webscraper(html_doc) #insert dictionary in the dataframe 

print(Data_final)


### Download the file in cvs form
# Data_final.to_csv('HTML_Scapper_FForner.csv')
