from selenium.webdriver.common.by import By

class LocatorsOrder:
    ORDER_FORM = (By.XPATH, "//*[@class='Order_Form__17u6u']")
    NAME_FIELD = (By.XPATH, "//input[contains(@placeholder,'* Имя')]")
    SURNAME_FIELD = (By.XPATH, "//input[contains(@placeholder,'* Фамилия')]")
    ADDRESS_FIELD = (By.XPATH, "//input[contains(@placeholder,'* Адрес: куда привезти заказ')]")
    METRO_FIELD = (By.XPATH, "//*[@class='select-search']")
    DATE_FIELD = (By.XPATH, "//input[contains(@placeholder,'* Когда привезти самокат')]")
    RENTAL_FIELD = (By.XPATH, "//*[@class='Dropdown-placeholder']")
    RENTAL_LIST = (By.XPATH, "//*[@class='Dropdown-menu']")
    CHOOSE_MENU_FIELD = (By.XPATH, ".//div[text()='двое суток']")
    CHOOSE_MENU_FIELD_ADD = (By.XPATH, ".//div[text()='сутки']")
    CHOOSE_METRO_FIELD = (By.XPATH, ".//div[text()='Черкизовская']")
    CHOOSE_METRO_FIELD_ADD = (By.XPATH, ".//div[text()='Сокольники']")
    METRO_LIST = (By.XPATH, "//*[@class='select-search__select']")
    PHONE_FIELD = (By.XPATH, "//input[contains(@placeholder,'* Телефон: на него позвонит курьер')]")
    BLACK_CHECKOX = (By.XPATH, "//*[@id='black']")
    GREY_CHECBOX = (By.XPATH, "//*[@id='grey']")
    COMMENT_FIELD = (By.XPATH, "//input[contains(@placeholder,'Комментарий для курьера')]")
    BUTTON_NEXT = (By.XPATH, ".//button[text()='Далее']")
    ORDER_BUTTON = (By.XPATH, ".//button[@class != 'Button_Button__ra12g' and text()='Заказать']")
    AGREE_BUTTON = (By.XPATH, ".//button[text()='Да']")
    SUCCESS_ORDER = (
    By.XPATH, ".//*[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']")
    CONFIRMATION_HEADER = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")







