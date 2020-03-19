from selenium import webdriver


import Utils
import Process
############### start to set env ################
WEB_DRV_PATH = "C:/Users/terry/chromedriver.exe"
PDF_PATH = "C:/Users/terry/Documents/카카오톡 받은 파일/2020-1_Korea_Uni/신입생 연락처-최종.pdf"
"""
url
id
passwrd
"""
TAGET_INFO = "C:/Users/terry/Documents/카카오톡 받은 파일/2020-1_Korea_Uni/원우회사이트정보.txt"
GISU = "65"
############### end setting env ################
WEB_DRV = webdriver.Chrome(WEB_DRV_PATH)
def main():
    util = Utils.Utils()
    target_info_list = util.read_txt_to_list(TAGET_INFO)
    target_url = target_info_list[0]
    target_id = target_info_list[1]
    target_pwd = target_info_list[2]

    process = Process.Process(WEB_DRV,target_url)

    table_data = util.read_pdf_as_table(PDF_PATH,False)

    process.go_to_url(target_url + "/Admin/")
    login_elements = [
        "username"
        , "password"
        , "button"
        , "fr"
    ]
    process.login(login_elements, [target_id, target_pwd])

    # 회원 등록
    # process.add_user(table_data)
    # 교우 주소록 등록
    process.add_address(table_data, GISU)


print("start>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
main()

