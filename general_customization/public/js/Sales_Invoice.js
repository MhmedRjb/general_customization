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

// frappe.ui.form.on('Sales Invoice Item', {
//     qty: function(frm, cdt, cdn) {
//         // Display message to check if qty function is triggered
//         frappe.msgprint('qty changed');
        
//         // Get the item from locals
//         var item = locals[cdt][cdn];
//         console.log('Quantity:', item.qty);

//         // Check if item.qty equals 5
//         if (item.qty === 5) {
//             // Log frm.fields_dict to check if correctly accessed
//             console.log(frm.fields_dict);
            
//             // Set custom_nosquantity field to read-only
//             frm.set_df_property("custom_nosquantity", 'read_only', 1);
            
//             // Log message to console for debugging
//             console.log('Setting custom_nosquantity to read-only for item:', item.item_code);
            
//             // Refresh the form to apply read-only changes visually
//         }
//     }
// });
