# Copyright (c) 2025, Dhwani RIS and contributors
# For license information, please see license.txt

import frappe
from frappe import _, msgprint, throw
from frappe.utils import get_url, random_string
from frappe.website.website_generator import WebsiteGenerator

from shortnr.shortnr.custom import get_qrcode


class QRCodeGenerator(WebsiteGenerator):
	def autoname(self):
		random_code = random_string(5)
		doc = frappe.get_value("QR Code Generator", {"route": random_code}, "name")
		if doc:
			frappe.throw(_("Try again, generated code is repeated on") + " " + doc.name)
		else:
			self.name = random_code

	@property
	def short_url(self):
		return get_url(self.name)

	def validate(self):
		if not (self.long_url.startswith("http") or self.long_url.startswith("upi")):
			frappe.throw(_("Please enter a proper URL or UPI"))

	def before_save(self):
		self.long_url = self.append_webform_fields_values(self.long_url)
		url_short = "".join([self.name])
		qr_code = get_url(url_short)
		logo_files = frappe.get_all(
			"File",
			fields=["name", "file_name", "file_url", "is_private"],
			filters={
				"attached_to_name": self.name,
				"attached_to_field": "logo",
				"attached_to_doctype": "QR Code Generator",
			},
		)
		logo = None
		if logo_files:
			logo = frappe.utils.get_files_path(logo_files[0].file_name, is_private=logo_files[0].is_private)

		self.qr_code = get_qrcode(qr_code, logo)
		self.published = True
		self.route = url_short

	def after_insert(self):
		"""Automatically submit after creation"""
		if self.docstatus == 0:
			self.submit()

	def append_webform_fields_values(self, url):
		params = []
		for field in self.webform_field_mapper:
			if field.value:
				params.append(f"{field.field_name}={field.value}")
		return f"{url}?{'&'.join(params)}" if params else url
