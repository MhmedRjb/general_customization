import frappe

def update_purchase_receipt(doc, method):
    pass
    # for item in doc.items:
    #     frappe.msgprint(item.purchase_receipt)

    #     if item.purchase_receipt:
    #         frappe.msgprint(item.purchase_receipt)
    #         purchase_receipt = frappe.get_doc("Purchase Receipt", item.purchase_receipt)
    #         purchase_receipt.status = "Closed"
    #         # ignore not update after submit
    #         purchase_receipt.save(ignore_permissions=True)
    #         frappe.db.commit()