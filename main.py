from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from getpass import getpass


def calculate_time(hrs_d,mins_d):
    time.sleep(5)
    timestamp = time.time()
    date_time = datetime.fromtimestamp(timestamp)
    str_time_hr = int( date_time.strftime("%H"))
    str_time_min = int( date_time.strftime("%M"))

    if(mins_d == str_time_min and hrs_d == str_time_hr):
        timePassed=True
    else:
        timePassed=False

    return timePassed

def get_input_time():
    print("Time should be in 24 hour format :)")
    entered_time = str(input('Enter time to send message (hh:mm): '))
    my_time = time.strptime(entered_time, "%H:%M")
    hrs = int(my_time.tm_hour)
    mins = int(my_time.tm_min)
    return hrs,mins



def login(email, password):

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    test_driver = webdriver.Chrome(chrome_options=chrome_options)
    test_driver.get("https://www.facebook.com/messages/t/")

    email_input = test_driver.find_element(By.ID,"email")
    password_input = test_driver.find_element(By.ID,"pass")
    login_button = test_driver.find_element(By.ID,"loginbutton")

    email_input.send_keys(email)
    password_input.send_keys(password)
    login_button.click()


    time.sleep(5)
    Contact=str(input("Enter Name of friend to send message: \n"))
    search_input=test_driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div/div/label/input')
    search_input.send_keys(Contact) 

    time.sleep(5)
    first_account = test_driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]/div/a/div')
    first_account.click()


    time.sleep(5)
    message = str(input("Enter Message: \n"))
    message_text_box = test_driver.find_element(By.CSS_SELECTOR,'.notranslate')
    message_text_box.send_keys(message)

    time.sleep(2)
    inputTime = get_input_time()
    hrs = inputTime[0]
    mins = inputTime[1]

    while(True):
        timePassed = calculate_time(hrs,mins)
        print("False Case")
        if(timePassed==True):
            print("True Case")
            press_send_button(test_driver)

            print("Message sent!! :)")
            break


def press_send_button(test_driver):
    send_button = test_driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/span[2]/div')
    send_button.click()




def get_user_login_data():
    email = input("Enter your username: ")
    password = getpass("Enter your password: ")
    login(email,password)

    

