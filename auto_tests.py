from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pytest
import time
chrome_options = Options()
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)

start_url = "https://cs.gmu.edu:8443/offutt/servlet/convert2"
driver.get(start_url)
    

def test_fahrenheit():
    print('Testing Fahrenheit with 32')
    search_form = driver.find_element_by_name('F')
    search_form.clear()
    search_form.send_keys('32')

    submit_button = driver.find_element_by_name('submit')
    submit_button.click()

    results = driver.find_element_by_name('C')
    print(results.get_attribute("value"))
    assert results.get_attribute("value") == '0.0'

def test_inches():
    print('Testing Inches with 12')
    search_form = driver.find_element_by_name('in')
    search_form.clear()
    search_form.send_keys('12')

    submit_button = driver.find_element_by_name('submit')
    submit_button.click()

    results = driver.find_element_by_name('cm')
    print(results.get_attribute("value"))
    assert results.get_attribute("value") == '30.48'

def test_feet():
    print('Testing Feet with 3')
    search_form = driver.find_element_by_name('ft')
    search_form.clear()
    search_form.send_keys('3')

    submit_button = driver.find_element_by_name('submit')
    submit_button.click()

    results = driver.find_element_by_name('m')
    print(results.get_attribute("value"))
    assert results.get_attribute("value") == '0.91'

def test_mile():
    print('Testing Mile with 1')
    search_form = driver.find_element_by_name('mi')
    search_form.clear()
    search_form.send_keys('1')

    submit_button = driver.find_element_by_name('submit')
    submit_button.click()

    results = driver.find_element_by_name('km')
    print(results.get_attribute("value"))
    assert results.get_attribute("value") == '1.61'

def test_gallon():
    print('Testing Gallon with 1')
    search_form = driver.find_element_by_name('gal')
    search_form.clear()
    search_form.send_keys('1')

    submit_button = driver.find_element_by_name('submit')
    submit_button.click()

    results = driver.find_element_by_name('L')
    print(results.get_attribute("value"))
    assert results.get_attribute("value") == '3.79'

def test_ounce():
    print('Testing Ounce with 1')
    search_form = driver.find_element_by_name('oz')
    search_form.clear()
    search_form.send_keys('1')

    submit_button = driver.find_element_by_name('submit')
    submit_button.click()

    results = driver.find_element_by_name('g')
    print(results.get_attribute("value"))
    assert results.get_attribute("value") == '28.35'

def test_pound():
    print('Testing Pound with 1')
    search_form = driver.find_element_by_name('lb')
    search_form.clear()
    search_form.send_keys('1')

    submit_button = driver.find_element_by_name('submit')
    submit_button.click()

    results = driver.find_element_by_name('kg')
    print(results.get_attribute("value"))
    assert results.get_attribute("value") == '0.45'



def tear_down():
    driver.quit()   