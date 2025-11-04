<div align="center">

![AlphaTechAI Logo](./attached_assets/image_1762231937857.png)

# AlphaTechAI - USPTO Trademark Scraper

### 🤖 AI-Powered Trademark Data Extraction

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Next.js](https://img.shields.io/badge/Next.js-15.0-black.svg)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Automate your USPTO trademark research workflow with AI-powered data extraction and seamless Google Sheets integration.**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Tech Stack](#-tech-stack) • [Contributing](#-contributing)

</div>

---

## 📋 Overview

AlphaTechAI's USPTO Trademark Scraper is an intelligent automation tool that eliminates hours of manual data entry by automatically extracting cancelled trademark information from the USPTO database and saving it directly to Google Sheets.

### 💡 The Problem

Manually copying trademark data from USPTO's public database is:
- ⏰ **Time-consuming** - Each record takes 2-3 minutes to copy manually
- 😓 **Error-prone** - Human errors in data entry
- 🔁 **Repetitive** - Same process for hundreds of records daily
- 📊 **Inefficient** - No easy way to organize and analyze data

### ✨ The Solution

AlphaTechAI automates the entire workflow:
1. **Enter your search formula** (e.g., `CD:[2015-07-01 TO 2015-07-05] AND EN:INDIVIDUAL OW:USA`)
2. **Provide your Google Sheets URL**
3. **Click "Start Extraction"**
4. **Done!** ☕ Grab a coffee while AI does the work

---

## 🚀 Features

### Core Capabilities

- 🤖 **AI-Powered Extraction** - Uses Claude 3.5 Sonnet via OpenRouter for intelligent data parsing
- 🌐 **Automated Web Scraping** - Playwright-based browser automation
- 📊 **Google Sheets Integration** - Direct export to your spreadsheets
- 🎯 **Smart Data Parsing** - Extracts 7 key trademark fields accurately
- 🔄 **Batch Processing** - Handle multiple records in one go
- 💾 **Auto-Save** - Data saved automatically as it's extracted
- 🎨 **Beautiful UI** - Clean, modern interface built with Next.js and Tailwind CSS
- ⚡ **Real-time Progress** - Live updates during extraction

### Extracted Data Fields

| Field | Description |
|-------|-------------|
| 📧 Correspondent Email | Contact email address |
| 📞 Phone | Phone number |
| 👤 Correspondent | Correspondent name |
| 📅 Date Cancelled | Cancellation date |
| 🔢 US Serial Number | Trademark serial number |
| ™️ Mark | Trademark name/text |
| 📝 Goods & Services | Full description |

---

## 🎬 Demo

### Interface Preview

The application features a clean, intuitive interface:

1. **Search Formula Input** - Enter your USPTO search query
2. **Google Sheets URL** - Provide your spreadsheet link
3. **One-Click Extraction** - Start the automated process
4. **Progress Tracking** - Real-time status updates
5. **Results Display** - Preview extracted data

### Example Search Formulas

```
# Cancelled trademarks by individuals in USA (July 2015)
CD:[2015-07-01 TO 2015-07-05] AND EN:INDIVIDUAL OW:USA

# Specific date range and entity type
CD:[2020-01-01 TO 2020-12-31] AND EN:CORPORATION

# Multiple criteria
CD:[2015-01-01 TO 2015-12-31] AND EN:INDIVIDUAL AND OW:California
```

---

## 🛠️ Installation

### Prerequisites

- Python 3.11+
- Node.js 20+
- Google Cloud Service Account (for Sheets API)
- OpenRouter API Key

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/syed-mujtaba-stack/AlphaTechAI.git
   cd AlphaTechAI
   ```

2. **Install backend dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   python -m playwright install chromium
   ```

3. **Install frontend dependencies**
   ```bash
   cd frontend
   npm install
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the backend directory:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key
   GOOGLE_SERVICE_ACCOUNT_JSON=your_service_account_json
   ```

5. **Run the application**
   
   Terminal 1 - Backend:
   ```bash
   cd backend
   python main.py
   ```
   
   Terminal 2 - Frontend:
   ```bash
   cd frontend
   npm run dev
   ```

6. **Open your browser**
   ```
   http://localhost:5000
   ```

---

## 📖 Usage

### Step 1: Google Sheets Setup

1. Create a Google Cloud project at https://console.cloud.google.com/
2. Enable Google Sheets API
3. Create a Service Account and download the JSON key
4. Share your Google Sheet with the service account email
5. Add the JSON content to your environment variables

**Detailed instructions**: See [SETUP_INSTRUCTIONS.md](./SETUP_INSTRUCTIONS.md)

### Step 2: Run a Search

1. Open the application in your browser
2. Enter your USPTO search formula
3. Paste your Google Sheets URL
4. Click "Start Extraction"
5. Monitor progress in real-time
6. Check your Google Sheet for results!

### Step 3: Analyze Your Data

Your extracted data is now in Google Sheets, ready for:
- 📊 Analysis and reporting
- 📈 Trend identification
- 📧 Mail merge campaigns
- 🔍 Further research
- 💼 Business intelligence

---

## 🏗️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **Playwright** - Browser automation
- **OpenRouter** - AI model access (Claude 3.5 Sonnet)
- **Google Sheets API** - Data persistence
- **gspread** - Python Google Sheets library
- **Pydantic** - Data validation

### Frontend
- **Next.js 15** - React framework with App Router
- **React 19** - UI library
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Axios** - HTTP client

### Infrastructure
- **Python 3.11** - Backend runtime
- **Node.js 20** - Frontend runtime
- **Chromium** - Browser for scraping

---

## 📁 Project Structure

```
alphatechai-uspto-scraper/
├── backend/
│   ├── main.py                    # FastAPI application
│   ├── setup_google_sheets.py     # Google Sheets setup helper
│   └── requirements.txt           # Python dependencies
├── frontend/
│   ├── app/
│   │   ├── page.tsx              # Main UI component
│   │   ├── layout.tsx            # Layout wrapper
│   │   └── globals.css           # Global styles
│   ├── public/
│   │   └── logo.png              # AlphaTechAI logo
│   ├── package.json              # Node dependencies
│   └── tsconfig.json             # TypeScript config
├── attached_assets/
│   └── image_1762231937857.png   # Logo asset
├── README.md                      # This file
├── SETUP_INSTRUCTIONS.md          # Detailed setup guide
└── replit.md                      # Project documentation
```

---

## 🔒 Security & Privacy

- ✅ Service account authentication for Google Sheets
- ✅ Environment variables for sensitive data
- ✅ No data stored on servers
- ✅ Direct browser-to-Sheets data flow
- ✅ CORS protection
- ✅ Input validation and sanitization

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💻 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔀 Open a Pull Request

### Development Guidelines

- Follow PEP 8 for Python code
- Use ESLint and Prettier for TypeScript/JavaScript
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed

---

## 🐛 Known Issues & Limitations

- Browser dependencies required for Playwright (handled automatically on most systems)
- Rate limiting may apply for large batch operations
- USPTO website structure changes may require selector updates
- Maximum 50 records per extraction (configurable)

---

## 🗺️ Roadmap

- [ ] Support for multiple USPTO databases
- [ ] Excel export option
- [ ] Scheduled automated searches
- [ ] Email notifications on completion
- [ ] Advanced filtering and sorting
- [ ] Data visualization dashboard
- [ ] Multi-language support
- [ ] Mobile app version

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- USPTO for providing public trademark data
- OpenRouter for AI API access
- Google for Sheets API
- Playwright team for browser automation tools
- Next.js and FastAPI communities

---

## 📧 Contact & Support

- **GitHub Issues**: [Report a bug](https://github.com/yourusername/alphatechai-uspto-scraper/issues)
- **Discussions**: [Ask questions](https://github.com/yourusername/alphatechai-uspto-scraper/discussions)
- **Email**: support@alphatechai.com

---

<div align="center">

**Made with ❤️ by AlphaTechAI**

⭐ Star us on GitHub if this project helped you!

[⬆ Back to Top](#alphatechai---uspto-trademark-scraper)

</div>
