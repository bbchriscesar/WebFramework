from selenium import webdriver

def setup(var):
    options = webdriver.ChromeOptions()
    options.add_argument(var['profile'])
    options.add_argument('--start-maximized')
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(executable_path=var['path'], options=options)
    return driver