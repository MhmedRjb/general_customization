from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice
from erpnext.accounts.utils import get_balance_on


class CustomSalesInvoice(SalesInvoice):
    def before_save(self):
        self.party_balance = get_balance_on(
            party_type="Customer", party=self.customer_name
        )
