'''
'''
from selenium2extjs.webelements.ExtJSComponent import ExtJSComponent


class Combobox(ExtJSComponent):
    '''
    classdocs
    '''

    def __init__(self, driver, query_type="", query="", top_element=None):
        '''
        Constructor
        '''
        self.combobox_element = "inputEl"
        super(Combobox, self).__init__(driver, query_type, query, top_element)

    def get_element_id(self):
        element_id = self.exec_script_on_extjs_cmp(
            "return extCmp.%s.id" % self.combobox_element
        )
        return element_id

    def get_element(self):
        element_id = self.exec_script_on_extjs_cmp(
            "return extCmp.%s.id" % self.combobox_element
        )
        return self.driver.find_element_by_id(element_id)

    def get_value(self):
        value = self.exec_script_on_extjs_cmp(
            "return extCmp.%s.dom.value" % self.combobox_element
        )
        return value

    def set_value(self, value):
        value = self.exec_script_on_extjs_cmp(
            "return extCmp.%s.dom.value='%s'" % (self.combobox_element, value)
        )
        return value

    def click(self):
        self.exec_script_on_extjs_cmp(
            "return extCmp.%s.dom.click()" % self.combobox_element
        )
