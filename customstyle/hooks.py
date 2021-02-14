# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "customstyle"
app_title = "Customstyle"
app_publisher = "Michael F"
app_description = "for erpnext custom styles"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "michaeleino@hotmail.com"
app_license = "MIT"

#app_include_css = "assets/customstyle/css/custom.css"
app_include_css = "/assets/css/custom_app.css"
app_include_js = "/assets/js/custom_app.js"



# boot_session = "customstyle.overrides.start_session_defaults"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/customstyle/css/customstyle.css"
# app_include_js = "/assets/customstyle/js/customstyle.js"

# include js, css files in header of web template
# web_include_css = "/assets/customstyle/css/customstyle.css"
# web_include_js = "/assets/customstyle/js/customstyle.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "customstyle.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "customstyle.install.before_install"
# after_install = "customstyle.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "customstyle.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"customstyle.tasks.all"
# 	],
# 	"daily": [
# 		"customstyle.tasks.daily"
# 	],
# 	"hourly": [
# 		"customstyle.tasks.hourly"
# 	],
# 	"weekly": [
# 		"customstyle.tasks.weekly"
# 	]
# 	"monthly": [
# 		"customstyle.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "customstyle.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "customstyle.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "customstyle.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]
