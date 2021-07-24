$(document).on('app_ready', function() {
// $(document).on('startup', function() {
//  let My_session_default_settings = getCookie("My_session_default_settings");
    if (!document.cookie.split(';').some((item) => item.includes('my_session_default_settings=yes'))) {
      // if (document.referrer.endsWith("/")) {
          // app ready after login, let's rumble
          console.log("let's set the session defaults");
          // get persistent session settings
          frappe.call({
              'method': "frappe.client.get_list",
              'args': {
                  'doctype': "Employee",
                  'filters': [[ "Employee","user_id","=",frappe.session.user ]],
                  'fields': ["company"]
              },
              'callback': function(response) {
                //console.log(response.message.length)
                  if (response.message > "0") {
                    //foreach here if there is more than 1 seting to be set
                      response.message.forEach(function (setting) {
                          console.log(setting.company);
                          // var key = setting.Key1.toLowerCase().replaceAll(" ", "_");
                          // frappe.defaults.set_user_default_local("company", setting.company);
                          frappe.call({
                                        method: 'frappe.core.doctype.session_default_settings.session_default_settings.set_session_default_values',
                                        args: {
                                                default_values: {"company":setting.company},
                                        },
                                        callback: function(data) {
                                                if (data.message == "success") {
                                                        frappe.show_alert({
                                                                'message': __('Session Defaults Saved'),
                                                                'indicator': 'green'
                                                        });
                                                        frappe.ui.toolbar.clear_cache();
                                                         document.cookie = "my_session_default_settings=yes;SameSite=Lax";
                                                }       else {
                                                        frappe.show_alert({
                                                                'message': __('An error occurred while setting Session Defaults'),
                                                                'indicator': 'red'
                                                        });
                                                }
                                        }
                                });
                      });
                  }
                  else{ // fallback to popup the setup_session_defaults
                      frappe.ui.toolbar.setup_session_defaults();
                  }
              }
          });
      }
      else {
        console.log("Session defaults is exist!");
      }
  });
