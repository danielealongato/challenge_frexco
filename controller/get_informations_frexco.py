from view.utilities_frexco import HandlerFrexco
from components.handler_csv import HandlerFile


class FrexcoFlow:

    def __init__(self):
        self.handler_frexco = HandlerFrexco()
        self.handler_file = HandlerFile()


    def frexco_flow(self):
        self.handler_frexco.load_site()
        list_items = self.handler_frexco.get_elements_list()
        self.handler_frexco.close_page()
        for item in list_items:
            self.handler_file.inserting_data(data=item)




