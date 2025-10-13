# Frappe Shortner

A comprehensive Frappe app for generating short URLs and QR codes with advanced webform integration and dynamic field mapping.

## 🚀 Features

- **URL Shortening**: Convert long URLs into short, shareable links
- **QR Code Generation**: Create styled QR codes with custom logos and designs
- **Webform Integration**: Dynamic field mapping from Frappe webforms
- **Offline Support**: Generate QR codes without internet connectivity

## 📋 Requirements

- Frappe Framework (v14+)
- Python 3.8+
- PIL/Pillow for image processing
- qrcode library for QR generation

## 🛠️ Installation

### Using Bench CLI

```bash
# Navigate to your bench directory
cd $PATH_TO_YOUR_BENCH

# Get the app from repository
bench get-app https://github.com/dhwani-ris/frappe_shortnr.git --branch develop

# Install the app
bench install-app shortnr

# Migrate database
bench migrate
```

### Manual Installation

```bash
# Clone the repository
git clone https://github.com/dhwani-ris/frappe_shortnr.git apps/shortnr

# Install dependencies
cd apps/shortnr
pip install -r requirements.txt

# Install the app
bench install-app shortnr
```

## 🎯 Usage

### 1. URL Shortening

1. Navigate to **QR Code Generator** doctype
2. Select **Type** as "URL Shortener"
3. Enter your **Long URL**
4. Click **Save** to generate short URL
5. Copy the generated **Short URL**

### 2. QR Code Generation

#### Basic QR Code
1. Select **Type** as "QR Code"
2. Enter the data to encode
3. Click **Save** to generate QR code
4. View the **QR Preview**

#### Styled QR Code with Logo
1. Upload a **Logo** image
2. The QR code will automatically include your logo
3. Custom styling includes:
   - Radial gradient color masks
   - Gapped square module drawers
   - Square eye drawers

### 3. Webform Integration

#### Setup Webform Mapping
1. Select **Type** as "Webform"
2. Choose your **Webform** from the dropdown
3. The app automatically fetches webform fields
4. Fields are organized into:
   - **Complex Fields**: Text areas, tables, file uploads (2-column layout)
   - **Simple Fields**: Input fields, selects, dates (4-column layout)

#### Dynamic Field Rendering
- Fields are automatically categorized by type
- Complex fields get more space in 2-column layout
- Simple fields are efficiently arranged in 4-column layout
- Fixed-width columns with justified alignment
- Responsive design for mobile devices

## 🔧 Configuration

### QR Code Settings

The app uses the following default QR code settings:
- **Version**: 7 (supports up to 1,816 characters)
- **Box Size**: 6 pixels
- **Border**: 3 modules
- **Error Correction**: High (30% error recovery)


## 🔌 API Reference

### Custom Functions

#### `get_qrcode(input_data, logo)`
Generates a styled QR code with optional logo embedding.

**Parameters:**
- `input_data` (str): Data to encode in QR code
- `logo` (str, optional): Path to logo image

**Returns:**
- Base64 encoded PNG image data URL

#### `get_webform_fields(webform)`
Fetches webform fields for dynamic rendering.

**Parameters:**
- `webform` (str): Webform name

**Returns:**
- List of field dictionaries with fieldname, label, fieldtype, options


## 🚨 Troubleshooting

### Common Issues

#### QR Code Not Generating
- Check if PIL/Pillow is installed: `pip install Pillow`
- Verify qrcode library: `pip install qrcode[pil]`
- Check file permissions for logo uploads

#### Webform Fields Not Loading
- Ensure webform exists and is published
- Check field permissions in webform
- Verify webform field types are supported

#### Layout Issues
- Clear browser cache
- Check for JavaScript console errors
- Verify CSS classes are not conflicting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


Made with ❤️ by the Dhwani RIS team
