// Copyright (c) 2025, mhmed rjb and contributors
// For license information, please see license.txt

frappe.ui.form.on("POS Payment", {
	customer: function (frm) {
	  if (frm.doc.customer) {
		console.log(frm.doc)

		frappe.call({
		  method: "erpnext.accounts.utils.get_balance_on",
		  args: {
			party_type: "Customer",
			party: frm.doc.customer,
		  },
		  callback: function (r) {
			if (r.message) {
			  frm.set_value("party_balance", r.message); 
			}
		  },
		});
	  }
	},
  });
  