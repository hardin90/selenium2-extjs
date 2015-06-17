'''
Created on Jun 15, 2015
'''
from selenium2extjs.webelements.Field import Field


class Grid(Field):
    '''
    classdocs
    '''

    def __init__(self, driver, query_type="", query="", top_element=None):
        '''
        Constructor
        '''
        super(Grid, self).__init__(driver, query_type, query, top_element)

    def get_grid_content_element(self):
        element_id = self.exec_script_on_extjs_cmp(
            "return extCmp.body.id"
        )
        return self.driver.find_element_by_id(element_id)
