from re import search

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\sumit.chowdhury\\PycharmProjects\\DevOpsBrowserTest\\Webdriver\\chromedriver.exe")

driver.get("https://qadevopsdemosumit.azurewebsites.net/webapp/")

text1 = driver.find_element_by_xpath("//*[text()=' One Large Ocean']").text
text2 = driver.find_element_by_css_selector("h2").text

print("The heading is : "+text1)
print("The first line is : "+text2)

assert text1 == "One Large Ocean"
assert search("OneOcean", text2)

driver.close()