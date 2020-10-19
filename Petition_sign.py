from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.change.org/p/andy-beshear-justice-for-breonna-taylor?source_location=topic_page")
fname = 'abdullah'
lname = 'maqsood'
email = 'abdullahmaqsood2012@gmail.com'
#signbutton = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div[3]/div[2]/div/div/div/div[2]/div[2]/form/button[2]")
signbutton = driver.find_element_by_css_selector('#page > div.container.xs-pan > div.row.mbxxl.xs-mbn.xs-mhn > div.hidden-xs > div > div > div > div.sc-AxheI.nPYYb > div.sc-AxheI.iDtiqJ > form > button.btn.btn-big.btn-full.btn-action')
print(signbutton)
publiccheck = driver.find_element_by_name("public")
#fnamebox.send_keys(fname)
#lnamebox.send_keys(lname)
#emailbox.send_keys(email)
#publiccheck.click()
signbutton.click()