from selenium import webdriver
import time


import Utils
import Process

WEB_DRV_PATH = "C:/Users/terry/chromedriver.exe"
PDF_PATH = "C:/Users/terry/Documents/카카오톡 받은 파일/2020-1_Korea_Uni/신입생 연락처-최종.pdf"

"""
url
id
passwrd
"""
TAGET_INFO = "C:/Users/terry/Documents/카카오톡 받은 파일/2020-1_Korea_Uni/원우회사이트정보.txt"
WEB_DRV = webdriver.Chrome(WEB_DRV_PATH)



def main():
    util = Utils.Utils()
    target_info_list = util.read_txt_to_list(TAGET_INFO)
    target_url = target_info_list[0]
    target_id = target_info_list[1]
    target_pwd = target_info_list[2]

    process = Process.Process(WEB_DRV, target_url)


    process.go_to_url(target_url + "/Admin/")
    login_elements = [
        "username"
        , "password"
        , "button"
        , "fr"
    ]
    process.login(login_elements, [target_id, target_pwd])
    # gisu = "65"
    # process.add_address(table_data, gisu)
    # process.go_to_url(target_url + "/Admin/boardw.htm?b_class=5")
    process.go_to_url(target_url + "/Admin/boardw.htm?mode=INSERT_FORM&b_class=5")

    process.get_by_xpath("//input[@name='b_name']",False).send_keys("성명")
    process.get_by_xpath("//input[@name='receive_name']",False).send_keys("핸드폰")
    process.get_by_xpath("//input[@name='b_email']",False).send_keys("gisu")
    process.get_by_xpath("//input[@name='bank_user']",False).send_keys("학 과 / 전 공")
    process.get_by_xpath("//textarea[@name='b_content']",False).send_keys("이메일")
    process.get_by_xpath("//body/table/tbody/tr/td/div/input", False).click()


    # inputs[2].click()
    #
    alert = WEB_DRV.switch_to.alert
    alert.accept()


print("start>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
main()

