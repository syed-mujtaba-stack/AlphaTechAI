# AlphaTechAI - USPTO Trademark Scraper Setup Guide

## Congratulations! Your system is ready! 🎉

![AlphaTechAI](./attached_assets/image_1762231937857.png)

The application is now running with **DEMO MODE** enabled. You can test the system immediately with sample data, or set up Google Sheets credentials for full functionality.

---

## Google Sheets Setup (5 Minutes)

To allow the system to write data to your Google Sheets, follow these steps:

### Step 1: Create a Google Cloud Project
1. Go to: https://console.cloud.google.com/
2. Click "Select a project" → "New Project"
3. Name it "USPTO Scraper" (or anything you like)
4. Click "Create"

### Step 2: Enable Google Sheets API
1. In your new project, search for "Google Sheets API" in the search bar
2. Click on it and press "Enable"

### Step 3: Create Service Account
1. Go to "APIs & Services" → "Credentials"
2. Click "Create Credentials" → "Service Account"
3. Enter a name like "USPTO Scraper Bot"
4. Click "Create and Continue"
5. Skip the optional steps and click "Done"

### Step 4: Generate and Download Key
1. Click on the service account you just created
2. Go to the "Keys" tab
3. Click "Add Key" → "Create New Key"
4. Select "JSON" format
5. Click "Create" - a file will download

### Step 5: Add to Replit Secrets
1. Open the downloaded JSON file in a text editor
2. Copy **ALL** the content (it should start with `{` and end with `}`)
3. In Replit, go to the **Tools** panel on the left
4. Click **Secrets** (lock icon)
5. Click "+ New Secret"
6. Name: `GOOGLE_SERVICE_ACCOUNT_JSON`
7. Value: Paste the entire JSON content you copied
8. Click "Add Secret"

### Step 6: Share Your Google Sheet
1. Open your Google Sheet (or create a new one)
2. Click the "Share" button
3. In the downloaded JSON file, find the line with `"client_email"` - it looks like:
   ```
   "client_email": "something@something.iam.gserviceaccount.com"
   ```
4. Copy that email address
5. Paste it in the "Share" dialog of your Google Sheet
6. Change permission to **"Editor"**
7. Click "Send"

---

## How to Use

### Demo Mode (Available Now!)

The system is currently running in **DEMO MODE**, which means:
- ✅ You can test the complete workflow immediately
- ✅ Sample trademark data will be generated and saved to Google Sheets
- ✅ No browser dependencies required
- ⚠️ Real USPTO scraping requires additional system setup (see note below)

**To test the demo:**
1. **Open the application** (it's already running in the Webview!)
2. **Enter any USPTO search formula**, for example:
   ```
   CD:[2015-07-01 TO 2015-07-05] AND EN:INDIVIDUAL OW:USA
   ```
3. **Paste your Google Sheets URL** (like `https://docs.google.com/spreadsheets/d/...`)
4. **Click "Start Extraction"**
5. The system will generate 5 sample trademarks and save them to your sheet!

### Full Mode (Real USPTO Scraping)

For real USPTO data scraping, you need:
- System dependencies for Playwright browser automation
- This works automatically on most systems, but may require manual setup on Replit

The system will automatically fall back to demo mode if browser dependencies aren't available.

---

## What Data Gets Extracted?

The system extracts these fields for each trademark:
- ✅ Correspondent Email
- ✅ Phone Number
- ✅ Correspondent Name
- ✅ Date Cancelled
- ✅ US Serial Number
- ✅ Mark (Trademark Name)
- ✅ Goods & Services Description

---

## Troubleshooting

**"Google Sheets credentials not found"**
→ Make sure you added `GOOGLE_SERVICE_ACCOUNT_JSON` to Replit Secrets

**"Permission denied on Google Sheets"**
→ Share your Google Sheet with the service account email (from the JSON file)

**"No trademarks found"**
→ Check your search formula on the USPTO website first to verify it returns results

---

## Need Help?

Check the README.md file for more detailed information!
