'''
'''
from selenium2extjs.webelements.ExtJSComponent import ExtJSComponent


class Button(ExtJSComponent):
    '''
    classdocs
    '''

    def __init__(self, driver, query_type="", query="", top_element=None):
        '''
        Constructor
        '''
        self.cmp_element = "btnEl"
        super(Button, self).__init__(driver, query_type, query, top_element)
