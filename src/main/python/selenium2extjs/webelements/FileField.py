'''
'''
from selenium2extjs.webelements.Field import Field


class FileField(Field):
    '''
    classdocs
    '''

    def __init__(self, driver, query_type="", query="", top_element=None):
        '''
        Constructor
        '''
        self.cmp_element = "fileInputEl"
        super(Field, self).__init__(driver, query_type, query, top_element)

    def get_input_el(self):
        element_id = self.exec_script_on_extjs_cmp(
            "return extCmp.button.%s.id" % self.cmp_element
        )
        return self.driver.find_element_by_id(element_id)
