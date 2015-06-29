'''
'''
from selenium2extjs.webelements.ExtJSComponent import ExtJSComponent


class Menu(ExtJSComponent):
    '''
    classdocs
    '''

    def __init__(self, driver, query_type="", query="", top_element=None):
        '''
        Constructor
        '''
        self.cmp_element = 'targetEl'
        super(Menu, self).__init__(driver, query_type, query, top_element)

    def select_menu_item(self, menu_item):
        pass
