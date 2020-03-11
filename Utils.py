import tabula

class Utils:
    def __init__(self):
        self.ext_pdf =".pdf"

    """
    read_pdf : read table data from pdf path then make it to DataFrame object
    :param
        path : pdf file path
        flag : multiple_tables=True/False
    :return
        DataFrame object 
    """
    def read_pdf(self,path, flag):
        return tabula.read_pdf(path, multiple_tables=flag)

    def read_by_col_name(self,col_name):