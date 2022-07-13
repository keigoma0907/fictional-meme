from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import time


# koushin==Tureでchromdriver自動更新
def get_manth_overtime_hour(koushin=False):

	try :
		s = Service('./driver/chromedriver')

		options = Options()
		options.headless = True
		if koushin == True :
			driver = webdriver.Chrome(ChromeDriverManager().install(),service = s,options = options)
		else:
			driver = webdriver.Chrome(service = s,options = options)


		driver.get(
			'https://kics2.jinji.denso.co.jp/siteminderagent/forms_ja-JP/login-kics-ext.fcc?TYPE=33554433&REALMOID=06'
			'-00002983-d190-18d0-b029-0e0e0a06b0a4&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM'
			'-li4UhosEbIspcBjDhA6loGK4HkJ2kPQVsDAqH3z5TVWr79NQcvEp%2fdeJspyBJjJj&TARGET=-SM-https%3a%2f%2fkics2%2ejinji'
			'%2edenso%2eco%2ejp%2fa0tpkkics%2fext%2fjsp%2fTop%2ejsp')

		driver.find_element(By.CSS_SELECTOR,
							'#searchLogin > div:nth-child(3) > input').send_keys('100012444482')
		driver.find_element(By.CSS_SELECTOR,
							'#searchLogin > div:nth-child(5) > input[type=password]:nth-child(2)').send_keys('Keigo0907')

		driver.find_element(By.CSS_SELECTOR,'#searchLogin > div:nth-child(5) > input.submit').click()

		selector1 = '#mainForm > div:nth-child(15) > table > tbody > tr:nth-child(2) > td > div'

		def click_element(selector):
			element = WebDriverWait(driver,30).until(EC.element_to_be_clickable(By.CSS_SELECTOR,selector))
			element.click()

		element1 = WebDriverWait(driver,30).until(
			EC.element_to_be_clickable((By.CSS_SELECTOR,selector1)))
		element1.click()

		selector2 = '#mainForm > div.headerAri > table:nth-child(48) > tbody > tr:nth-child(1) > td:nth-child(2)'

		element2 = WebDriverWait(driver,30).until(
			EC.visibility_of_element_located((By.CSS_SELECTOR,selector2)))

		month_overtime_hour = element2.text

		driver.quit()

	finally:
		driver.quit()

	return month_overtime_hour.replace('h','時間').replace('m','分')


if __name__ == '__main__':

	root = Tk()
	root.title('表示')

	root.geometry("220x90")
	root.withdraw()

	messagebox.showinfo("残業時間",f"今月の残業時間は{get_manth_overtime_hour(koushin=False)}です。")

'''
	f1 = Frame(root)
	f2 = Frame(root)

	def Check_time():
		label2['text'] = '取得中'
		time.sleep(1)
		t = get_manth_overtime_hour()
		label2['text'] = t

	label1 = ttk.Label(
		f1,
		text = f'今月の残業時間  : '
	)

	label2 = ttk.Label(
		f1,
		text = f'未取得'
	)

	button1 = ttk.Button(
		f2,
		text = 'Check',
		command = Check_time)

	button2 = ttk.Button(
		f2,
		text = 'OK',
		command = lambda: root.quit())

	label1.pack(padx=2,pady=10,side=LEFT)
	label2.pack(padx=2,pady=10,side=RIGHT)
	button1.pack(padx=2,pady=10,side=LEFT)
	button2.pack(padx=2,pady=10,side=RIGHT)

	f1.pack(side=TOP)
	f2.pack(side=BOTTOM)

	root.mainloop()
'''

