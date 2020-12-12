def start_session_defaults(login_manager):
    # allocate free credits to frappe.session.user
    # frappe.ui.toolbar.setup_session_defaults();
    console.log(frappe.ui.toolbar.setup_session_defaults());
