frappe.ui.form.on('Sales Invoice', {
 
    refresh: function(frm) {
        if (frm.doc.is_return && frm.doc.__islocal) {
            frm.set_value('update_billed_amount_in_delivery_note', 0);
            frm.set_value('update_outstanding_for_self', 0);
        }
    },
    is_return: function(frm) {
        frm.set_value('update_billed_amount_in_delivery_note', 0);
    }
});