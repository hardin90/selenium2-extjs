'''
'''
from selenium2extjs.webelements.Field import Field


class Checkbox(Field):
    '''
    classdocs
    '''

    def __init__(self, driver, query_type="", query="", top_element=None):
        '''
        Constructor
        '''
        self.cmp_element = 'inputEl'
        super(Field, self).__init__(driver, query_type, query, top_element)

    def is_checked(self):
        return self.exec_script_on_extjs_cmp(
            'return extCmp.checked;')

    def check(self):
        if not self.is_checked():
            self.get_element().click()

    def un_check(self):
        if self.is_checked():
            self.get_element().click()
