import frappe
@frappe.whitelist(allow_guest=True)
def get_balance_pos():
    total_sales = frappe.db.get_all("POS Invoice", 
        filters={
            "status": ["not in", ["Draft", "Consolidated", "Cancelled"]],
            "docstatus": 1
        }, 
        fields=["name"]
    )

    total_payment = frappe.db.get_all("Sales Invoice Payment",
        fields=["amount"], 
        filters={
            "parenttype": "POS Invoice", 
            "parent": ["in", [x.name for x in total_sales]]
        }
    )

    sum_total_payment = sum([x.amount for x in total_payment])
    return sum_total_payment