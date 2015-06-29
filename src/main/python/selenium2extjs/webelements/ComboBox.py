'''
'''
from selenium2extjs.webelements.ExtJSComponent import ExtJSComponent


class ComboBox(ExtJSComponent):
    '''
    classdocs
    '''

    def __init__(self, driver, query_type="", query="", top_element=None):
        '''
        Constructor
        '''
        self.cmp_element = "inputEl"
        super(ComboBox, self).__init__(driver, query_type, query, top_element)

    def get_value(self):
        value = self.exec_script_on_extjs_cmp(
            "return extCmp.%s.dom.value" % self.cmp_element
        )
        return value

    def set_value(self, value):
        value = self.exec_script_on_extjs_cmp(
            "return extCmp.%s.dom.value='%s'" % (self.cmp_element, value)
        )
        return value

    def click(self):
        self.exec_script_on_extjs_cmp(
            "return extCmp.%s.dom.click()" % self.cmp_element
        )
