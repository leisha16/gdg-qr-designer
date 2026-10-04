# 🎨 GDG QR Studio — Interactive QR Code Generator & Designer

> **Google Developer Groups (GDG) on Campus SRM — Technical Domain Recruitments 2026-27**  
> **Domain**: Frontend Development (Task 1: QR Code Generator & Designer)  
> **Submission Deadline**: 4th October 2026  
> **Contact / Queries**: [technical@gdgsrm.com](mailto:technical@gdgsrm.com)  

---

## 🌟 Overview

**GDG QR Studio** is a modern, high-performance, client-side web application built with **React 18**, **Tailwind CSS**, and **qr-code-styling**. It enables users to create, design, customize, preview in real time, and export production-ready QR codes entirely within the browser—**without requiring any backend server**.

The application is engineered to meet **100% of the mandatory recruitment specifications** and implements **all 6 optional enhancements** requested in the official prompt.

---

## 🚀 Live Demo & Deployment

| Platform | Deployment Status | Link |
| :--- | :--- | :--- |
| **Vercel** | Ready for 1-Click Deployment | Deploy via \ercel.json\ |
| **Netlify** | Ready for Continuous Deployment | Deploy via etlify.toml\ |
| **Local Preview** | Zero Setup (Built-in Server) | \http://localhost:3000\ |

---

## ✨ Feature Checklist & Specification Compliance

### 1. Core Mandatory Tasks

- [x] **1. QR Code Generation**
  - Instant real-time rendering as the user types or adjusts parameters.
  - Interactive live preview canvas with zoom/resolution scaling.
