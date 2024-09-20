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
import random

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
   
def projects_page(wait):
    project_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/header/nav/div[1]/div/ul/li[4]'))).click()
    
    time.sleep(3)
    
def new_project(wait, proj_ammount, driver):
    
    for _ in range(proj_ammount):
        print(u'\033[43m\033[30mCreating project\033[0m')
        
        add_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div/div[2]/button[2]'))).click()
        
        name_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/form/div/div/div[1]/div/input'))).send_keys(create_random_name(), ' Auto Project')

        phase_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/form/div/div/div[2]/div'))).click()
        
        phase_select = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-fase-option-1"]'))).click()
        
        user_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/form/div/div/div[3]/div/div'))).click()
        
        user_select = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-select-client-option-12"]'))).click()
        
        next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/form/div/button'))).click()
        
        from_zero_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/section/div/div[2]'))).click()
        
        new_user_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[1]/div/button'))).click()
        
        add_new = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/div/div/div[2]/div/button/span'))).click()
        
        add_user_name = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/div/div/div[2]/form/div[1]/div/div/input'))).send_keys('App user')
        
        app_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/div/div/div[2]/form/div[2]/div/div[1]/label/div[2]'))).click()
        
        register_user = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/div/div/div[2]/form/div[3]/button[2]'))).click()
        
        add_screen_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div/div/div[1]/div/div/button[2]'))).click()

        app_qnt = random.randint(1, 10)
        for i in range(app_qnt):
            print('\033[37m\033[40mCreating app screen ', i, '\033[0m')
            time.sleep(2)
            
            add_screen_name = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div[1]/div/div/input'))).send_keys(f'{i} Auto App Screen')
        
            register_screen = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div[2]/button[2]'))).click()
        
            time.sleep(1)
                                                                               
            click_screen = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[1]/div/div[1]/div[{4+i}]/span'))).click()
            
            file_input = driver.find_element(By.ID, f"imageUpload_0_{i}")
            file_input.send_keys(r'C:\Users\josef\Desktop\AutoCRM\image.png')
            
            func_qnt = random.randint(1, 3)
            for j in range(func_qnt):
                print('\033[37m\033[40mCreating app functionality ', j, '\033[0m')
                add_func_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/div[2]/div[2]/div/div[1]/div/button[2]'))).click()
                time.sleep(0.5)
                func_name = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[2]/div[2]/div[2]/div/div[5]/div/div/div[2]/div[1]/input[2]"))).send_keys(f'{j}')
                time.sleep(0.5)
                add_value = wait.until(EC.element_to_be_clickable((By.XPATH, f"/html/body/main/div/div/div[2]/div[2]/div[2]/div/div[5]/div/div[{j+1}]/div[2]/div[1]/div/input"))).send_keys(func_qnt * 999999)
                time.sleep(0.5)                                                                 
                add_func = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[2]/div[2]/div/div[5]/div/div[{j+1}]/div[1]/button[1]'))).click()
                time.sleep(2)
                print('\033[37m\033[40mApp functionality created ', j, '\033[0m')
                
            add_new_screen_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/div[1]/div/div[1]/div[1]/button[2]'))).click()
        
        print('\033[37m\033[40mApp screen done\033[0m')
        
        close_window = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/div[1]/div/div[3]'))).click()
        
        new_user_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[1]/div/button'))).click()
        
        add_new = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/div/div[2]/div/button'))).click()
        
        add_user_name = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/div/div[2]/form/div[1]/div/div/input'))).send_keys('Web user')
        
        web_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/div/div[2]/form/div[2]/div/div[2]/label/div[2]'))).click()
        
        register_user = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/div/div[2]/form/div[3]/button[2]'))).click()
        
        add_screen_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div/div/div[1]/div/div/button[2]'))).click()

        web_qnt = random.randint(1, 10)  
        for i in range(web_qnt):
            print('\033[37m\033[40mCreating web screen ', i, '\033[0m')
            time.sleep(2)
            
            add_screen_name = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div[1]/div/div/input'))).send_keys(f'{i} Auto Web Screen')
        
            register_screen = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div[2]/button[2]'))).click()
        
            time.sleep(1)
                                                                               
            click_screen = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[1]/div/div[1]/div[{4+i}]/span'))).click()
            
            file_input = driver.find_element(By.ID, f"imageUpload_1_{i}")
            file_input.send_keys(r'C:\Users\josef\Desktop\AutoCRM\image.png')
            
            func_qnt = random.randint(1, 3)
            for j in range(func_qnt):
                print('\033[37m\033[40mCreating web functionality ', j, '\033[0m')
                add_func_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/div[2]/div[2]/div/div[1]/div/button[2]'))).click()
                time.sleep(0.5)
                func_name = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[2]/div[2]/div[2]/div/div[5]/div/div/div[2]/div[1]/input[2]"))).send_keys(f'{j}')
                time.sleep(0.5)
                add_value = wait.until(EC.element_to_be_clickable((By.XPATH, f"/html/body/main/div/div/div[2]/div[2]/div[2]/div/div[5]/div/div[{j+1}]/div[2]/div[1]/div/input"))).send_keys(func_qnt * 9999999)
                time.sleep(0.5)                                                                 
                add_func = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[2]/div[2]/div/div[5]/div/div[{j+1}]/div[1]/button[1]'))).click()
                time.sleep(2)
                print('\033[37m\033[40mApp functionality created ', j, '\033[0m')
                
            add_new_screen_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/div[1]/div/div[1]/div[1]/button[2]'))).click()
    
        print('\033[37m\033[40mWeb screen done\033[0m')
    
        close_window = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/div[1]/div/div[3]'))).click()
        
        new_user_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[1]/div/button'))).click()
        
        add_new = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/div/div[2]/div/button'))).click()
        
        add_user_name = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/div/div[2]/form/div[1]/div/div/input'))).send_keys('App + Web user')
        
        app_web_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/div/div[2]/form/div[2]/div/div[3]/label/div[2]'))).click()
        
        register_user = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/div/div[2]/form/div[3]/button[2]'))).click()
        
        add_screen_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div/div/div[1]/div/div/button[2]'))).click()

        web_app_qnt = random.randint(1, 10)  
        for i in range(web_app_qnt):
            print('\033[37m\033[40mCreating app + web screen ', i, '\033[0m')
            time.sleep(2)
            
            add_screen_name = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div[1]/div/div/input'))).send_keys(f'{i} Auto App + Web Screen')
        
            register_screen = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/div[2]/button[2]'))).click()
        
            time.sleep(1)
                                                                               
            click_screen = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[1]/div/div[1]/div[{4+i}]/span'))).click()
            
            file_input = driver.find_element(By.ID, f"mobileImageUpload")
            file_input.send_keys(r'C:\Users\josef\Desktop\AutoCRM\image.png')
            file_input = driver.find_element(By.ID, f"desktopImageUpload")
            file_input.send_keys(r'C:\Users\josef\Desktop\AutoCRM\image.png')
            
            func_qnt = random.randint(1, 3)
            for j in range(func_qnt):
                print('\033[37m\033[40mCreating app + web functionality ', j, '\033[0m')
                add_func_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/div[2]/div[2]/div/div[1]/div/button[2]'))).click()
                time.sleep(0.5)
                func_name = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div/div[2]/div[2]/div[2]/div/div[5]/div/div/div[2]/div[1]/input[2]"))).send_keys(f'{j}')
                time.sleep(0.5)
                add_value = wait.until(EC.element_to_be_clickable((By.XPATH, f"/html/body/main/div/div/div[2]/div[2]/div[2]/div/div[5]/div/div[{j+1}]/div[2]/div[1]/div/input"))).send_keys(func_qnt * 9999999)
                time.sleep(0.5)                                                                 
                add_func = wait.until(EC.element_to_be_clickable((By.XPATH, f'/html/body/main/div/div/div[2]/div[2]/div[2]/div/div[5]/div/div[{j+1}]/div[1]/button[1]'))).click()
                time.sleep(2)
                print('\033[37m\033[40mApp + Web functionality created ', j, '\033[0m')
                
            add_new_screen_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/div[1]/div/div[1]/div[1]/button[2]'))).click()
        
        print('\033[37m\033[40mApp + Web screen done\033[0m')
        
        close_window = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[2]/div[1]/div/div[3]'))).click()

        save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/nav/div[2]/button'))).click()
        save_btn2 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[1]/div/div/button[2]'))).click()   
        
        time.sleep(3) 
        
        payment_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/div[1]/div/div[2]/div[2]/button'))).click()
        
        payment_option = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[3]/div/div[1]/div/div[2]/div[2]/div/div[1]/span'))).click()

        end_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/nav/div[2]/button'))).click()
        
        save_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div[1]/div/div/button[2]'))).click()
        
        print(u'\033[32m\033[40mPROJECT CREATED\033[0m')
        
        time.sleep(7.5)
        
def create_user(proj_ammount):
    driver_path = 'chromedriver.exe'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s) 
    driver.get(os.getenv('URL'))
    wait = WebDriverWait(driver, 5)
    driver.fullscreen_window()
    
    login(wait, driver)
    
    projects_page(wait)
    
    new_project(wait, proj_ammount, driver)
    
    time.sleep(3)
    
    driver.quit()
    
def main():
    num_processes = int(get_user_input("How many users to simulate?"))

    proj_ammount = int(get_user_input("How many project?"))

    processes = []
    for _ in range(num_processes):
        p = multiprocessing.Process(target=create_user, args=(proj_ammount,))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    main()