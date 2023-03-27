import sqlite3
import undetected_chromedriver as uc
from bs4 import BeautifulSoup

test_url = 'https://tgstat.ru/channel/@rian_ru'




class Parser:
    # TODO сделать проверку на валидность
    def write_tgstat_to_html(self, url_channel):
        self.driver = uc.Chrome(suppress_welcome=False, headless=True)
        self.driver.get(url_channel + '/stat')

        with open('html_file/page_tgstat.html', 'w') as file:
            file.write(self.driver.page_source)

        self.driver.quit()

    def write_tgstat_traffic_to_html(self, url_channel):
        self.driver = uc.Chrome(suppress_welcome=False, headless=True)
        self.driver.get(url_channel + '/stat/external-traffic')

        with open('html_file/page_tgstat_traffic.html', 'w') as file:
            file.write(self.driver.page_source)

        self.driver.quit()

    def scrap_subscribes_count_channel(self):
        """Функция парсит колличество подписчиков канала"""
        with open('html_file/page_tgstat.html') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')
        list_pars = soup.find('div', class_='row justify-content-center mb-n3').find_all('h2')
        subscribes = []
        for i in list_pars:
            subscribes.append(i.text.strip())
        return subscribes[0]

    def scrap_cpm_channel(self):
        """Функция парсит CPM"""
        with open('html_file/page_tgstat.html') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')
        list_pars = soup.find('div', class_='row justify-content-center mb-n3').find_all('h2')
        cpm = []

        for i in list_pars:
            cpm.append(i.text.strip())
        return cpm[3]

    def scrap_err_channel(self):
        """Функция парсит ERR"""
        with open('html_file/page_tgstat.html') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')
        list_pars = soup.find('div', class_='row mt-2').find_all('b')
        err = []

        for i in list_pars:
            err.append(i.text.strip())
        return err[1].strip('%')

    def scrap_coverage_channel(self):
        """Функция парсит ERR"""
        with open('html_file/page_tgstat.html') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')
        list_pars = soup.find('div', class_='row justify-content-center mb-n3').find_all('h2')
        coverage = []

        for i in list_pars:
            coverage.append(i.text.strip())
        return coverage[2]

    def scrap_geo(self, url_channel):

        with open('html_file/page_tgstat_traffic.html') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')
        list_pars_1 = soup.find('div', class_='col-12 col-sm-6').find_all('div', class_='col col-8')
        list_pars_2 = soup.find('div', class_='col-12 col-sm-6').find_all('div', class_='col col-4 text-right font-12')
        lst_1 = []
        lst_2 = []
        final_lst = []

        for i in list_pars_2:
            lst_2.append(i.text.strip().replace(' %', ''))

        for i in list_pars_1:
            lst_1.append(i.text.strip())

        for index, lst in enumerate(lst_1):
            final_lst.append(lst)
            final_lst.append(lst_2[index])
        return final_lst

    def clear_page_tgstat_html(self):
        with open('html_file/page_tgstat.html', 'w') as file:
            file.write('')






