// // a js code to fetch customer balance in sales invoice
// frappe.ui.form.on('Sales Invoice', {
//     customer: function(frm) {
//         console.log(frm.doc.customer_name,"customer");
//         if (frm.doc.customer) {
//             frappe.call(
//                 {
//                     method: "erpnext.accounts.utils.get_balance_on",
//                     args: {
//                         party_type: "Customer",
//                         party: frm.doc.customer
//                     },
//                     callback: function(response) {
//                         console.log(response.message);
//                         if (response.message) {
//                             frm.set_value("party_balance", response.message);
//                         }
//                     }

//                 }
//             )

//         }

//     }
// })
