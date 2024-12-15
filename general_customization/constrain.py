import frappe

def delivery_note(doc, method):
    for item in doc.items:
        if item.rate == 0:
            item.rate = 20
            doc.save(ignore_permissions=True)
            frappe.db.commit()
            frappe.msgprint("Rate has been updated")