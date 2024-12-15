import frappe
def delivery_note(doc, method):
    for item in doc.items:
        frappe.msgprint("Item has been delivered1")
        if item.si_detail:
            frappe.msgprint("Item has been delivered")
            doc.custom_state ="Approved"
            doc.save()
            frappe.db.commit()
        
            
