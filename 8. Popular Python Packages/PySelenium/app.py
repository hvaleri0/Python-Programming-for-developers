from selenium import webdriver
import config

# create an instance of the Chrome Class:
browser = webdriver.Chrome()

# browse to github:
browser.get("https://github.com")

# find element by its text, make sure to spell it exactly how you see it on webpage
signin_link = browser.find_element_by_link_text("Sign in")

# click on the CTA:
signin_link.click()

# if the element has a unique id use the unique id! & simultate entering keys:
username_box = browser.find_element_by_id("login_field")
username_box.send_keys(config.username)
password_box = browser.find_element_by_id("password")
password_box.send_keys(config.password)
password_box.submit()

# you can create an assertion to make sure the user name is in the html
assert "ninjacoder22" in browser.page_source

# more specific:
profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "ninjacoder22" in link_label

browser.quit()
