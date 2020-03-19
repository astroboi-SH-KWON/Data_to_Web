

class Process:
    def __init__(self, web_drv,target_url):
        self.web_drv = web_drv
        self.target_url = target_url

    def go_to_url(self, url):
        self.web_drv.get(url)

    def login(self, elements, login_info):
        self.input_data_by_id(elements[0],login_info[0])
        self.input_data_by_id(elements[1],login_info[1])
        self.get_by_xpath("//"+elements[2]+"[@class='"+elements[3]+"']",False).click()

    def input_data_by_id(self, el_id, data):
        self.web_drv.find_element_by_id(el_id).send_keys(data)

    def click_by_id(self, el_id):
        self.web_drv.find_element_by_id(el_id).click()

    """
    get_by_xpath : 
    :param
        ml_path : xml path
        flag : True -> multi elements
    """
    def get_by_xpath(self,ml_path,flag):
        if flag:
            return self.web_drv.find_elements_by_xpath(ml_path)
        return self.web_drv.find_element_by_xpath(ml_path)

    def add_user(self, data):
        self.go_to_url(self.target_url + "/member_list.htm")
        # table_data_keys = data.keys()
        # print(table_data_keys)
        table_data_trns = data.T
        for header in table_data_trns.keys():
            major = str(table_data_trns[header]["학 과 / 전 공"])
            name = str(table_data_trns[header]["성명"])
            mobile = str(table_data_trns[header]["핸드폰"])
            email = str(table_data_trns[header]["이메일"])
            user_id = mobile.replace("-","")[3:]+"0"

            self.get_by_xpath("//label/input[@name='userid']", False).send_keys(user_id)
            # save parent window
            parent = self.web_drv.current_window_handle
            self.web_drv.execute_script("idcheck()") # popup child window
            # print("check")
            # child popup handles
            child = self.web_drv.window_handles
            self.web_drv.switch_to_window(child.pop())
            # child popup closed
            self.web_drv.execute_script("ok('"+user_id+"')")
            self.web_drv.switch_to_window(parent)

            self.get_by_xpath("//td/input[@name='passwd']", False).send_keys(user_id[4:])
            self.get_by_xpath("//td/input[@name='passwd2']", False).send_keys(user_id[4:])
            self.get_by_xpath("//label/input[@name='name']", False).send_keys(name)
            self.get_by_xpath("//select[@name='mobile1']/option[@value='"+mobile[:3]+"']", False).click()
            self.get_by_xpath("//input[@name='mobile2']", False).send_keys(user_id[:4])
            self.get_by_xpath("//input[@name='mobile3']", False).send_keys(user_id[4:])
            self.get_by_xpath("//input[@name='email']", False).send_keys(email)
            inputs = self.get_by_xpath("//body/table/tbody/tr/th/table/tbody/tr/td/input", True)
            inputs[2].click()

            alert = self.web_drv.switch_to.alert
            alert.accept()

    def add_address(self, data, GISU):
        table_data_trns = data.T
        for header in table_data_trns.keys():
            self.go_to_url(self.target_url + "/Admin/boardw.htm?mode=INSERT_FORM&b_class=5")
            major = str(table_data_trns[header]["학 과 / 전 공"])
            name = str(table_data_trns[header]["성명"])
            mobile = str(table_data_trns[header]["핸드폰"])
            email = str(table_data_trns[header]["이메일"])

            self.get_by_xpath("//input[@name='b_name']",False).send_keys(name)
            self.get_by_xpath("//input[@name='receive_name']",False).send_keys(mobile)
            self.get_by_xpath("//input[@name='b_email']",False).send_keys(GISU)
            self.get_by_xpath("//input[@name='bank_user']",False).send_keys(major)
            self.get_by_xpath("//textarea[@name='b_content']",False).send_keys(email)
            self.get_by_xpath("//body/table/tbody/tr/td/div/input", False).click()

            alert = self.web_drv.switch_to.alert
            alert.accept()
