from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
action = ActionChains(driver)




def start(URL):

  driver.get(URL)

def get_by_id(ID):
  result = driver.find_element(By.ID, ID)
  return result

  
def get_by_name(NAME):
  result = driver.find_element(By.NAME,NAME)
  return result


  
def click(element):
  action.click(element)
  action.perform()

  
def type(text,element):
  element.send_keys(text)