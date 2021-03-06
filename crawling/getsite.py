'''
크롤링할 사이트 접속하기
'''
from selenium import webdriver

# 링크 긁어오기
driver = webdriver.Chrome(executable_path="C:/Users/morrr/chromedriver.exe")
driver.get("https://transcripts.foreverdreaming.org/viewforum.php?f=431")
driver.implicitly_wait(10)