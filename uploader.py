from selenium import webdriver
import time
import os
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
EXTENSION_PATH = './metamask.crx'
opt = webdriver.ChromeOptions()
opt.add_extension(EXTENSION_PATH)
driver = webdriver.Chrome('./chromedriver.exe', options=opt)


def metamask_setup(driver):
    driver.get(
        'chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome')
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="app-content"]/div/div[2]/div/div/div/button').click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath(
        '//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button').click()
    driver.implicitly_wait(3)
    driver.find_element_by_xpath(
        '//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]').click()
    driver.implicitly_wait(3)
    inputs = driver.find_elements_by_xpath('//input')
    inputs[0].send_keys(
        '********Your secret phrase************')
    driver.implicitly_wait(3)

    inputs[1].send_keys('***Set a password*****')
    inputs[2].send_keys('*******Set password*******')
    driver.find_element_by_xpath(
        '//*[@id="app-content"]/div/div[2]/div/div/form/div[7]/div').click()
    driver.implicitly_wait(3)

    driver.find_element_by_xpath(
        '//*[@id="app-content"]/div/div[2]/div/div/form/button').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="app-content"]/div/div[2]/div/div/button').click()
    time.sleep(1)
    initial_setup(driver)


def initial_setup(driver):
    driver.get(r'https://opensea.io/login?referrer=%2Faccount')
    driver.implicitly_wait(3)
    driver.find_element_by_xpath(
        '//*[@id="__next"]/div[1]/main/div/div/div/div[2]/ul/li[1]/button').click()
    time.sleep(5)
    # switch to windows while siging in to metamask

    # Store the ID of the original window
    original_window = driver.current_window_handle
    window_after = driver.window_handles[1]
    # click metamask sign in buttons
    driver.switch_to.window(window_after)
    driver.implicitly_wait(3)
    # next button
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[2]/div[4]/div[2]/button[2]').click()
    driver.implicitly_wait(3)
    # connect button   
    connect = driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
    if connect:
        connect
   # time.sleep(6)
   # sign_window = driver.window_handles[1]
   # driver.switch_to.window(sign_window)
    # sign button click
   # driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]').click()
   # time.sleep(1)
    driver.switch_to.window(original_window)
    # start uploading iterations
    time.sleep(5)
    upload_items(driver,original_window,1103)



# upload nfts 

def upload_items(driver,original_window,x):
    wait = WebDriverWait(driver, 60)
    time.sleep(2)
    driver.get('https://opensea.io/collection/the-cryptomobs-villa')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/div[1]/span/a').click()
    # will ask for signing before going to upload page
    # wait and switch to metamsk sign window
    time.sleep(3)
    
    sign_window = driver.window_handles[1]
    driver.switch_to.window(sign_window)
        # sign button click
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]').click()
        
        # # should be siged and switch back to original window
    driver.switch_to.window(original_window)

    time.sleep(2)
    driver.implicitly_wait(3)
    filePath = f"./build/images/Cryptomob #{x}.png"
    # Opening JSON file
    f = open(f"./build/json/Cryptomob #{x}.json",)
 
    # returns JSON object as
    # a dictionary
    data = json.load(f)

    driver.implicitly_wait(10)
    imageUpload = driver.find_element_by_xpath('//*[@id="media"]')
    imagePath = os.path.abspath(filePath) 
    imageUpload.send_keys(imagePath)
    # fill name
    driver.find_element_by_xpath('//*[@id="name"]').send_keys(f"Cryptomob #{x}")
    # fill external link
    driver.find_element_by_xpath('//*[@id="external_link"]').send_keys('https://www.cryptomobs-villa.com/')
    # fill the description
    driver.find_element_by_xpath('//*[@id="description"]').send_keys('Cryptomobs is a collection of 10K M.O.B. NFTs—unique digital collectibles living on the (block)chain. Through a Cryptomob you become a member of the gang getting access to exclusive perks within the villa')
    # click the properties button
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/section/div[1]/div/div[2]/button').click()
    
    for x in range(6):
        # add properties slots for number of prorperties
        
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/button').click()
    
    time.sleep(1)
    # fill the first property
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[1]/td[1]/div/div/input').send_keys(data['attributes'][0]['trait_type'])
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[1]/td[2]/div/div/input').send_keys(data['attributes'][0]['value'])
    

    # fill the first property
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[2]/td[1]/div/div/input').send_keys(data['attributes'][1]['trait_type'])
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[2]/td[2]/div/div/input').send_keys(data['attributes'][1]['value'])
    

    # fill the first property
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[3]/td[1]/div/div/input').send_keys(data['attributes'][2]['trait_type'])
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[3]/td[2]/div/div/input').send_keys(data['attributes'][2]['value'])
    

    # fill the first property
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[4]/td[1]/div/div/input').send_keys(data['attributes'][3]['trait_type'])
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[4]/td[2]/div/div/input').send_keys(data['attributes'][3]['value'])
    

    # fill the first property
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[5]/td[1]/div/div/input').send_keys(data['attributes'][4]['trait_type'])
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[5]/td[2]/div/div/input').send_keys(data['attributes'][4]['value'])
    

    # fill the first property
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[6]/td[1]/div/div/input').send_keys(data['attributes'][5]['trait_type'])
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[6]/td[2]/div/div/input').send_keys(data['attributes'][5]['value'])
    

    # fill the first property
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[7]/td[1]/div/div/input').send_keys(data['attributes'][6]['trait_type'])
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[7]/td[2]/div/div/input').send_keys(data['attributes'][6]['value'])
    


    # save and create the listing
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/footer/button').click()
    driver.implicitly_wait(3)
    #driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/div[9]/div[1]/span/button').click()
    time.sleep(0.5)
    createNFT = driver.find_element_by_xpath(
            '//*[@id="__next"]/div[1]/main/div/div/section/div/form/div/div[1]/span/button')
    #time.sleep(500000)
    createNFT.click()
    time.sleep(5)
    try:
        WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div[2]/button")))
    finally:
        print('*******************************************************************')
        driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[2]/button").click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/div[1]/div/span[2]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[1]/div/div[2]/div/div/div[2]/input').send_keys('0.025')
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[5]/button').submit()
    time.sleep(2)
    
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/section/div/div/section/div/div/div/div/div/div/div/button').click()
    time.sleep(2)
    sign_window = driver.window_handles[1]
    driver.switch_to.window(sign_window)
    # sign button click
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]').click()
    time.sleep(2)
    # should be siged and switch back to original window
    driver.switch_to.window(original_window)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/button').click()
    # loop items uploading from here and change number of range to upload item from and to
    for x in range(1103,1500):
        loop_items(driver,original_window,x)


