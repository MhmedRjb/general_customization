frappe.ui.form.on('Sales Invoice', {
    customer: function(frm) {
        if (frm.doc.customer) {
            frappe.call({
                method: "erpnext.accounts.utils.get_balance_on",  
                args: {
                    party_type: 'Customer',  
                    party: frm.doc.customer  
                },
                callback: function(r) {
                   if (r.message) {
                        frm.set_value('custom_party_balance', r.message);
                        console.log("Customer selected: " + frm.doc.customer + ", custom balance set: " + r.message);
                    }
                }
            });
        }
    }
});
