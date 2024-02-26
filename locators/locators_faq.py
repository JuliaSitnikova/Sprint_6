from selenium.webdriver.common.by import By

class FaqLocators:
    SCOOTER_FIELD = (By.XPATH, "//*[@class='Home_Scooter__3YdJy']")
    SCOOTER_IMAGE = (By.XPATH, "//*[@class='Home_BluePrint__TGX2n']")
    FAQ_0_Q = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-0"]'
    FAQ_1_Q = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-1"]'
    FAQ_2_Q = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-2"]'
    FAQ_3_Q = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-3"]'
    FAQ_4_Q = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-4"]'
    FAQ_5_Q = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-5"]'
    FAQ_6_Q = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-6"]'
    FAQ_7_Q = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__heading-7"]'
    FAQ_0_A = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-0"]'
    FAQ_1_A = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-1"]'
    FAQ_2_A = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-2"]'
    FAQ_3_A = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-3"]'
    FAQ_4_A = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-4"]'
    FAQ_5_A = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-5"]'
    FAQ_6_A = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-6"]'
    FAQ_7_A = By.CSS_SELECTOR, '[class*="Home_FAQ"] [id="accordion__panel-7"]'
    ORDER_BUTTON_FIN = (By.XPATH, "//*[@class='Home_FinishButton__1_cWm']")