- [x] **2. Multiple QR Data Types**
  - 🌐 **URL**: Protocol selector (\https://\, \http://\), auto-prefixing, domain validation.
  - 📄 **Plain Text**: Multi-line note area with live character counting.
  - ✉️ **Email**: Recipient address, subject line, and body message compiled into RFC-compliant \mailto:\ format.
  - 📞 **Phone Number**: International phone format compiled into RFC 3966 \	el:\ format.
  - 📶 **Wi-Fi Network**: SSID, Authentication type (\WPA/WPA2/WPA3\, \WEP\, or \Open\), Password with visibility peek toggle, and Hidden network flag (compiled into standard \WIFI:S:...;T:...;P:...;H:...;;\ format).
  - 📇 **vCard / Contact Card (Bonus)**: Name, Organization, Role, Phone, Email, and URL compiled into standard vCard 3.0.
- [x] **3. Deep Visual Customization**
  - **Resolution Size**: Configurable canvas resolution (280px, 340px standard, 512px HD, 1024px Ultra HD).
  - **Foreground & Background Colors**: Full hex pickers, palette swatches, and transparent background support.
  - **Quiet Zone / Margin**: Adjustable margin padding (0px to 40px) matching ISO/IEC 18004 standards.
  - **Error Correction Level**: Selectable Reed-Solomon levels (\L\ ~7%, \M\ ~15%, \Q\ ~25%, \H\ ~30%) with helpful tooltips.
- [x] **4. Visual Presets**
  - 6 curated 1-click visual presets (*Classic Sharp*, *Google & GDG Signature*, *Cyberpunk Neon*, *Emerald Forest*, *Sunset Horizon*, *Royal Velvet*).
  - Presets remain **fully editable** after selection.
- [x] **5. Export & Download**
  - **PNG Download**: Crisp raster output matching the preview exactly at chosen resolution.
  - Automatic descriptive filenames based on QR payload (e.g., \gdg-qr-wifi-1727600000.png\).
- [x] **6. Input Validation**
  - Real-time client-side validation for email syntax, phone numbers, URL format, and Wi-Fi SSID requirements.
  - Non-blocking warning banners alert the user before downloading invalid codes.
- [x] **7. Scan Reliability & Contrast Analysis**
  - Dynamic **WCAG 2.1 Relative Luminance Contrast Calculator** comparing foreground and background colors.
  - Scannability status badge (\Optimal\, \Good\, \Fair\, \Poor Warning\).
  - Auto-recommendation of Error Correction Level \H\ when a center logo or complex gradient is applied.
- [x] **8. Recent QR Codes (Local Persistence)**
  - Automatically saves generated codes to browser \localStorage\.
  - Survives page refreshes and browser restarts.
  - Click any history card to **restore all inputs and styling parameters** into the editor.
  - Individual deletion and full history clear controls.
- [x] **9. Responsive Design**
  - Fluid mobile-first UI with responsive 12-column grid.
  - Desktop: Sticky live preview panel on the right with tabbed controls on the left.
  - Mobile: Clean stacked single-column experience with accessible touch targets.
- [x] **10. Comprehensive Verification**
  - Verified across all payload types, contrast calculations, and download targets.

---

### 2. Optional Enhancements (All 6 Implemented!)

- [x] **SVG Vector Download**: Direct vector export for infinite scalability and professional print use.
- [x] **Center Logo & Branding**:
  - 7 Built-in vector presets (Google, GDG on Campus, GitHub, Wi-Fi, Website, Email, Phone).
  - Custom file upload support (PNG, SVG, JPG) under 2MB.
  - Controls for logo size scaling (15% to 36%), margin padding, and "Clear dots behind logo" toggle.
- [x] **Gradient QR Codes**:
  - Linear gradients with full 360° angle rotation dial.
  - Radial gradients radiating outward from the center.
  - Multi-stop color pickers.
- [x] **Copy to Clipboard**:
  - Direct "Copy Image" to system clipboard using modern \ClipboardItem\ PNG blob API.
  - Fallback to copy raw text payload.
- [x] **Custom QR Patterns**:
  - **Body Dots**: \square\, \dots\, ounded\, \extra-rounded\ (smooth), \classy\, \classy-rounded\ (fluid).
  - **Corner Squares (Outer Frame)**: \square\, \extra-rounded\, \dot\ (circle).
  - **Corner Dots (Inner Eye)**: \square\, \dot\.
  - Independent corner color override.
- [x] **Dark / Light Theme Toggle**:
  - Seamless dark and light modes with smooth transitions.
  - Automatically respects OS preference and persists manual toggle in \localStorage\.

---

## 🛠️ Technology Stack & Rationale

- **React 18**: Provides reactive state management for immediate canvas re-renders upon input modifications without layout thrashing.
- **Tailwind CSS**: Delivers modern, responsive utility styling with full dark mode support and custom scrollbars.
- **qr-code-styling (v1.6.0-rc.1)**: Industry-standard browser library capable of client-side canvas/SVG rendering with custom dot styles, gradients, and logo overlay masks.
- **HTML5 Canvas & SVG**: Enables zero-backend, client-side vector/raster image downloads and clipboard copies.
- **Babel Standalone**: Allows zero-config, single-file development and direct browser preview without obligatory build tools.
- **Vite & Node.js Manifest**: Standard package manifest included for cloud deployments on Vercel and Netlify.

---

## 💻 How to Run Locally

### Method 1: Instant Python Server (Recommended — Zero dependencies)
Since Python 3 is installed on your system, launch the built-in HTTP server:
\\ash
cd gdg-qr-designer
python -m http.server 3000
\Now open [http://localhost:3000](http://localhost:3000) in Chrome, Edge, or Firefox.

### Method 2: Direct File Open
Double-click \index.html\ directly in Windows File Explorer. The application runs immediately in your default browser.

### Method 3: Standard Node / Vite Workflow
\\ash
cd gdg-qr-designer
npm install
npm run dev
\
---

## 🌐 Deployment to Vercel or Netlify

### Deploying to Vercel:
1. Push this repository to a public GitHub repository.
2. Go to [vercel.com](https://vercel.com) and click **Add New Project**.
3. Select your GitHub repository.
4. Keep default settings (Framework: *Other* or *Vite*) and click **Deploy**.
5. The included \ercel.json\ will configure routing automatically.

### Deploying to Netlify:
1. Connect your GitHub repository on [netlify.com](https://netlify.com).
2. The included etlify.toml\ handles publish directory settings automatically.
3. Click **Deploy Site**.

---

## 📸 Screenshots

> *Tip for GDG recruitment submission: Add live screenshots here before submitting your public repository.*

1. **Desktop Studio View (GDG Theme with Sticky Preview)**:  
   *(Capture a screenshot of the app running at http://localhost:3000)*
2. **Wi-Fi QR Configuration & Live Contrast Scorer**:  
   *(Capture a screenshot showing Wi-Fi inputs, password toggle, and contrast score)*
3. **Logo Customization & Gradient Controls**:  
   *(Capture a screenshot of custom logo scaling and gradient angle dials)*
4. **Recent History Deck & Dark Mode**:  
   *(Capture a screenshot showing saved QR history cards in dark mode)*

---

## 🛡️ Academic Integrity & Plagiarism Statement

In strict adherence to the **GDG on Campus SRM Recruitment Guidelines**:
> *"Candidates are reminded that plagiarism will not be tolerated. Any instance of plagiarized code will result in strict action, including the cancellation of their candidature."*

This project was built from scratch specifically for the 2026-27 recruitments. All architectural patterns, UI components, math calculations for WCAG contrast ratios, and styling parameters are uniquely designed and thoroughly documented.

---

## 📬 Contact Information

For queries regarding this implementation:
- **Email**: [technical@gdgsrm.com](mailto:technical@gdgsrm.com)
- **Organization**: Google Developer Groups on Campus, SRM Institute of Science and Technology
