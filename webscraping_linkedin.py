
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.linkedin.com/")

# Localizando o botão de jobs
jobs_botao = driver.find_element(By.XPATH, "/html/body/nav/ul/li[4]/a")
jobs_botao.click()
job_title = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/section/section[2]/form/section[1]/input")
job_title.click()
job_title.send_keys("Cientista de dados")
job_location = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/section/section[2]/form/section[2]/input")
job_location.click()
job_location.clear()
job_location.send_keys("Rio de janeiro")
job_location.send_keys(Keys.ARROW_DOWN)
job_location.send_keys(Keys.RETURN)
job_cards = driver.find_elements(By.CLASS_NAME, 'base-card')


# Colocando tudo em um local só
table = pd.DataFrame(columns=["Company","Job_Description","Level"]) # Criando o Dataframde




for job in range(len(job_cards)):
    job_cards[job].click()
    sleep(2)
    job_description = driver.find_element(By.CLASS_NAME, "show-more-less-html__markup").text
    sleep(1)
    job_level = driver.find_element(By.CLASS_NAME, 
                                    "description__job-criteria-text.description__job-criteria-text--criteria").text
    sleep(2)
    try:
        company = driver.find_element(By.CLASS_NAME, "topcard__org-name-link.topcard__flavor--black-link").text
    except:
        company = driver.find_element(By.CLASS_NAME, "topcard__flavor").text
    
    lista = [company,job_description,job_level]
    table = table.append({"Company": company,"Job_Description":job_description,
                    "Level":job_level}, ignore_index=True)



driver.close()

table.to_csv("jobs_RJ.csv", index=False)







# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




