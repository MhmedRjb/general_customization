import frappe

DELIVERD="Deliverd"
CANCLED="Sales Cancled"
BILLED="Billed"
import frappe
def sales_invoice(doc, method):
    for item in doc.items:
        if item.delivery_note:
            delivery_note = frappe.get_doc("Delivery Note", item.delivery_note)
            delivery_note.workflow_state =BILLED
            delivery_note.save(ignore_permissions=True)
            frappe.db.commit()
        
def cancel_sales_invoice(doc, method):
    for item in doc.items:
        if item.delivery_note:
            delivery_note = frappe.get_doc("Delivery Note", item.delivery_note)
            delivery_note.workflow_state =CANCLED
            delivery_note.save(ignore_permissions=True)
            frappe.db.commit()



def purchase_invoice(doc, method):
    for item in doc.items:
        frappe.msgprint("Purchase Invoice")
        frappe.msgprint("Purchase Invoice")
        frappe.msgprint("Purchase Invoice")
        
        if item.purchase_receipt:
            delivery_note = frappe.get_doc("Purchase Receipt", item.purchase_receipt)
            delivery_note.workflow_state =BILLED
            delivery_note.save(ignore_permissions=True)
            frappe.db.commit()
        
        
def cancel_purchase_invoice(doc, method):
    for item in doc.items:
        if item.purchase_receipt:
            delivery_note = frappe.get_doc("Purchase Receipt", item.purchase_receipt)
            delivery_note.workflow_state =CANCLED
            delivery_note.save(ignore_permissions=True)
            frappe.db.commit()
