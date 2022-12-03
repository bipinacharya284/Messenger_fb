from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime

timePassed=False

entered_time = str(input('Enter time(hh:mm): '))
my_time = time.strptime(entered_time, "%H:%M")
hrs = int(my_time.tm_hour)
mins = int(my_time.tm_min)
# print(my_time.tm_hour,my_time.tm_min)



def calculate_time(hrs_d,mins_d):
    
    timestamp = time.time()
    date_time = datetime.fromtimestamp(timestamp)
    str_time_hr = int( date_time.strftime("%H"))
    str_time_min = int( date_time.strftime("%M"))

    # print(str_time_hr)
    # print(str_time_min)

    if(mins_d == str_time_min and hrs_d == str_time_hr):
        timePassed=True
        return timePassed
    


def send_message(): 

    test_driver = webdriver.Chrome()

    test_driver.get("https://www.facebook.com/messages/t/")

    email_input = test_driver.find_element(By.ID,"email")
    password_input = test_driver.find_element(By.ID,"pass")
    login_button = test_driver.find_element(By.ID,"loginbutton")

    email = "bipinacharya284@gmail.com"
    password = "Letsseetheuniverse0811"

    email_input.send_keys(email)
    password_input.send_keys(password)
    login_button.click()

    time.sleep(10)
    Contact=str(input("Enter Name: \n"))
    search_input=test_driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div/div/label/input')
    search_input.send_keys(Contact) 

    time.sleep(3)
    first_account = test_driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]/div/a/div')
    first_account.click()

    time.sleep(3)
    message = str(input("Enter Message: \n"))
    message_text_box = test_driver.find_element(By.CSS_SELECTOR,'.notranslate')
    message_text_box.send_keys(message)

    time.sleep(3)
    send_button = test_driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/span[2]/div')
    send_button.click()

    print("Message Send Successfully")
        




while(True):
    time.sleep(5)
    timePassed = calculate_time(hrs,mins)
    print(timePassed)
    if(timePassed==True):
        break

send_message()




