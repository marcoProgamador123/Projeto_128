from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
#from selenium.webdriver.chrome.service import Service
#service = Service('path/to/chromedriver.exe')
#service.start()

#browser = webdriver.Chrome(service=service)
# selenium 4
# from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# URL dos Exoplanetas da NASA
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser.get(START_URL)

time.sleep(10)

scarped_data = []


def scraped():
        # Objeto BeautifulSoup
       
        # page_source obtem o código da pagina html
        # html.parser extrai o conteúdo das tags html
        page = requests.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")
        
        soup = BeautifulSoup(page.content,"html.parser")
        
        tables = soup.find("table",attrs={'class','wikitable'})
        
        table = tables.find("tbody")
            
        table_rows = table.find_all('tr')
    
        temp_list = []

        # Obetenha os dados de <td>
        for row in table_rows:
            table_cols = row.find_all('td')
            print(table_cols)  
            
            for col_data in table_cols:
               # Remova os espaços em bracos extras 
                data = col_data.text.strip()
             
                temp_list.append(data)
                
            scarped_data.append(temp_list)    
        print(scarped_data)
       
            
scraped()
stars_data = []

for i in range(0,len(scarped_data)):
    Star_names = scarped_data[i][1]
    Distance = scarped_data[i][3]
    Mass = scarped_data[i][5]
    Radius = scarped_data[i][6]
    Lum = scarped_data[i][7]
            
    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)
     
# Defina o cabeçalho
headers = ['Stars_name', 'Distance', 'Mass', 'Radius', 'luminosity']
        
# Defina o dataframe do pandas
star_df_1  = pd.DataFrame(stars_data,columns=headers)
        
# Converta para CSV   
star_df_1.to_csv('new_scraped_data.csv',index = True, index_label = "id") 



      
