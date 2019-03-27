import threading
import traceback
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from insta_login import *
from insta_window import *
from bs4 import BeautifulSoup as bs
import requests


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
base_url = 'https://hypeauditor.com/top-instagram-all-ukraine/?p={page_num}'

def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    text += ''.join(traceback.format_tb(tb))
    print(text)
    QtWidgets.QMessageBox.critical(None, 'Error', text)
    sys.exit()
sys.excepthook = log_uncaught_exceptions


class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None): # Показывает форму авторизации
        QtWidgets.QWidget.__init__(self, parent)
        self.secondWin = None
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.pushButton_clicked)
        self.MyWin = []


    def pushButton_clicked(self,): # Запускает Chrome Browser
        self.driver = webdriver.Chrome()
        self.driver.set_window_position(-7, 0)
        self.driver.set_window_size(640, 772)
        self.wait = WebDriverWait(self.driver, 22)
        self.login()


    def login(self): # Авторизации пользователя
        username = 'anna_kanswer'
        password = '4005001610lm'
        #username = self.ui.lineEdit.text()
        #password = self.ui.lineEdit_2.text()
        self.driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        self.emailbox = self.driver.find_element_by_xpath("//input[@name='username']")
        self.emailbox.send_keys(username)
        self.passbox = self.driver.find_element_by_xpath("//input[@name='password']")
        self.passbox.send_keys(password)
        self.passbox.send_keys(Keys.RETURN)
        time.sleep(2)
        self.check_error_login()


    def check_error_login(self):# Выводит сообщение о неверной авторизации
        try:
            self.driver.find_element_by_id('slfErrorAlert')
        except:
            windownum = self.ui.lineEdit_3.text()
            if windownum != 0:
                if self.MyWin != '':
                    self.close()
            self.openWin2()
            self.bloggers_username_pars()
            return True
        return self.ui.lineEdit_3.setText('Неверный Логин или Пароль'),self.driver.quit()


    def openWin2(self):# Открывает Окно Пользователей
        if not self.secondWin:
            self.secondWin = MyWin2(self)
        self.secondWin.show()


    def thread(fn):# Запускает Второй Поток
        def execute(*args, **kwargs):
            threading.Thread(target=fn, args=args, kwargs=kwargs).start()
        return execute


    @thread
    def bloggers_username_pars(self):#  Процесс Подписки на Блогеров
        blogger_list = []
        urls = []
        urls.append(base_url)
        session = requests.Session()                          # Парсинг Url Bloggers
        request = session.get(base_url, headers=headers)
        if request.status_code == 200:
            for i in range(1, 4):
                url = f'https://hypeauditor.com/top-instagram-all-ukraine/?p={i}'
                urls.append(url)

            for url in urls:
                request = session.get(url, headers=headers)
                soup = bs(request.content, 'html.parser')
                bloggers_table = soup.find('table', attrs={'id': 'bloggers-top-table'})
                bloggers_info = bloggers_table.find_all('td', attrs={'class': 'bloggers-top-name'})
                for blogger in bloggers_info:
                    bloggername = {'bloggers-top-name': blogger.a.text}
                    blogger_list.append(bloggername['bloggers-top-name'])
                    for url in blogger_list[-1:]:                           # Начало Подписки
                        self.driver.get('https://www.instagram.com/' + url.lstrip('@') + '/')
                        btn_subscr = self.wait.until(
                            EC.presence_of_element_located(
                                (By.XPATH,
                                 "//*[@id='react-root']/section/main/div/header/section/div/span/span/button")))
                        time.sleep(4)
                        btn_subscr.click()
                        try:
                            btn_unsubscr = self.wait.until(
                                EC.presence_of_element_located(
                                    (By.XPATH, "/html/body/div/div/div/div/button")))
                            time.sleep(8)
                            btn_unsubscr.click()
                        except:
                            pass
        else:
            print('ERROR')





class MyWin2(QtWidgets.QMainWindow,):

    def __init__(self, parent=None,):       # Показывает Окно Пользователей
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)





if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    myapp = MyWin()
    myapp.show()
    app.exec_()