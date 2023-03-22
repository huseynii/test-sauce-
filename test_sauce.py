from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Sauce:

    def kullaniciAdiBos(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput= driver.find_element(By.ID, "user-name")
        passwordInput= driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()

        errorMessage= driver.find_element(By.XPATH,"//*[@id='login-button']")
        testResult= errorMessage.text=="Epic sadface: Username is required"
        print(f"TEST SONUCU:{testResult}")
        sleep(2) 


    def sifreBos(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput= driver.find_element(By.ID, "user-name")
        passwordInput= driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage= driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult= errorMessage.text=="Epic sadface: Password is required"
        print(f"TEST SONUCU:{testResult}")
        sleep(2)



    def girisKitlendi(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput= driver.find_element(By.ID, "user-name")
        passwordInput= driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage= driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult= errorMessage.text=="Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU:{testResult}")
        sleep(2)




    def errorIcon(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput= driver.find_element(By.ID, "user-name")
        passwordInput= driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage= driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult= errorMessage.text=="Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU:{testResult}")
        sleep(2)



    def girisBilgileri(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput= driver.find_element(By.ID, "user-name")
        passwordInput= driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(3)
        driver.get("https://www.saucedemo.com/inventory.html")
        sleep(2)
        


    def urunListesi(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput= driver.find_element(By.ID, "user-name")
        passwordInput= driver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage= driver.find_element(By.XPATH,"//*[@id='login-button']")
        testResult= errorMessage.text=="Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU:{testResult}")
        sleep(5)
        driver.get("https://www.saucedemo.com/inventory.html")
        listofCourses= driver.find_elements(By.CLASS_NAME,"inventory_iteg")
        print(f"soucedemo sitesinde şu anda {len(listofCourses)} adet kurs var.")
        sleep(25)
testClass=Test_Sauce()

testClass.kullaniciAdiBos() 
testClass.sifreBos()
testClass.girisKitlendi()
testClass.errorIcon()
testClass.girisBilgileri()
testClass.urunListesi()
while True:
    continue