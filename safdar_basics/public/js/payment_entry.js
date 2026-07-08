frappe.ui.form.on('Payment Entry', {
    onload: function(frm) {
        set_sales_person_from_customer(frm);
    },

    refresh: function(frm) {
        set_sales_person_from_customer(frm);
    },

    party_type: function(frm) {
        // Clear the field if party_type is not Customer
        if (frm.doc.party_type !== 'Customer') {
            frm.set_value('custom_sales_person', '');
        }
    },

    party: function(frm) {
        set_sales_person_from_customer(frm);
    }
});

function set_sales_person_from_customer(frm) {
    // Only proceed if party_type is Customer and party is set
    if (frm.doc.party_type !== 'Customer' || !frm.doc.party) {
        return;
    }

    frappe.db.get_doc('Customer', frm.doc.party).then(customer_doc => {
        if (customer_doc.sales_team && customer_doc.sales_team.length > 0) {
            let sales_person = customer_doc.sales_team[0].sales_person;
            frm.set_value('custom_sales_person', sales_person);
        } else {
            frm.set_value('custom_sales_person', '');
        }
    });
}