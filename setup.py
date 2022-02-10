import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#This is where the setup for the task is
class Setup:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=self.options)
    def run(self):
        options = self.options
        driver=self.driver
        driver.get("https://in.tradingview.com/chart/?symbol=NSE%3ANIFTY")
        driverwait = WebDriverWait(driver, 10)
        # time.sleep(1)
        #Accept Cookies
        driverwait.until(EC.presence_of_element_located((By.CLASS_NAME,"content-1UNGmyXO"))).click() 
        # time.sleep(1)
        #Change Interval
        driverwait.until(EC.presence_of_element_located((By.ID,"header-toolbar-intervals"))).click()
        driver.find_element(By.CSS_SELECTOR,"div[data-value='15']").click()
        # time.sleep(1)

        # Theme switch for easy debugging
        # driver.find_element(By.CLASS_NAME,"menu-2WfzAPA-").click()
        # driver.find_element(By.CSS_SELECTOR,"label[for='theme-switcher']").click()
        # ActionChains(driver).key_down(Keys.ESCAPE).key_up(Keys.ESCAPE).perform()
        # time.sleep(2)
        
        
        #Indicators tab
        driverwait.until(EC.presence_of_element_located((By.ID,"header-toolbar-indicators"))).click()

        searchBar=driverwait.until(EC.presence_of_element_located((By.CLASS_NAME,"input-3n5_2-hI")))
        # time.sleep(0.5)

        #Search Alligator
        searchBar.send_keys("Alligator") 
        # time.sleep(0.7)
        driverwait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[data-title='Williams Alligator']"))).click() #Add Alligator

        #Search Supertrend
        searchBar.send_keys("Supertrend") 
        # time.sleep(0.7)
        driverwait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[data-title='Supertrend']"))).click() #Add Supertrend

        #Search Pivot
        searchBar.send_keys("Pivot") 
        # time.sleep(0.7)
        driverwait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[data-title='Pivot Points Standard']"))).click() #Add Pivot
        driverwait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span[data-name='close']"))).click()
        time.sleep(2)
        
        action = ActionChains(driver)

        #Change the settings for alligator jawline
        allig = driverwait.until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Alligator')]")))
        action.move_to_element(allig).perform()
        driver.find_elements(By.CSS_SELECTOR,"div[data-name='legend-settings-action']")[0].click() 
        # time.sleep(0.6)
        driverwait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[data-value='style']"))).click()
        driverwait.until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Teeth')]"))).click()
        driverwait.until(EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'Lips')]"))).click()
        # time.sleep(0.3)
        driverwait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[name='submit']"))).click()
        # ActionChains.click(driver.find_element(By.XPATH,"//div[contains(@class,'fill-i5o9yNmy')]"))

        #Adjust for relevant data
        for i in range(15):
            action.key_down(Keys.CONTROL).send_keys(Keys.ARROW_UP).key_up(Keys.CONTROL).perform()
            # time.sleep(0.5)
        action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
        time.sleep(0.5)
        action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()
        time.sleep(3)
        self.driver = driver

        

    def quit(self):
        self.driver.close()

    def getdata(self):
        driver = self.driver
        driverwait = WebDriverWait(driver, 10)
        #Get Candle info
        candlePoints = {}
        candlePoints['open'] = float(driverwait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'O')]/following-sibling::div"))).text)
        candlePoints['close'] = float(driverwait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'C')]/following-sibling::div"))).text)
        candlePoints['high'] = float(driverwait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'H')]/following-sibling::div"))).text)
        candlePoints['low'] = float(driverwait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(text(),'L')]/following-sibling::div"))).text)

        #Get latest Alligator line and Supertrend
        refPoints = {}
        refPoints['alligatorJaw'] = float(driverwait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='valueValue-1WIwNaDF' and contains(@style,'color: rgb(41, 98, 255);')]"))).text)
        try:
            refPoints['superTrendGreen'] = float(driverwait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='valueValue-1WIwNaDF' and contains(@style,'color: rgb(76, 175, 80);')]"))).text)
            refPoints['superTrendRed'] = None
        except Exception as e:
            refPoints['superTrendGreen'] = None
            refPoints['superTrendRed'] = float(driverwait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='valueValue-1WIwNaDF' and contains(@style,'color: rgb(255, 82, 82);')]"))).text) 

        #uncomment for deubgging  
        # output_img = "checkpoint2.png"     
        # driver.get_screenshot_as_file(output_img)
        # print(refPoints)
        # print(candlePoints)
        # print(pivots)
        
        return {'refPoints':refPoints,'candlePoints':candlePoints}

if __name__ == "__main__":
    s = Setup()
    s.run()
    s.quit()    