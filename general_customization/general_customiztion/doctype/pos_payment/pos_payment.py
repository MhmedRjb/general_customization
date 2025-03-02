# Copyright (c) 2025, mhmed rjb and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class POSPayment(Document):
	customer_account ="مدينون - E"
 
	def validate(self):
		frappe.msgprint("customer, paid_amount, customer_account, account")

	def on_submit(self):
		frappe.msgprint("customer, paid_amount, customer_account, account")
		self.add_payment_entry(self.customer, self.paid_amount, self.customer_account, self.paid_to)

	def on_cancel(self):
		self.cancel_payment_entry()



	def add_payment_entry(self, customer, paid_amount, customer_account, account):
		frappe.msgprint("customer, paid_amount, customer_account, account")
		if not customer_account:
			frappe.throw(f"Customer account for {customer} not found")

		pe = frappe.new_doc("Payment Entry")
		payment_entry = {
			"party_type": "Customer",
			"party": customer,
			"payment_type": "Receive",
			"paid_amount": paid_amount,
			"received_amount": paid_amount,
			"paid_from": customer_account,
			"paid_to": account,
			"target_exchange_rate": 1,
			"source_exchange_rate": 1,
			"paid_to_account_currency": "EGP",
		}
		pe.update(payment_entry)


		pe.flags.ignore_permissions = True
		pe.flags.ignore_validate_update_after_submit = True

		pe.save(ignore_permissions=True)
		pe.submit()
  
  
		self.payment_entry=pe.name
		self.save(ignore_permissions=True)

		frappe.db.commit()
  
  
	def cancel_payment_entry(self):
		if self.payment_entry:
			pe = frappe.get_doc("Payment Entry", self.payment_entry)
			if pe.docstatus == 1:
				pe.cancel()
				frappe.db.commit()