# Made by Teebowie (github.com/teebowie)

# Library import
import subprocess
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException

# Constant
VOTESITE = "https://mvhatquocca.truyenhinhthanhnien.com.vn/khoi-5-tieu-hoc-minh-khai-1227-tin237"
VOTESITETITLE = "Khối 5, Tiểu học Minh Khai | 1227"
XPATH_1 = "/html/body/section/div/div/div[1]/div[3]/button[2]"
XPATH_2 = "/html/body/section/div/div/div[1]/div[3]/button[1]"
PATH = "py F:\\python\\newAuto.py"

# Main func  
def main():
	driver.get(VOTESITE)
	if driver.title == VOTESITETITLE:
		time.sleep(22)
		try:
		WebDriverWait(driver, 10).until(EC.alert_is_present())
			driver.switch_to.alert.accept()
			print("The alert is accepted. Successfully connected to the Website!")
			time.sleep(3)
			locateElAndVote()
		except (NoAlertPresentException, TimeoutException) as error:
			html = driver.find_element_by_tag_name('html')
			html.send_keys(Keys.END)
			vote_noAlert()
		except WebDriverException:
			call('taskkill /f /im chrome.exe')
			call(PATH)
	else:
		subprocess.run('taskkill /f /im chrome.exe')
		subprocess.run(PATH)

def locateElAndVote():
	try:
		voteBtn_1 = driver.find_element_by_xpath(XPATH_1)
		voteBtnText_1 = voteBtn_1.text
		if voteBtnText_1 == "BÌNH CHỌN":
			voteBtn_1.location_once_scrolled_into_view
			voteBtn_1.click()
	except NoSuchElementException:
		print('btn 1 not found, trying with btn 2')
			
	try:
		voteBtn_2 = driver.find_element_by_xpath(XPATH_2)
		voteBtnText_2 = voteBtn_2.text
		if voteBtnText_2 == "BÌNH CHỌN":
			voteBtn_2.location_once_scrolled_into_view
			voteBtn_2.click()
	except NoSuchElementException:
		print('something went wrong')

	print("Vote submitted! Closing...")
	print(x)
	# 3 : so thoi` gian doi sau khi da vote thanh` cong (da binh` chon)
	time.sleep(3)
	driver.quit()

def vote_noAlert():
		print("Successfully connected to the Website!")
		time.sleep(3)
		locateElAndVote()

if __name__ == "__main__":
	for x in range(10000):
		print(time.ctime(time.time()))
		driver = webdriver.Chrome(ChromeDriverManager().install())
		main()	

# Made by Teebowie (github.com/teebowie)
