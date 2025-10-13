app_name = "shortnr"
app_title = "ShortNR"
app_publisher = "Bhushan Barbuddhe"
app_description = "ShortNR is a lightweight and powerful Frappe app that lets you easily create short URLs and QR codes directly from your Frappe desk."
app_email = "frappeteam@dhwaniris.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "shortnr",
# 		"logo": "/assets/shortnr/logo.png",
# 		"title": "ShortNR",
# 		"route": "/shortnr",
# 		"has_permission": "shortnr.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/shortnr/css/shortnr.css"
# app_include_js = "/assets/shortnr/js/shortnr.js"

# include js, css files in header of web template
# web_include_css = "/assets/shortnr/css/shortnr.css"
# web_include_js = "/assets/shortnr/js/shortnr.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "shortnr/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "shortnr/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "shortnr.utils.jinja_methods",
# 	"filters": "shortnr.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "shortnr.install.before_install"
# after_install = "shortnr.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "shortnr.uninstall.before_uninstall"
# after_uninstall = "shortnr.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "shortnr.utils.before_app_install"
# after_app_install = "shortnr.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "shortnr.utils.before_app_uninstall"
# after_app_uninstall = "shortnr.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "shortnr.notifications.get_notification_config"

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
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"shortnr.tasks.all"
# 	],
# 	"daily": [
# 		"shortnr.tasks.daily"
# 	],
# 	"hourly": [
# 		"shortnr.tasks.hourly"
# 	],
# 	"weekly": [
# 		"shortnr.tasks.weekly"
# 	],
# 	"monthly": [
# 		"shortnr.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "shortnr.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "shortnr.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "shortnr.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["shortnr.utils.before_request"]
# after_request = ["shortnr.utils.after_request"]

# Job Events
# ----------
# before_job = ["shortnr.utils.before_job"]
# after_job = ["shortnr.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"shortnr.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
