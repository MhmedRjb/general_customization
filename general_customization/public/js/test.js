frappe.ui.form.on('Sales Invoice', {
    // Customer field change event handler
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
    },
    onload_post_render: function(frm) {
        // Bind the event handler only once
        if (!frm.has_item_focus_handler) {
            frm.has_item_focus_handler = true;
            frm.fields_dict.items.grid.wrapper.on("focus", "div.frappe-control.form-group", function(e) {
                toggle_nosquantity_editability(frm);
            });
        }
        frm.trigger('refresh_items');
    },
    refresh: function(frm) {
        frm.trigger('refresh_items');
    },
    refresh_items: function(frm) {
        toggle_nosquantity_editability(frm);
    },
    items_add: function(frm) {
        toggle_nosquantity_editability(frm);
    },
    items_remove: function(frm) {
        toggle_nosquantity_editability(frm);
    }
});

function toggle_nosquantity_editability(frm) {
    $.each(frm.doc.items, function(i, d) {
        let grid_row = frm.fields_dict['items'].grid.grid_rows_by_docname[d.name];
        if (d.qty === 5) {
            grid_row.toggle_editable('custom_nosquantity', false);
        } else {
            grid_row.toggle_editable('custom_nosquantity', true);
        }
    });
}
