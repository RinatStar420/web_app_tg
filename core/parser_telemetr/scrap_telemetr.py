from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time



from bs4 import BeautifulSoup





test_url = 'https://telemetr.me/@novosti_voinaa'
test_email = 'rinatlucke@gmail.com'
test_password = '@.$LqJAfGHR@pz3'


class Parser_telemetr:
    def write_telemetr_to_html(self, url_channel, test_email, test_password):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get(url_channel)



        login = self.driver.find_element(By.XPATH, '//*[@id="btn_auth"]')
        login.click()

        email = self.driver.find_element(By.XPATH,'//*[@id="modal_auth"]/div/div/div[2]/form/div[1]/input')
        email.send_keys(test_email)

        password = self.driver.find_element(By.XPATH,'//*[@id="modal_auth"]/div/div/div[2]/form/div[2]/input')
        password.send_keys(test_password)

        button_login = self.driver.find_element(By.XPATH, '//*[@id="modal_auth"]/div/div/div[2]/form/button')
        button_login.click()

        time.sleep(7)

        with open('html_file/page_telemetr.html', 'w') as file:
            file.write(self.driver.page_source)

        self.driver.quit()


    def get_gender(self):
        with open('html_file/page_telemetr.html') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')
        list_pars = soup.find('span', class_='kt-widget__value').text
        gender = []
        gender.append(list_pars[4:8])
        gender.append(list_pars[15:18])

        # первое значение мужчина, второе значение женщина !!! прочитай !!!
        return gender

    def clear_page_telemetr_html(self):
        with open('html_file/page_tgstat_traffic.html', 'w') as file:
            file.write('')

