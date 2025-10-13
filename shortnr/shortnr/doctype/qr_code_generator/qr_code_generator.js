// Keep controls outside frm.doc
let dynamic_controls = {};

frappe.ui.form.on("QR Code Generator", {
	webform(frm) {
		if (!frm.doc.webform) return;

		frappe.call({
			method: "shortnr.shortnr.custom.get_webform_fields",
			args: { webform: frm.doc.webform },
			callback: function (r) {
				if (!r.message) return;

				// reset child table + html area
				frm.clear_table("webform_field_mapper");
				let wrapper = frm.fields_dict.dynamic_inputs_html.wrapper;
				$(wrapper).empty();
				dynamic_controls = {}; // reset cache
				console.log(r.message);
				// Separate fields by type for different layouts
				let complex_fields = [];
				let simple_fields = [];

				r.message.forEach((df) => {
					if (_is_complex_field(df.fieldtype)) {
						complex_fields.push(df);
					} else {
						simple_fields.push(df);
					}
				});

				// Create 2-column section for complex fields
				if (complex_fields.length > 0) {
					let complex_section =
						$(`<div class="form-section" style="margin-bottom: 20px; margin-left: 20px;">
					</div>`).appendTo(wrapper);

					let complex_container = $(
						`<div class="row" style="display: flex; justify-content: space-between; flex-wrap: wrap;"></div>`
					).appendTo(complex_section);
					let complex_current_row = null;
					let complex_field_count = 0;

					complex_fields.forEach((df) => {
						// add row in child table
						let row = frm.add_child("webform_field_mapper");
						row.field_label = df.label;
						row.field_name = df.fieldname;
						row.field_type = df.fieldtype;
						row.options = df.options || "";

						// Create new row every 2 fields
						if (complex_field_count % 2 === 0) {
							complex_current_row = $(
								`<div class="row" style="display: flex; justify-content: space-between; margin-bottom: 15px; width: 100%;"></div>`
							).appendTo(complex_container);
						}

						// Create column wrapper with fixed width 2-column layout
						let field_wrapper = $(
							`<div style="width: 48%; margin-bottom: 12px; flex-shrink: 0;"></div>`
						).appendTo(complex_current_row);

						// make control
						let control = frappe.ui.form.make_control({
							df: {
								fieldname: df.fieldname,
								label: df.label,
								fieldtype: df.fieldtype || "Data",
								options: df.options || "",
							},
							parent: field_wrapper,
							render_input: true,
						});
						control.refresh();

						control.on_change = () => {
							row.value = control.get_value();
						};

						// store control in memory map (not in row)
						dynamic_controls[row.name] = control;
						complex_field_count++;
					});
				}

				// Create 4-column section for simple fields
				if (simple_fields.length > 0) {
					let simple_section =
						$(`<div class="form-section" style="margin-bottom: 20px; margin-left: 20px;">
					</div>`).appendTo(wrapper);

					let simple_container = $(
						`<div class="row" style="display: flex; justify-content: space-between; flex-wrap: wrap;"></div>`
					).appendTo(simple_section);
					let simple_current_row = null;
					let simple_field_count = 0;

					simple_fields.forEach((df) => {
						// add row in child table
						let row = frm.add_child("webform_field_mapper");
						row.field_label = df.label;
						row.field_name = df.fieldname;
						row.field_type = df.fieldtype;
						row.options = df.options || "";

						// Create new row every 4 fields
						if (simple_field_count % 4 === 0) {
							simple_current_row = $(
								`<div class="row" style="display: flex; justify-content: space-between; margin-bottom: 15px; width: 100%;"></div>`
							).appendTo(simple_container);
						}

						// Create column wrapper with fixed width 4-column layout
						let field_wrapper = $(
							`<div style="width: 23%; margin-bottom: 12px; flex-shrink: 0;"></div>`
						).appendTo(simple_current_row);

						// make control
						let control = frappe.ui.form.make_control({
							df: {
								fieldname: df.fieldname,
								label: df.label,
								fieldtype: df.fieldtype || "Data",
								options: df.options || "",
							},
							parent: field_wrapper,
							render_input: true,
						});
						control.refresh();

						control.on_change = () => {
							row.value = control.get_value();
						};

						// store control in memory map (not in row)
						dynamic_controls[row.name] = control;
						simple_field_count++;
					});
				}

				frm.refresh_field("webform_field_mapper");
			},
		});
	},

	before_save(frm) {
		// final sync
		(frm.doc.webform_field_mapper || []).forEach((row) => {
			if (dynamic_controls[row.name]) {
				row.value = dynamic_controls[row.name].get_value();
			}
		});
	},

	refresh(frm) {
		_render_qr_preview(frm);
		_rebuild_dynamic_inputs(frm);
	},
});

