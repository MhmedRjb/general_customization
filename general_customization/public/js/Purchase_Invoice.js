frappe.ui.form.on('Purchase Invoice', {
    supplier: function(frm) {
        if (frm.doc.supplier) {
            frappe.call({
                method: "erpnext.accounts.utils.get_balance_on",
                args: {
                    party_type: 'Supplier',
                    party: frm.doc.supplier
                },
                callback: function(r) {
                    if (r.message) {
                        frm.set_value('custom_party_balance', r.message);
                        console.log("supplier selected: " + frm.doc.supplier + ", custom balance set: " + r.message);
                    }
                }
            });
        }
    }
});