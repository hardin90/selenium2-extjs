'''
'''
from selenium2extjs.webelements.Field import Field


class Radio(Field):
    '''
    classdocs
    '''

    def __init__(self, driver, query_type="", query="", top_element=None):
        '''
        Constructor
        '''
        self.cmp_element = "inputEl"
        super(Field, self).__init__(driver, query_type, query, top_element)

    def is_checked(self):
        '''check if radio button is checked'''
        return self.exec_script_on_extjs_cmp('return extCmp.checked')
