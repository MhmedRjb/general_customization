//cahnge list view of delivery note
frappe.listview_settings['Delivery Note'] = {
    add_fields: ["workflow_state"],
    get_indicator: function(doc) {


        if (doc.docstatus == 2) {
            return [__("ألغيت"), "grey", "docstatus,=,2"];
        
        } else if (doc.workflow_state == "Billed") {
            return [__("سُلمت وفوترت"), "green", "workflow_state,=,Deliverd"];

        } else if (doc.workflow_state == "Sales Cancled") {
          return [__(" سلمت وألغيت الفاتورة"), "blue", "workflow_state,=,Deliverd"];

          } else if (doc.docstatus == 1) {
            return [__("سُلمت"), "orange", "docstatus,=,1"];
            
        } else {
            return [__("غير معلوم"), "gray", "workflow_state,=,Deliverd"];
        }
    }
};