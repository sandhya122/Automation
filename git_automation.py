import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome('/usr/local/bin/chromedriver')

#Challenge #1: Repository Creation
email= 'systemtest941@gmail.com'
password = 'github@1234'

driver.get("https://github.com/")
driver.find_element(By.LINK_TEXT, 'Sign in').click()
driver.find_element(By.ID, 'login_field').send_keys(email)
driver.find_element(By.ID, 'password').send_keys(password)
driver.find_element(By.XPATH,'//*[@class="btn btn-primary btn-block"]').click()

driver.find_element(By.XPATH, '//*[@class="dropdown-caret"]').click()
driver.find_element(By.XPATH,'(//*[@class="dropdown-item"])[1]').click()
driver.find_element(By.XPATH, '//*[@id="repository_name"]').send_keys("test_repo")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@class="btn btn-primary first-in-line"]').click()

try:

    #Challenge #2: Issue Creation

    driver.find_element(By.XPATH,'//*[@class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline"]').click()
    driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="issue_title"]').send_keys("issue title")
    driver.find_element(By.XPATH,'//*[@id="issue_body"]').send_keys("issue description")
    driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]').click()

    #Create another issue on Github while mentioning previous issue in description and title

    driver.find_element(By.XPATH, '//*[@class="btn btn-sm btn-primary m-0 ml-2 ml-md-2"]').click()
    driver.find_element(By.XPATH,'//*[@id="issue_title"]').send_keys("new issue title")
    driver.find_element(By.XPATH,'//*[@id="issue_body"]').send_keys("new issue description")
    driver.find_element(By.XPATH, '//*[@class="octicon octicon-cross-reference"]') .click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[contains(@id,"suggester-issue-")]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]').click()

    #Challenge #3: Comment to an Issue
    #Add some comments to the issue created in challenge #2
    driver.find_element(By.XPATH, '//*[@id="new_comment_field"]').send_keys("Comment line")
    time.sleep(2)
    driver.find_element(By.XPATH,'(//*[@class="btn btn-primary"])[2]').click()
    time.sleep(2)

    #Add emoji in the repository created in challenge #1

    driver.find_element(By.XPATH,'(//*[@class="octicon octicon-smiley"])[3]').click()
    driver.find_element(By.XPATH, '(//*[@class="emoji"])[3]').click()

    #Challenge  # 4: Issue mention in comments link to Issue
    #Issue mention in comments link to Issue
    driver.find_element(By.XPATH, '//*[@id="new_comment_field"]').send_keys("Comment line 2")
    driver.find_element(By.XPATH, '(//*[@class="octicon octicon-cross-reference"])[3]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[contains(@id,"suggester-issue-")][1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'(//*[@class="btn btn-primary"])[4]').click()

    #Navigate to the issue from the comment
    time.sleep(2)
    driver.find_element(By.XPATH, '(//*[@class="issue-link js-issue-link"])[2]').click()


    #Challenge #5: Delete repository
    driver.find_element(By.XPATH,'//*[@class="octicon octicon-gear UnderlineNav-octicon d-none d-sm-inline"]').click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.XPATH, '(//*[@class="btn btn-danger boxed-action"])[4]').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'(//*[@class="btn btn-block btn-danger" and contains(text(),"delete this")])').click()
    driver.find_element(By.XPATH,'(//*[@name="verify"])[3]').send_keys("usertest-sys/test_repo")
    driver.find_element(By.XPATH,'(//*[@class="btn btn-block btn-danger" and contains(text(),"delete this")])').click()

except:
    #Challenge #5: Delete repository
    driver.find_element(By.XPATH, '//*[@class="octicon octicon-gear UnderlineNav-octicon d-none d-sm-inline"]').click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.XPATH, '(//*[@class="btn btn-danger boxed-action"])[4]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '(//*[@class="btn btn-block btn-danger" and contains(text(),"delete this")])').click()
    driver.find_element(By.XPATH, '(//*[@name="verify"])[3]').send_keys("usertest-sys/test_repo")
    driver.find_element(By.XPATH, '(//*[@class="btn btn-block btn-danger" and contains(text(),"delete this")])').click()
