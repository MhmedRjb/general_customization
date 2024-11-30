import frappe
from erpnext.accounts.doctype.pos_invoice_merge_log.pos_invoice_merge_log import POSInvoiceMergeLog

import json

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.query_builder.functions import Sum
from frappe.utils import flt, nowdate
from frappe.utils.background_jobs import enqueue

from erpnext import get_company_currency
from erpnext.accounts.doctype.accounting_dimension.accounting_dimension import (
	get_accounting_dimensions,
)
from erpnext.accounts.doctype.payment_entry.payment_entry import (
	get_company_defaults,
	get_payment_entry,
)
from erpnext.accounts.doctype.subscription_plan.subscription_plan import get_plan_rate
from erpnext.accounts.party import get_party_account, get_party_bank_account
from erpnext.accounts.utils import get_account_currency, get_currency_precision
from erpnext.utilities import payment_app_import_guard

class CustomPOSInvoiceMergeLog(POSInvoiceMergeLog):
	def on_submit(self):
		super().on_submit()
		self.make_payment_for_on_change()

	def make_payment_for_on_change(self):
		for invoice in self.pos_invoices:
			pos_invoice = frappe.get_doc("POS Invoice", invoice.pos_invoice)
			if pos_invoice.change_amount:
				for payment in pos_invoice.payments:
					change_amount = int(pos_invoice.change_amount)
					self.add_payment_entry(
						customer=pos_invoice.customer,
						paid_amount=change_amount,
						reference_name=pos_invoice.name,
						customer_account=pos_invoice.debit_to,
						account=payment.account,
					)
					break

 

	@frappe.whitelist(allow_guest=True)
	def add_payment_entry(self, customer, paid_amount, reference_name, customer_account, account):
		# customer_account = get_accounts_details(customer)
		if not customer_account:
			frappe.throw(f"Customer account for {customer} not found")

		pe = frappe.new_doc("Payment Entry")
		payment_entry = {
			"party_type": "Customer",
			"party": customer,
			"payment_type": "Receive",
			"mode_of_payment": "Cash",
			"paid_amount": paid_amount,
			"received_amount": paid_amount,
			"paid_from": customer_account,
			"paid_to": account,
			"target_exchange_rate": 1,
			"source_exchange_rate": 1,
			"paid_to_account_currency": "EGP",
		}
		print("payment_entry", payment_entry)
		print("pe", pe)
		# Add payments details in payment reference child table
		pe.update(payment_entry)

		# references = [
		# 	{
		# 		"reference_doctype": "POS Invoice",
		# 		"reference_name": reference_name,
		# 		"allocated_amount": paid_amount
		# 	}
		# ]
		# for reference in references:
		# 	pe.append("references", {
		# 		"reference_doctype": reference["reference_doctype"],
		# 		"reference_name": reference["reference_name"],
		# 		"allocated_amount": reference["allocated_amount"],
		# 	})

		pe.flags.ignore_permissions = True
		pe.flags.ignore_validate_update_after_submit = True

		pe.save(ignore_permissions=True)
		pe.submit()
		frappe.db.commit()


	