/*
 * Helper: QR Preview
 */
function _render_qr_preview(frm) {
	let template = frm.doc.__islocal
		? '<img src="" />'
		: '<img src="' + (frm.doc.qr_code || "") + '" width="240px"/>';
	frm.set_df_property("qr_preview", "options", frappe.render_template(template));
	frm.refresh_field("qr_preview");
}

function _rebuild_dynamic_inputs(frm) {
	if (frm.doc.webform_field_mapper && frm.doc.webform_field_mapper.length > 0) {
		let wrapper = frm.fields_dict.dynamic_inputs_html.wrapper;
		$(wrapper).empty();
		dynamic_controls = {}; // reset

		// Separate fields by type for different layouts
		let complex_fields = [];
		let simple_fields = [];

		frm.doc.webform_field_mapper.forEach((row) => {
			if (_is_complex_field(row.field_type)) {
				complex_fields.push(row);
			} else {
				simple_fields.push(row);
			}
		});

		// Create 2-column section for complex fields
		if (complex_fields.length > 0) {
			let complex_section =
				$(`<div class="form-section" style="margin-bottom: 20px; margin-left: 20px;">
				<h5 style="margin-bottom: 15px; color: #6c757d;">Complex Fields</h5>
			</div>`).appendTo(wrapper);

			let complex_container = $(
				`<div class="row" style="display: flex; justify-content: space-between; flex-wrap: wrap;"></div>`
			).appendTo(complex_section);
			let complex_current_row = null;
			let complex_field_count = 0;

			complex_fields.forEach((row) => {
				// Create new row every 2 fields
				if (complex_field_count % 2 === 0) {
					complex_current_row = $(
						`<div class="row" style="display: flex; justify-content: space-between; margin-bottom: 15px; width: 100%;"></div>`
					).appendTo(complex_container);
				}

				// Create column wrapper with fixed width 2-column layout
				let field_wrapper = $(
					`<div style="width: 48%; margin-bottom: 12px; flex-shrink: 0;"></div>`
				).appendTo(complex_current_row);

				let control = frappe.ui.form.make_control({
					df: {
						fieldname: row.field_name,
						label: row.field_label,
						fieldtype: row.field_type || "Data",
						options: row.options || "",
					},
					parent: field_wrapper,
					render_input: true,
				});
				control.refresh();

				// set saved value into control
				if (row.value) {
					control.set_value(row.value);
				}

				// keep control synced with row
				control.on_change = () => {
					row.value = control.get_value();
				};

				dynamic_controls[row.name] = control;
				complex_field_count++;
			});
		}

		// Create 4-column section for simple fields
		if (simple_fields.length > 0) {
			let simple_section =
				$(`<div class="form-section" style="margin-bottom: 20px; margin-left: 20px;">
				<h5 style="margin-bottom: 15px; color: #6c757d;">Simple Fields</h5>
			</div>`).appendTo(wrapper);

			let simple_container = $(
				`<div class="row" style="display: flex; justify-content: space-between; flex-wrap: wrap;"></div>`
			).appendTo(simple_section);
			let simple_current_row = null;
			let simple_field_count = 0;

			simple_fields.forEach((row) => {
				// Create new row every 4 fields
				if (simple_field_count % 4 === 0) {
					simple_current_row = $(
						`<div class="row" style="display: flex; justify-content: space-between; margin-bottom: 15px; width: 100%;"></div>`
					).appendTo(simple_container);
				}

				// Create column wrapper with fixed width 4-column layout
				let field_wrapper = $(
					`<div style="width: 23%; margin-bottom: 12px; flex-shrink: 0;"></div>`
				).appendTo(simple_current_row);

				let control = frappe.ui.form.make_control({
					df: {
						fieldname: row.field_name,
						label: row.field_label,
						fieldtype: row.field_type || "Data",
						options: row.options || "",
					},
					parent: field_wrapper,
					render_input: true,
				});
				control.refresh();

				// set saved value into control
				if (row.value) {
					control.set_value(row.value);
				}

				// keep control synced with row
				control.on_change = () => {
					row.value = control.get_value();
				};

				dynamic_controls[row.name] = control;
				simple_field_count++;
			});
		}
	}
}

function _is_complex_field(fieldtype) {
	const complex_types = [
		"Text",
		"Small Text",
		"Long Text",
		"Code",
		"HTML Editor",
		"Table",
		"Child Table",
		"Table MultiSelect",
		"Attach",
		"Attach Image",
		"Image",
		"File",
		"Signature",
		"Geolocation",
		"Duration",
	];
	return complex_types.includes(fieldtype);
}
