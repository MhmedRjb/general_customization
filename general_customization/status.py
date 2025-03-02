import frappe
def delivery_note(doc, method):
    for item in doc.items:
        if item.si_detail:
            frappe.msgprint("Item has been delivered")
            doc.workflow_state ="Approved"
            doc.save(ignore_permissions=True)
            frappe.db.commit()
        
            
