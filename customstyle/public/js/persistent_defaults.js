$(document).on('app_ready', function() {
      if (document.referrer.endsWith("/login")) {
          // app ready after login, let's rumble
          console.log("let's rumble");
          // get persistent session settings
          frappe.call({
              'method': "frappe.client.get_list",
              'args': {
                  'doctype': "Persistent Session Setting",
                  'filters': [[ "UsersDoc","user","in",frappe.session.user ]],
                  // {'users': frappe.session.user},
                  'fields': ["company"]
              },
              'callback': function(response) {
                  if (response.message) {
                      response.message.forEach(function (setting) {
                          //console.log(setting.company);
                          // var key = setting.Key1.toLowerCase().replaceAll(" ", "_");
                          frappe.defaults.set_user_default_local("company", setting.company);
                      });
                  }
              }
          });
      }
  });
