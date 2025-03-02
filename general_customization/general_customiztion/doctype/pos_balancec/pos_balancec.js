frappe.ui.form.on('POS Balancec', {
    check: function(frm) {
        frappe.call({
            method: 'general_customization.general_customiztion.doctype.pos_balancec.utility.get_balance_pos',
            callback: function(r) {
                if (r.message) {
                    frm.set_value('balance', r.message);
                }
            }
        });
    }
});