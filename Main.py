import Utils

PDF_PATH = "C:/Users/terry/Documents/카카오톡 받은 파일/신입생 연락처-최종.pdf"

WEB_DRV_PATH = "C:/Users/terry/chromedriver.exe"
MAIN_URL = "http://eng.acz.kr/"
ID = "admin"
PWD = "11223344"


def main():
    util = Utils.Utils()
    df = util.read_pdf(PDF_PATH,False)
    print(df)




print("start>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
main()


