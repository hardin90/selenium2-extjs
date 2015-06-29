'''
'''
from selenium2extjs.webelements.ExtJSComponent import ExtJSComponent


class MenuItem(ExtJSComponent):
    '''
    classdocs
    '''

    def __init__(self, driver, query_type="", query="", top_element=None):
        '''
        Constructor
        '''
        self.cmp_element = 'itemEl'
        super(MenuItem, self).__init__(driver, query_type, query, top_element)
