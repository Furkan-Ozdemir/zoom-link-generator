import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import tkinter as tk


class ZoomBot:
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path="D:\\PythonProjects\\zoom-link\\chromedriver.exe"
        )

    def go_to_temp_mailer(self):
        self.driver.get("https://www.temporary-mail.net/")
        self.driver.find_element_by_xpath('//*[@id="active-mail"]').click()

    def go_to_zoom(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://zoom.us/signup")

    def init_zoom_account(self):
        self.driver.find_element_by_xpath('//*[@id="select-0"]').click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="select-item-select-0-0"]/span[2]')
            )
        )
        self.driver.find_element_by_xpath(
            '//*[@id="select-item-select-0-0"]/span[2]'
        ).click()
        self.driver.find_element_by_xpath('//*[@id="select-1"]').click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="select-item-select-1-0"]'))
        )
        self.driver.find_element_by_xpath('//*[@id="select-item-select-1-0"]').click()
        self.driver.find_element_by_xpath('//*[@id="select-2"]').click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="select-item-select-2-0"]/span[2]')
            )
        )
        self.driver.find_element_by_xpath(
            '//*[@id="select-item-select-2-0"]/span[2]'
        ).click()
        self.driver.find_element_by_xpath(
            '//*[@id="age_gating_question"]/div/div[3]/button'
        ).click()

        email_input = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_input.send_keys(Keys.CONTROL, "v")
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="signup-button"]').click()

    def activate_zoom_account(self):
        WebDriverWait(self.driver, 180).until(
            EC.url_to_be("https://zoom.us/emailsent?entry=signup")
        )
        self.driver.switch_to.window(self.driver.window_handles[0])
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="message-list"]/tr[1]/td[2]/a')
            )
        )
        self.driver.find_element_by_xpath(
            '//*[@id="message-list"]/tr[1]/td[3]/a/span'
        ).click()
        WebDriverWait(self.driver, 40).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="main"]/div/div/div[2]/div['
                    "1]/div/div["
                    "3]/table/tbody/tr/td/table/tbody/tr["
                    "4]/td/table/tbody/tr/td/strong/a",
                )
            )
        )
        self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div/div[2]/div[1]/div/div[3]/table/tbody/tr/td/table/tbody/tr['
            "4]/td/table/tbody/tr/td/strong/a"
        ).click()

    def fill_credentials(self):
        self.driver.find_element_by_xpath('//*[@id="firstName"]').send_keys("deneme")
        self.driver.find_element_by_xpath('//*[@id="lastName"]').send_keys("dneme")
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(
            "L+=b}Cv{['4V{hS"
        )
        self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(
            "L+=b}Cv{['4V{hS"
        )
        WebDriverWait(self.driver, 180).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/button/span',
                )
            )
        )
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/button/span'
        ).click()

    def start_meeting(self):
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div[2]/div/div[1]/div[1]/div[2]/a'
        ).click()


def main():
    bot = ZoomBot()
    bot.go_to_temp_mailer()
    bot.go_to_zoom()
    bot.init_zoom_account()
    # bot.activate_zoom_account()
    # bot.fill_credentials()
    # bot.start_meeting()
    time.sleep(60)


# root = tk.Tk()
# canvas1 = tk.Canvas(root, width=300, height=300)
# canvas1.pack()
# button1 = tk.Button(text="Click Me", command=main, bg="brown", fg="white")
# canvas1.create_window(150, 150, window=button1)
# root.mainloop()
main()