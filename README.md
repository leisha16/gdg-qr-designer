# 🎨 GDG QR Studio — Interactive QR Code Generator & Designer

>

> **Domain:** Frontend Development  
> **Task:** QR Code Generator & Designer

---

## 🔗 Project Links

| Resource | Link |
|---|---|
| 🌐 **Live Demo** | [Open GDG QR Studio](https://gdg-qr-designer.vercel.app/) |
| 💻 **GitHub Repository** | [View Source Code](https://github.com/leisha16/gdg-qr-designer) |
| 🚀 **Vercel Project** | [View Deployment on Vercel](https://vercel.com/leisha3/gdg-qr-designer) |

---

# 🌟 Overview

**GDG QR Studio** is a modern, interactive, browser-based QR Code Generator and Designer

The application allows users to generate, customize, preview, and download QR codes in real time without requiring a dedicated backend server for QR generation.

The application supports multiple QR data types, advanced visual customization, predefined presets, QR history, input validation, responsive design, and several additional enhancements.

---

# 🎯 Project Objective

The objective of this project is to provide a simple yet powerful QR Code Generator that allows users to create QR codes for different types of information and customize their appearance while maintaining readability and scan reliability.

The application focuses on:

- Ease of use
- Real-time preview
- Flexible customization
- QR scan reliability
- Client-side processing
- Responsive design
- Easy exporting
- Local persistence

---

# ✨ Features

## 1. ⚡ Real-Time QR Code Generation

The application generates QR codes dynamically as users enter or modify information.

### Features

- Real-time QR generation
- Instant live preview
- Dynamic updates
- Adjustable resolution
- Browser-based QR generation
- No backend required for QR generation

Changes made to the input or customization settings are reflected immediately in the preview.

---

# 2. 📦 Multiple QR Data Types

GDG QR Studio supports multiple types of QR data.

## 🌐 URL

Users can generate QR codes for websites and links.

### Features

- HTTP / HTTPS support
- URL validation
- Protocol handling
- Real-time preview

Example:

```text
https://gdgsrm.com
```

---

## 📄 Plain Text

Users can encode normal text into a QR code.

### Features

- Multi-line text
- Live character count
- Instant QR generation

Example:

```text
Welcome to GDG on Campus SRM!
```

---

## ✉️ Email

Users can generate QR codes containing email information.

### Supported fields

- Email address
- Subject
- Message body

The information is converted into a `mailto:` payload.

Example:

```text
mailto:test@example.com
```

---

## 📞 Phone Number

Users can generate QR codes for phone numbers.

The application converts the phone number into a suitable telephone payload.

Example:

```text
tel:+919876543210
```

---

## 📶 Wi-Fi

Users can generate QR codes that contain Wi-Fi connection information.

### Supported fields

- Network name / SSID
- Authentication type
- Password
- Hidden network option

### Authentication options

- WPA / WPA2 / WPA3
- WEP
- Open

The information is encoded using the standard Wi-Fi QR format.

Example:

```text
WIFI:S:NetworkName;T:WPA;P:Password;H:false;;
```

---

## 📇 Contact Card

The application also supports contact card QR codes.

### Supported fields

- Name
- Organization
- Role
- Phone number
- Email
- Website

The information is compiled into a vCard-compatible QR payload.

---

# 3. 🎨 QR Code Customization

Users can customize the visual appearance of their QR codes.

### Customization options

- QR resolution
- Foreground color
- Background color
- Transparent background
- Error correction level
- Margin / quiet zone
- QR pattern
- Corner square style
- Corner dot style
- Gradient
- Logo
- Logo size
- Logo margin

All customization changes are reflected immediately in the live preview.

---

# 4. 📐 QR Resolution

Users can choose different output resolutions.

### Available resolutions

- 280px
- 340px
- 512px
- 1024px

This allows QR codes to be generated for different use cases, from normal digital sharing to high-resolution applications.

---

# 5. 🎨 Foreground & Background Colors

Users can customize both QR foreground and background colors.

### Supported options

- Custom foreground color
- Custom background color
- Color palettes
- Transparent background support

The preview updates immediately whenever colors are changed.

---

# 6. 📏 Margin / Quiet Zone

Users can control the spacing around the QR code.

The application provides adjustable margin settings to help maintain sufficient spacing around the QR code and improve scanning reliability.

---

# 7. 🧩 Error Correction Levels

The application provides multiple QR error correction levels.

| Level | Approximate Recovery |
|---|---:|
| L | ~7% |
| M | ~15% |
| Q | ~25% |
| H | ~30% |

Higher error correction levels can help maintain QR readability when additional visual elements such as logos are used.

---

# 8. 🎭 Visual Presets

The application includes predefined visual presets for quickly creating styled QR codes.

### Included presets

- **Classic Sharp**
- **Google & GDG Signature**
- **Cyberpunk Neon**
- **Emerald Forest**
- **Sunset Horizon**
- **Royal Velvet**

Presets remain editable after selection.

Users can continue modifying:

- Colors
- Patterns
- Gradients
- Logo
- Error correction
- Margins
- Other visual settings

---

# 9. 📥 PNG Download

Users can download generated QR codes as PNG images.

The exported image is generated directly in the browser and is designed to match the selected preview resolution.

The application also generates descriptive filenames based on the QR payload/type.

Example:

```text
gdg-qr-wifi-1727600000.png
```

---

# 10. 🧾 SVG Download

As an additional enhancement, the application supports SVG export.

SVG is useful for:

- Posters
- Printing
- Branding
- Presentations
- Large-scale designs
- Professional graphics

Because SVG is vector-based, it can be scaled without the same pixelation limitations as raster images.

---

# 11. ✅ Input Validation

The application performs client-side validation for supported QR types.

### Validation includes

- URL validation
- Email validation
- Phone number validation
- Required field validation
- Wi-Fi SSID validation
- Incomplete input detection

The application displays useful warnings when the entered information is invalid or incomplete.

---

# 12. 📊 Scan Reliability & Contrast Analysis

QR code customization should not compromise readability.

GDG QR Studio includes contrast and scan-reliability feedback.

The application analyzes the relationship between the foreground and background colors and provides a visual status.

### Scannability states

- 🟢 Optimal
- 🟢 Good
- 🟡 Fair
- 🔴 Poor / Warning

The application can warn users when their selected customization may negatively affect QR readability.

When visual elements such as logos are used, higher error correction can also be recommended.

---

# 13. 💾 Recent QR Codes

The application stores recently generated QR configurations locally using browser `localStorage`.

### History functionality

- Save recent QR codes
- Restore previous QR configurations
- Preserve styling settings
- Delete individual history items
- Clear complete history
- Persist history after page refresh

This allows users to return to previously generated QR designs without having to recreate them.

---

# 14. 📱 Responsive Design

GDG QR Studio is designed to work across different screen sizes.

## Desktop

The desktop interface provides:

- QR configuration controls
- Live preview
- Customization settings
- History
- Additional controls

## Mobile

The interface adapts into a stacked layout for smaller screens.

The application is designed for:

- Desktop
- Laptop
- Tablet
- Mobile

---

# 🚀 Optional Enhancements

In addition to the core requirements, the application includes several additional features.

---

## 1. 🧾 SVG Vector Download

Users can export QR codes as scalable SVG files.

This is useful for:

- Printing
- Posters
- Branding
- High-resolution graphics
- Professional use

---

## 2. 🖼️ Center Logo & Branding

The application supports QR code branding using logos.

### Logo functionality

- Built-in logo presets
- Custom logo upload
- Logo size adjustment
- Logo margin adjustment
- Clear dots behind logo

Built-in branding options include examples such as:

- Google
- GDG on Campus
- GitHub
- Wi-Fi
- Website
- Email
- Phone

---

## 3. 🌈 Gradient QR Codes

Users can create gradient QR codes.

### Gradient features

- Linear gradients
- Radial gradients
- Multiple color stops
- Adjustable gradient angle

The gradient controls allow users to create more visually appealing QR codes while still monitoring scan reliability.

---

## 4. 📋 Copy to Clipboard

The application supports copying generated QR images directly to the clipboard where supported by the browser.

It uses the browser Clipboard API and provides a fallback for copying the QR payload when image clipboard functionality is unavailable.

---

## 5. 🔵 Custom QR Patterns

Users can customize the QR pattern.

### Body patterns

Available styles include:

- Square
- Dots
- Rounded
- Extra Rounded
- Classy
- Classy Rounded

### Corner styles

Users can customize:

- Corner squares
- Corner dots
- Outer eye patterns
- Inner eye patterns

This provides additional control over the appearance of the generated QR code.

---

## 6. 🌙 Dark / Light Mode

The application supports:

- Dark mode
- Light mode

The selected theme can be persisted locally.

The application can also respect the user's system color preference.

---

# 🛠️ Technology Stack

## ⚛️ React

React is used to build the interactive user interface.

It provides efficient state management and allows the QR preview to update dynamically when the user changes inputs or customization settings.

---

## 🎨 Tailwind CSS

Tailwind CSS is used for responsive UI development.

It provides:

- Responsive layouts
- Utility-based styling
- Dark mode support
- Consistent spacing
- Responsive components

---

## 🔲 qr-code-styling

The `qr-code-styling` library is used for QR generation and visual customization.

It provides functionality for:

- QR rendering
- Custom dot patterns
- Gradients
- Logos
- Canvas output
- SVG output

---

## 🖼️ HTML5 Canvas

HTML5 Canvas is used for browser-based QR rendering and raster image generation.

---

## 🔷 SVG

SVG is used for scalable vector QR output and vector downloads.

---

## 🟨 JavaScript

JavaScript handles:

- Application logic
- Input validation
- QR payload generation
- State management
- Local storage
- User interactions
- Download functionality
- Clipboard functionality

---

## ⚡ Vite

Vite is used as the development and build tool.

It provides:

- Fast development
- Modern frontend workflow
- Production builds
- Easy deployment

---

## 🟢 Node.js & npm

Node.js and npm are used for:

- Dependency management
- Local development
- Build scripts
- Package management

---

# 📁 Project Structure

```text
gdg-qr-designer/
│
├── .vscode/
│   └── settings.json
│
├── screenshots/
│   ├── Screenshot 2026-10-04 201212.png
│   ├── Screenshot 2026-10-04 201251.png
│   ├── Screenshot 2026-10-04 201305.png
│   └── Screenshot 2026-10-04 201502.png
│
├── .gitignore
├── index.html
├── package.json
├── README.md
├── netlify.toml
├── vercel.json
├── vite.config.js
├── serve.py
└── test_app.py
```

---

# 💻 Running the Project Locally

## Method 1 — Python HTTP Server

If Python is installed, the application can be served using Python's built-in HTTP server.

Open a terminal in the project directory:

```bash
cd gdg-qr-designer
```

Run:

```bash
python -m http.server 3000
```

Then open:

```text
http://localhost:3000
```

in your browser.

---

# Method 2 — Vite Development Server

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Vite will provide a local development URL, usually:

```text
http://localhost:5173
```

---

# 🌐 Deployment

## Vercel

The project is configured for deployment using Vercel.

### Deployment process

1. The project is stored in a public GitHub repository.
2. The GitHub repository is connected to Vercel.
3. Vercel builds and deploys the project.
4. Future pushes to the connected repository can trigger new deployments.

### Vercel Project

🚀 [View GDG QR Studio on Vercel](https://vercel.com/leisha3/gdg-qr-designer)

### Live Application

🌐 **Add your public `.vercel.app` URL here:**

```text
YOUR-PUBLIC-VERCEL-URL
```

---

# 🔄 Updating the Project

After making changes locally, use Git to update the GitHub repository:

```bash
git add .
```

Then create a commit:

```bash
git commit -m "Update project"
```

Finally push the changes:

```bash
git push
```

If the GitHub repository is connected to Vercel, the updated project can then be deployed automatically.

---

# 📸 Screenshots

## 🖥️ Desktop Studio View

![GDG QR Studio Desktop View](screenshots/Screenshot%202026-10-04%20201212.png)

---

## 🎨 QR Customization

![QR Customization](screenshots/Screenshot%202026-10-04%20201251.png)

---

## ⚙️ QR Generator Features

![QR Generator Features](screenshots/Screenshot%202026-10-04%20201305.png)

---

## 📱 History / Responsive Interface

![QR History and Responsive Interface](screenshots/Screenshot%202026-10-04%20201502.png)

---

# 🧪 Testing & Verification

The application was tested across the major functionality included in the project.

## QR Type Testing

Tested QR generation for:

- URL
- Plain Text
- Email
- Phone
- Wi-Fi
- Contact Card

---

## Customization Testing

Tested:

- QR resolution
- Foreground color
- Background color
- Error correction
- Margin
- Visual presets
- QR patterns
- Gradients
- Logos

---

## Export Testing

Tested:

- PNG download
- SVG download
- Clipboard copy

---

## Validation Testing

Tested:

- Invalid URLs
- Invalid email addresses
- Invalid phone numbers
- Missing required fields
- Invalid Wi-Fi information

---

## Persistence Testing

Tested:

- Recent QR history
- Page refresh
- Restoring previous QR configurations
- Deleting history entries
- Clearing history

---

## Responsive Testing

Tested across:

- Desktop
- Laptop
- Tablet-sized layouts
- Mobile-sized layouts

---

# 📋 Feature Checklist

| Feature | Status |
|---|---|
| QR Code Generation | ✅ |
| Real-Time QR Preview | ✅ |
| URL QR | ✅ |
| Plain Text QR | ✅ |
| Email QR | ✅ |
| Phone QR | ✅ |
| Wi-Fi QR | ✅ |
| Contact Card QR | ✅ |
| QR Resolution Customization | ✅ |
| Foreground Color | ✅ |
| Background Color | ✅ |
| Margin / Padding | ✅ |
| Error Correction | ✅ |
| Visual Presets | ✅ |
| PNG Download | ✅ |
| Input Validation | ✅ |
| Scan Reliability Feedback | ✅ |
| Recent QR Codes | ✅ |
| Local Persistence | ✅ |
| Responsive Design | ✅ |
| SVG Download | ✅ |
| Logo Support | ✅ |
| Gradient QR Codes | ✅ |
| Clipboard Copy | ✅ |
| Custom QR Patterns | ✅ |
| Dark / Light Mode | ✅ |

---

# 🔐 Client-Side Architecture

The application is designed to perform QR generation and customization directly in the browser.

### General flow

```text
User Input
    ↓
Input Validation
    ↓
QR Payload Generation
    ↓
QR Styling & Customization
    ↓
Real-Time QR Preview
    ↓
Contrast / Reliability Feedback
    ↓
Export / Copy / Save
```

This architecture reduces the need for a backend server for the core QR generation functionality.

---

# 💾 Local Data Persistence

Recent QR configurations and theme preferences can be stored using browser `localStorage`.

This allows the application to maintain selected information between page refreshes.

No external database is required for the local history functionality.

---

# 🎯 Design Goals

The main design goals of GDG QR Studio were:

### 1. Simplicity

Users should be able to create a QR code without needing technical knowledge.

### 2. Real-Time Feedback

Changes should be visible immediately.

### 3. Customization

Users should have control over the visual appearance of their QR codes.

### 4. Reliability

Customization should not unnecessarily compromise QR readability.

### 5. Responsiveness

The application should remain usable across different devices.

### 6. Client-Side Processing

Core QR generation functionality should work directly within the browser.

---

# 🎓 Academic Integrity

The project repository contains the source code, documentation, deployment configuration, and screenshots required for evaluation.



---

# 📌 Project Information

### Organization

**Google Developer Groups on Campus SRM**

### Recruitment

**Technical Domain Recruitment 2026–27**

### Domain

**Frontend Development**

### Task

**QR Code Generator & Designer**

### GitHub Repository

🔗 [github.com/leisha16/gdg-qr-designer](https://github.com/leisha16/gdg-qr-designer)

### Vercel Project

🔗 [vercel.com/leisha3/gdg-qr-designer](https://vercel.com/leisha3/gdg-qr-designer)



# ❤️ GDG QR Studio

### Interactive QR Code Generator & Designer



**Generate. Customize. Preview. Scan. 🚀**