# AlphaTechAI - USPTO Trademark Scraper

## Overview
AlphaTechAI's intelligent automation platform for extracting USPTO cancelled trademark data and saving to Google Sheets using AI-powered data extraction (Claude 3.5 Sonnet via OpenRouter).

## Current State
- Project structure created with FastAPI backend and Next.js frontend
- OpenRouter API integration configured for AI-powered data extraction
- Google Sheets integration ready (requires service account setup by user)
- Playwright configured for web scraping

## Recent Changes
- November 04, 2025: Complete project implementation with AlphaTechAI branding
  - ✅ Rebranded to AlphaTechAI with custom logo
  - ✅ Created FastAPI backend with USPTO scraping endpoints
  - ✅ Built Next.js frontend with beautiful UI
  - ✅ Integrated OpenRouter API (Claude 3.5 Sonnet) for AI extraction
  - ✅ Implemented demo mode fallback for testing without browser dependencies
  - ✅ Configured Google Sheets API integration
  - ✅ Created comprehensive GitHub-ready README.md
  - ✅ Added detailed setup instructions
  - ⚠️ Playwright browser automation available (falls back to demo mode in Replit due to system dependencies)

## User Preferences
- Language: Urdu/English mix (conversational)
- Use case: Office workflow automation for USPTO trademark data
- Specific data fields required:
  - Correspondent email
  - Phone
  - Correspondent name
  - Date Cancelled
  - US Serial Number
  - Mark (trademark name)
  - Goods & Services Description

## Project Architecture

### Backend (FastAPI - Python)
- **Port**: 8000
- **Main endpoint**: `/api/scrape`
- **Key features**:
  - Playwright-based web scraping
  - OpenRouter AI integration for intelligent data extraction
  - Google Sheets API integration for data storage
  - Fallback regex-based extraction if AI fails

### Frontend (Next.js - TypeScript)
- **Port**: 5000
- **Framework**: Next.js 15 with App Router
- **Styling**: Tailwind CSS
- **Key features**:
  - Formula input form
  - Google Sheets URL input
  - Progress tracking
  - Results display

### Dependencies
- Backend: FastAPI, Playwright, gspread, google-auth, httpx
- Frontend: Next.js, React, Tailwind CSS, Axios
- System: Chromium browser dependencies for Playwright

## Environment Setup
- **OPENROUTER_API_KEY**: ✅ Configured
- **GOOGLE_SERVICE_ACCOUNT_JSON**: ⏳ Requires user setup (see SETUP_INSTRUCTIONS.md)
- **Playwright Browser**: ⚠️ Demo mode active (browser dependencies require system-level packages)

## Current Status
- ✅ Application fully functional in DEMO MODE
- ✅ Can be tested immediately with sample data
- ✅ Google Sheets integration ready (needs user credentials)
- ✅ GitHub-ready with comprehensive documentation
- ✅ AlphaTechAI branding complete

## Next Steps for User
1. Set up Google Sheets service account (follow SETUP_INSTRUCTIONS.md)
2. Test demo mode with sample data
3. For production use on a server with full browser support, deploy outside Replit
4. Optional: Fork and customize for specific needs
