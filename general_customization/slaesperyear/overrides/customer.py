#overide gl entry file
from frappe import _
from erpnext.accounts.doctype.gl_entry.gl_entry import GLEntry

class CustomGLEntry(GLEntry):

    def before_insert(self):
        pass
    #bering total sales from last doc which fit the condition of customer and
    #Voucher Type should be  sales or reture 


    def after_insert(self):
     # sum credit + debit +  total sales  from last doc

        pass

