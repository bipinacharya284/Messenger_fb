from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



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



def login(email, password, contact, message):

    """
    This function login into your facebook account.
    DiSCLAMER :: This function only excess the message sending part only.
    Args: 
        email(str): Facebook email/username
        password(str): Facebook password 
        contact(str): This is the friend name to whom the message should be sent
            Note :: 
            1) Contact should be name of only one person.
            2) Top most contact from search list is selected for sending message

        message(str): This is the message that is to be sent.

    """

    # Opening chrome browser and surfing to facebook messaging page
    try:
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        test_driver = webdriver.Chrome(chrome_options=chrome_options)
        test_driver.get("https://www.facebook.com/messages/t/")
    
    except TimeoutException:
        print("Error Loading the webpage")
    finally:

        email_input = test_driver.find_element(By.ID,"email")
        password_input = test_driver.find_element(By.ID,"pass")
        login_button = test_driver.find_element(By.ID,"loginbutton")
        

        email_input.send_keys(email)
        password_input.send_keys(password)
        login_button.click()


    # Search name for the contact
    try:
        search_input= WebDriverWait(test_driver,1000).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div/div/label/input'))) 
        # search_input= test_driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div/div/label/input')
    except TimeoutException:
        print("Error getting friend name from user")
    finally:
        search_input.send_keys(contact) 

        try:
            first_account =WebDriverWait(test_driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]/div/a/div'))) 
        finally:
            first_account.click()


    # Enter message to the text box
    try:
        message_text_box = WebDriverWait(test_driver,1000).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.notranslate'))) 
        # message_text_box = test_driver.find_element(By.CSS_SELECTOR,'.notranslate')
    finally:
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


# Press send button
def press_send_button(test_driver):
    send_button = test_driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/span[2]/div')
    send_button.click()




def get_user_login_data():
    email = input("Enter your username: ")
    password = getpass("Enter your password: ")
    friendName = input("Enter your Friend's Name to send Message: ")
    message = input("Enter your message to send : ")
    login(email,password,friendName,message)

get_user_login_data()

