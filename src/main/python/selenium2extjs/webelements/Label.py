'''
Created on Jun 22, 2015
'''
from selenium2extjs.webelements.Field import Field


class Label(Field):
    '''
    classdocs
    '''

    def __init__(self, driver, query_type="", query="", top_element=None):
        '''
        Constructor
        '''
        super(Field, self).__init__(driver, query_type, query, top_element)

    def get_text_content(self):
        return self.exec_script_on_extjs_cmp('return extCmp.html')
