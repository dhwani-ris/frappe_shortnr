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

## 📁 File Structure

```
shortnr/
├── shortnr/
│   ├── doctype/
│   │   ├── qr_code_generator/
│   │   │   ├── qr_code_generator.json
│   │   │   ├── qr_code_generator.py
│   │   │   ├── qr_code_generator.js
│   │   │   └── test_qr_code_generator.py
│   │   └── webform_url_mapper/
│   │       ├── webform_url_mapper.json
│   │       └── webform_url_mapper.py
│   ├── custom.py
│   ├── hooks.py
│   └── modules.txt
├── requirements.txt
└── README.md
```

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
bench run-tests --app shortnr

# Run specific test file
bench run-tests --app shortnr --doctype "QR Code Generator"

# Run with coverage
bench run-tests --app shortnr --coverage
```

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

## 🎨 Customization

### Adding New QR Styles

1. Import new style modules in `custom.py`:
```python
from qrcode.image.styles.moduledrawers import YourCustomDrawer
from qrcode.image.styles.colormasks import YourCustomColorMask
```

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


## 🤝 Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/shortnr
pre-commit install
```

### Pre-commit Tools

- **ruff**: Python linting and formatting
- **eslint**: JavaScript linting
- **prettier**: Code formatting
- **pyupgrade**: Python syntax upgrades

### Development Workflow

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Run tests: `bench run-tests --app shortnr`
5. Commit with pre-commit: `git commit -m "Add your feature"`
6. Push to your fork
7. Create a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For support and questions:
- **Email**: bhushan.barbuddhe@dhwaniris.com
- **Issues**: [GitHub Issues](https://github.com/dhwani-ris/frappe_shortnr/issues)
- **Documentation**: [Readme](https://github.com/dhwani-ris/frappe_shortnr/)

## 🏢 Publisher

**Dhwani RIS**
- Website: [dhwaniris.com](https://dhwaniris.com/)
- Email: bhushan.barbuddhe@dhwaniris.com

---

Made with ❤️ by the Dhwani RIS team
