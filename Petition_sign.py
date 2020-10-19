from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
petitions = ['https://www.change.org/p/justin-trudeau-canada-needs-to-step-up-for-mental-health?source_location=petitions_browse']

for petition in petitions:
    driver.get(petition)
fname = 'abdullah'
lname = 'maqsood'
email = 'abdullahmaqsood2012@gmail.com'
#signbutton = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div[3]/div[2]/div/div/div/div[2]/div[2]/form/button[2]")
signbutton = driver.find_element_by_css_selector('#page > div.container.xs-pan > div.row.mbxxl.xs-mbn.xs-mhn > div.hidden-xs > div > div > div > div.sc-AxheI.nPYYb > div.sc-AxheI.iDtiqJ > form > button.btn.btn-big.btn-full.btn-action')
fname_box = driver.find_element_by_css_selector('#firstName')
lname_box = driver.find_element_by_css_selector('#lastName')
email_box = driver.find_element_by_css_selector('#email')
print(signbutton)
publiccheck = driver.find_element_by_name("public")
fname_box.send_keys(fname)
lname_box.send_keys(lname)
email_box.send_keys(email)
#publiccheck.click()
signbutton.click()