def loop_items(driver,original_window,x):
    wait = WebDriverWait(driver, 60)
    time.sleep(2)
    driver.get('https://opensea.io/collection/the-cryptomobs-villa')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/div[1]/span/a').click()
    # will ask for signing before going to upload page
    # wait and switch to metamsk sign window
    time.sleep(3)
    
    # sign_window = driver.window_handles[1]
    # driver.switch_to.window(sign_window)
    #     # sign button click
    # driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]').click()
        
    #     # # should be siged and switch back to original window
    # driver.switch_to.window(original_window)

    time.sleep(2)
    driver.implicitly_wait(3)
    filePath = f"./build/images/Cryptomob #{x+1}.png"
    # Opening JSON file
    f = open(f"./build/json/Cryptomob #{x+1}.json",)
 
    # returns JSON object as
    # a dictionary
    data = json.load(f)

    driver.implicitly_wait(3)
    imageUpload = driver.find_element_by_xpath('//*[@id="media"]')
    imagePath = os.path.abspath(filePath) 
    imageUpload.send_keys(imagePath)
    # fill name
    driver.find_element_by_xpath('//*[@id="name"]').send_keys(f"Cryptomob #{x+1}")
    # fill external link
    driver.find_element_by_xpath('//*[@id="external_link"]').send_keys('https://www.cryptomobs-villa.com/')
    # fill the description
    driver.find_element_by_xpath('//*[@id="description"]').send_keys('Cryptomobs is a collection of 10K M.O.B. NFTs—unique digital collectibles living on the (block)chain. Through a Cryptomob you become a member of the gang getting access to exclusive perks within the villa')
    # click the properties button
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/section/div[1]/div/div[2]/button').click()
    
    for z in range(6):
        # add properties slots for number of prorperties
        
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/button').click()
    
    time.sleep(1)
    # fill the first property
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[1]/td[1]/div/div/input').send_keys(data['attributes'][0]['trait_type'])
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[1]/td[2]/div/div/input').send_keys(data['attributes'][0]['value'])
    

    # fill the first property
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[2]/td[1]/div/div/input').send_keys(data['attributes'][1]['trait_type'])
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[2]/td[2]/div/div/input').send_keys(data['attributes'][1]['value'])
    

    # fill the first property
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[3]/td[1]/div/div/input').send_keys(data['attributes'][2]['trait_type'])
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[3]/td[2]/div/div/input').send_keys(data['attributes'][2]['value'])
    

    # fill the first property
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[4]/td[1]/div/div/input').send_keys(data['attributes'][3]['trait_type'])
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[4]/td[2]/div/div/input').send_keys(data['attributes'][3]['value'])
    

    # fill the first property
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[5]/td[1]/div/div/input').send_keys(data['attributes'][4]['trait_type'])
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[5]/td[2]/div/div/input').send_keys(data['attributes'][4]['value'])
    

    # fill the first property
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[6]/td[1]/div/div/input').send_keys(data['attributes'][5]['trait_type'])
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[6]/td[2]/div/div/input').send_keys(data['attributes'][5]['value'])
    

    # fill the first property
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[7]/td[1]/div/div/input').send_keys(data['attributes'][6]['trait_type'])
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/section/table/tbody/tr[7]/td[2]/div/div/input').send_keys(data['attributes'][6]['value'])
    


    # save and create the listing
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/footer/button').click()
    driver.implicitly_wait(3)
    #driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/section/div[2]/form/div[9]/div[1]/span/button').click()
    time.sleep(0.5)
    createNFT = driver.find_element_by_xpath(
            '//*[@id="__next"]/div[1]/main/div/div/section/div/form/div/div[1]/span/button')
    #time.sleep(500000)
    createNFT.click()
    time.sleep(5)
    try:
        WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div[2]/button")))
    finally:
        print('*******************************************************************')
        print(f"{x} posted........")
        print("**************************************************************")
        driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[2]/button").click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/div[1]/div/span[2]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="__next"]/div[1]/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[1]/div/div[2]/div/div/div[2]/input').send_keys('0.025')
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[5]/button').submit()
    time.sleep(2)
    
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/section/div/div/section/div/div/div/div/div/div/div/button').click()
    time.sleep(3)
    sign_window = driver.window_handles[1]
    driver.switch_to.window(sign_window)
    # sign button click
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]').click()
    time.sleep(2)
    # should be siged and switch back to original window
    driver.switch_to.window(original_window)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/button').click()


metamask_setup(driver)
