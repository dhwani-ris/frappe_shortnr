# Copyright (c) 2021, PibiCo and contributors
# For license information, please see license.txt

import base64
from io import BytesIO

import frappe
import qrcode
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import HorizontalGradiantColorMask, ImageColorMask, RadialGradiantColorMask, SquareGradiantColorMask, VerticalGradiantColorMask
from qrcode.image.styles.moduledrawers import CircleModuleDrawer, GappedSquareModuleDrawer, HorizontalBarsDrawer, RoundedModuleDrawer, SquareModuleDrawer, VerticalBarsDrawer


def _create_qr_code(input_data):
	qr = qrcode.QRCode(version=7, box_size=6, border=3, error_correction=qrcode.constants.ERROR_CORRECT_H)
	qr.add_data(input_data)
	qr.make(fit=True)
	return qr


def _get_color_mask():
	return RadialGradiantColorMask(
		back_color=(255, 255, 255), center_color=(70, 130, 180), edge_color=(0, 0, 0)
	)


def _create_qr_image(qr, logo=None):
	common_params = {
		"image_factory": StyledPilImage,
		"color_mask": _get_color_mask(),
		"module_drawer": GappedSquareModuleDrawer(),
		"eye_drawer": SquareModuleDrawer(),
	}

	if logo:
		common_params["embeded_image_path"] = logo

	return qr.make_image(**common_params)


def _encode_image_to_base64(img):
	temp = BytesIO()
	img.save(temp, "PNG")
	temp.seek(0)
	b64 = base64.b64encode(temp.read())
	return "data:image/png;base64,{0}".format(b64.decode("utf-8"))


def get_qrcode(input_data, logo):
	qr = _create_qr_code(input_data)
	img = _create_qr_image(qr, logo)
	return _encode_image_to_base64(img)


@frappe.whitelist()
def get_webform_fields(webform):
	if not webform:
		return []

	exclude = ["Column Break", "Section Break", "Page Break", "HTML", "Heading", "Fold"]
	fields = frappe.get_all(
		"Web Form Field",
		filters={
			"parent": webform,
			"fieldtype": ["not in", exclude],
		},
		fields=["fieldname", "label", "fieldtype", "options"],
	)

	# Ensure options is always a string
	for f in fields:
		f["options"] = f.get("options") or ""
	return fields
