from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import request

# URL dos Exoplanetas da NASA
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = webdriver.Chrome(
    "D:\Documentos\BYJUS\AulasVScode\Aulas\Alunos\Aluno 0\Python\Aula127&128\chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scarped_data = []


def scraped():
        # Objeto BeautifulSoup
        soup = BeautifulSoup(browser.page_source, "html.parser")
        # page_source obtem o código da pagina html
        # html.parser extrai o conteúdo das tags html
         
        bright_star_table = soup.find("table", attrs={"class", "wikitable"})

        table_body = bright_star_table.find("tbody")
            
        table_rows = table_body.find_all('tr')
        
        

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
star_df_1.to_csv('scraped_data.csv',index = True, index_label = "id") 



      
