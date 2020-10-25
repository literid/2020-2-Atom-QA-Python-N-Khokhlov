from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_BUTTON = (By.XPATH, "//div[@class='responseHead-module-button-1BMAy4']")
    EMAIl_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    AUTH_BUTTON = (By.XPATH, "//div[@class='authForm-module-button-2G6lZu']")
    INVALID_LOGIN_TEXT = (By.XPATH, "//div[@class='formMsg_text']")
    LOGOUT_FIELD= (By.XPATH, "//span[@class='js-head-balance']")
    EXIT_BUTTON = (By.XPATH, "//a[@href='/logout']")

class MainPageLocators(object):
    BALANCE = (By.XPATH, "//a[@class='center-module-button-cQDNvq center-module-billing-x3wyL6']")
    COMPANY = (By.XPATH,
               "//a[@class='center-module-button-cQDNvq center-module-campaigns-3hwOlL center-module-activeButton-3i8iSI']")
    SEGMENT = (By.XPATH, "//a[@href='/segments']")


class CompanyPageLocators(object):
    CREATE_COMPANY_BUTTON = (By.XPATH, "//div[1][@class='button-module-textWrapper-3LNyYP' and contains(text(),'Создать кампанию')]")
    TRAFFIC_BUTTON = (By.XPATH, "//div[@class='column-list-item__title js-title' and contains(text(),'Трафик')]")
    LINK_INPUT = (By.XPATH, "//input[@data-gtm-id='ad_url_text']")
    BUDGET_PER_DAY = (By.XPATH, "//input[@data-test='budget-per_day']")
    BUDGET_TOTAL = (By.XPATH, "//input[@data-test='budget-total']")
    BANNER = (By.XPATH, "//span[@class='banner-format-item__title' and contains(text(),'Баннер')]")
    UPLOAD_IMAGE = (By.XPATH, "//input[@data-test='image_240x400']")
    COMPANY_NAME_FIELD = (By.XPATH, "//div[@class='input input_campaign-name input_with-close']//input")
    FINALLY_CREATE_COMPANY = (By.XPATH, "//div[@class='button__text' and contains(text(), 'Создать кампанию')]")
    MYCOMPANY_NAME_IN_LIST = ()


class SegmentPageLocators(object):
    CREATE_SEGMENT_BUTTON1 = (By.XPATH, "//a[@href='/segments/segments_list/new/']")
    CREATE_SEGMENT_BUTTON2 = (By.XPATH, "//div[@class='segments-list'] //div[contains(text(),'Создать сегмент')]")
    APPS_AND_GAMES_BUTTON = (By.XPATH, "//div[@class='adding-segments-modal__block-left js-sources-types'] //div[contains(text(),'Приложения и игры')]")
    PLAYED_AND_PAYED_BUTTON = (By.XPATH, "//input[@class='adding-segments-source__checkbox js-main-source-checkbox']")
    ADD_SEGMENT = (By.XPATH, "//div[@class='button__text' and contains(text(),'Добавить сегмент')]")
    SEGMENT_NAME_FIELD = (By.XPATH, "//div[@class='input input_create-segment-form'] //input")
    SUBMIT_SEGMENT = (By.XPATH, "//div[@class='create-segment-form']    //div[contains(text(),'Создать сегмент')]")
    SEARCH_BUTTON = (By.XPATH, "//input[@placeholder='Поиск по названию или id...']")
    UNDER_SEARCH_FIELD = (By.XPATH, "//li[@class='suggester-module-option-1kQRIM optionsList-module-option-25VJZx']")
    DELETE_BUTTON = (By.XPATH, "//span[@class='icon-cross cells-module-removeCell-2tweYp']")
    CONFIRM_REMOVE_BUTTON = (By.XPATH, "//button[@class='button button_confirm-remove button_general'] / div")
    MY_SEGMENT_NAME_LOC = ()