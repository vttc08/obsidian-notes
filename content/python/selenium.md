# Selenium Web Scraping
```
pip install selenium
```

```python
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
```

```python
# Preparation
driver = webdriver.Firefox()
```

```python
# Go to the page
driver.get("http://google.com")
```

```python
# Persistent Firefox Sessions
options = Options()
options.add_argument("--profile")
options.add_argument("./data")
driver = webdriver.Firefox(options=options)
```

```python
# Input Box
search_box = driver.find_element(By.ID, "APjFqb") # it has to be a textarea or input element in HTML
search_box.clear() # clear the input box
search_box.send_keys("Hello World")
```

```python
# Wait for an element to appear
WebDriverWait(driver, 10).until( # pass a driver class and timeout
    EC.presence_of_element_located((By.ID, "APjFqb")))
# same syntax as find_element, but it waits for the element to appear
# if it doesn't appear in 10 seconds, it will raise an exception
```

    <selenium.webdriver.remote.webelement.WebElement (session="cf63deda-ea4a-4eb1-adac-bf40d80f6241", element="99408df9-69f6-437a-a995-69d84ee4ee03")>

```python
# Find Elements by Text
link = driver.find_element(By.PARTIAL_LINK_TEXT,"computer") # partial link text - all elements that contain the text
# to find by full link text, use By.LINK_TEXT
# can also use find_elements to get a list of matches
```

```python
# Find Elements attribute
link.text # get the text of the element
link.get_attribute("href") # get the href attribute or link of the element
link.screenshot("file.jpg") # take a screenshot of the element (only JPG, for PNG use screenshot_as_png)
link.get_attribute("outerHTML") # get the outer HTML of the element
link.click()
```

    c:\Users\hubcc\Documents\Projects\selenium\venv\lib\site-packages\selenium\webdriver\remote\webelement.py:343: UserWarning: name used for saved screenshot does not match file type. It should end with a `.png` extension
      warnings.warn(

```python
# Send Keys
search_box.send_keys(Keys.LEFT_CONTROL + "a") # Select All
search_box.send_keys(Keys.ENTER + "c") # Copy
# LEFT_CONTROL, LEFT_SHIFT, LEFT_ALT, ENTER
```

[Selenium Keys](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.keys)

```python
# Save screenshot
driver.save_full_page_screenshot("file.jpg") # take a screenshot of the whole page
```

```python
# Stop the driver
driver.quit()
```

### Selenium on a Remote Server (Selenium Grid)
Deploy it on Docker first
https://hub.docker.com/r/selenium/standalone-firefox

```python
newdriver = webdriver.Remote(command_executor='http://10.10.120.16:4444/wd/hub', options=options)
# put the remote drive location :4444/wd/hub
# for persistent directory, it will be stored in the remote server
```
