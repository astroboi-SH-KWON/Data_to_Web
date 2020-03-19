import tabula

class Utils:
    def __init__(self):
        self.ext_pdf = ".pdf"

    """
    read_pdf : read table data from pdf file then make it to DataFrame object
    :param
        path :
        flag : multiple_tables=True/False
    :return
        dict object
    """
    def read_pdf_to_dict(self,path,flag):
        return tabula.read_pdf(path,multiple_tables=flag).to_dict()

    def read_pdf_as_table(self,path,flag):
        return tabula.read_pdf(path,multiple_tables=flag)

    def read_table_by_header(self, obj, header):
        return obj[header]

    def read_txt_to_list(self, file_path):
        tmp_list = []
        with open(file_path, "r") as f:
            while True:
                str_line = f.readline().replace("\n","").replace("\r","")
                if str_line == '':
                    break
                tmp_list.append(str_line)
        return tmp_list

