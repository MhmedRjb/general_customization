from erpnext.accounts.utils import get_balance_on
import frappe
def add_balance_on(doc, method):
	doc.party_balance = get_balance_on(
		party_type="Customer", party=doc.customer
	)
