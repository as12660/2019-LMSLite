from selenium import webdriver

browser1 = webdriver.Chrome("C:\\Users\\Noah's Desktop\\Desktop\\chromedriver")
browser1.get('http://127.0.0.1:8000')
browser1.maximize_window()
loginlink = browser1.find_element_by_link_text('Login')
loginlink.click()

email = browser1.find_element_by_id('id_username')
password = browser1.find_element_by_id('id_password')
email.send_keys('prof@prof.com')
password.send_keys('prof')

submit = browser1.find_element_by_id('submit')
submit.click()
#Working on how to figure out testing for quiz code above works though^^^^
'''course1 = browser1.find_element_by_link_text('Course 101')
course1.click()
quiz = browser1.find_element_by_id('quizBtn')
quiz.click()'''



