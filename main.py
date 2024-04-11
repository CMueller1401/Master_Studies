from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

SHEETY_URL = "https://api.sheety.co/ceb4756d9f0d04f989285e96e2232b58/masterStudiengaenge/master"
sheety_headers = {
    "Authorization": "Bearer x6JeBD5br^2wv@",
}

URL = "https://www.studieren-studium.com/master/studieren/Maschinenbau-Deutschland"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_driver = webdriver.Chrome(options=chrome_options)
chrome_driver.get(URL)
time.sleep(3)

while True:
    try:
        button = chrome_driver.find_element(by="css selector", value="#studiengang-list-container-sgf > div.position-relative.mb-7.pe-none > div > button")
    except NoSuchElementException:
        break
    button.send_keys(Keys.ENTER)
    time.sleep(2)

study_names = [study.text for study in chrome_driver.find_elements(by="css selector", value="div div h3 a")]
# print(study_names)
# print(len(study_names))

study_unis = [study.text for study in chrome_driver.find_elements(by="css selector", value="div div div p")]
# print(study_unis)
# print(len(study_unis))

study_information = [study.text for study in chrome_driver.find_elements(by="css selector",
                                                                         value="main div div div div div div div")]
del study_information[0:9]
del study_information[1::3]

study_cities = [city for city in study_information[1::2]]
# print(study_cities)
# print(len(study_cities))

del study_information[1::2]
# print(study_information)
# print(len(study_information))
chrome_driver.quit()

master_studies = {
    "Studienname": study_names,
    "Uni/Hochschule": study_unis,
    "Stadt": study_cities,
    "Master-Info": study_information,
}

master_df = pd.DataFrame(master_studies)
print(master_df)
print(master_studies)

master_df.to_csv("Master.csv", index=False)
