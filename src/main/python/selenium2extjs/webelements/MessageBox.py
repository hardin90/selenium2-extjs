'''
'''
from selenium2extjs.webelements.ExtJSComponent import ExtJSComponent
from selenium2extjs.webelements.ExtJSQueryType import ComponentQuery
from selenium2extjs.webelements.Button import Button


class MessageBox(ExtJSComponent):
    '''
    References: 
        http://docs.sencha.com/extjs/4.2.3/source/MessageBox.html
        http://dev.sencha.com/deploy/ext-4.0.0/examples/message-box/msg-box.html
    '''

    def __init__(self, driver):

        self.ext_attr = dict(
            item_id="[itemId='%s']",
            msgbox_xtype="messagebox",
        )

        self.button_ids = dict(
            yes='yes',
            no='no',
            ok='ok',
            cancel='cancel',
        )

        super(MessageBox, self).__init__(
            driver, ComponentQuery, self.ext_attr['msgbox_xtype'])

        self.yes_btn = self.ext_attr['item_id'] % self.button_ids['yes']
        self.no_btn = self.ext_attr['item_id'] % self.button_ids['no']
        self.ok_btn = self.ext_attr['item_id'] % self.button_ids['ok']
        self.cancel_btn = self.ext_attr['item_id'] % self.button_ids['cancel']

    def get_title(self):
        return self.exec_script_on_extjs_cmp('return extCmp.title')

    def get_message(self):
        return self.exec_script_on_extjs_cmp('return extCmp.msg.value')

    def is_visible(self):
        '''
        @see: MessageBox.isVisible(): Boolean     
        Returns true if the message box is currently displayed
        '''
        return self.exec_script_on_extjs_cmp_return_bool(
            'return extCmp.isVisible()'
        )

    def click_yes(self):
        self.click_button_by_cmp_query(self.yes_btn)

    def click_no(self):
        self.click_button_by_cmp_query(self.no_btn)

    def click_ok(self):
        self.click_button_by_cmp_query(self.ok_btn)

    def click_cancel(self):
        self.click_button_by_cmp_query(self.cancel_btn)

    def click_button_by_cmp_query(self, query):
        element = self.get_button_by_cmp_query(query)
        element.click()

    def get_button_by_cmp_query(self, query):
        button = Button(self.driver, ComponentQuery, query)
        return button.get_element()
