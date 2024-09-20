import sys
import os

path_to_add = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..','.'))
print(path_to_add)
sys.path.append(path_to_add)

from FUNCTIONS.Get_User_Input import *
from FUNCTIONS.Create_Name import *
from FUNCTIONS.Create_PhoneNum import *
from FUNCTIONS.Create_CPF import *

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
import multiprocessing

load_dotenv()

def login(wait, driver):    
    email_input = wait.until(EC.element_to_be_clickable((By.NAME, 'email')))
    email_input.clear()
    email_input.send_keys(os.getenv('EMAIL'))
    
    password_input = wait.until(EC.element_to_be_clickable((By.NAME, 'password')))
    password_input.clear()
    password_input.send_keys(os.getenv('PASSWORD'))
    
    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/form/button'))).click()
    
    time.sleep(3)
   
def clients_page(wait):
    clients_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/header/nav/div[1]/div/ul/li[2]'))).click()
    
def new_client(wait, client_amount):
    
    for _ in range(client_amount):
        add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div[1]/div[2]/button[2]'))).click()

        name_input = wait.until(EC.element_to_be_clickable((By.NAME, 'clientName'))).send_keys(create_random_name())
        
        email_input = wait.until(EC.element_to_be_clickable((By.NAME, 'clientEmail'))).send_keys(create_random_email())
        
        cpf_input = wait.until(EC.element_to_be_clickable((By.NAME, 'docValue'))).send_keys(gera_e_valida_cpf())
        
        phone_input = wait.until(EC.element_to_be_clickable((By.NAME, 'phoneValue'))).send_keys(create_phone())
        
        info_input = wait.until(EC.element_to_be_clickable((By.NAME, 'clientInfo'))).send_keys(create_text(999))
        
        create_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div[5]/div/div/div[2]/form/div[6]/button[2]'))).click()
    
        time.sleep(3)
 
def create_user(client_amount):
    driver_path = u'selenium_tests\chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s) 
    driver.get(os.getenv('URL'))
    wait = WebDriverWait(driver, 5)
    driver.fullscreen_window()
    
    login(wait, driver)
    
    clients_page(wait)
    
    new_client(wait, client_amount)
    
    time.sleep(3)
    
    driver.quit()
    
def main():
    num_processes = int(get_user_input("How many users to simulate?"))

    client_amount = int(get_user_input("How many clients?"))

    processes = []
    for _ in range(num_processes):
        p = multiprocessing.Process(target=create_user, args=(client_amount,))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    main()