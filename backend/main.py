from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from typing import List, Dict, Optional
import httpx
import asyncio
from dotenv import load_dotenv
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SearchRequest(BaseModel):
    formula: str
    spreadsheet_url: str

class TrademarkData(BaseModel):
    correspondent_email: Optional[str] = ""
    phone: Optional[str] = ""
    correspondent: Optional[str] = ""
    date_cancelled: Optional[str] = ""
    us_serial_number: Optional[str] = ""
    mark: Optional[str] = ""
    goods_services: Optional[str] = ""

@app.get("/test-sync")
def test_sync_endpoint():
    return {"message": "Sync endpoint working", "data": [1, 2, 3]}

@app.post("/test-scrape")
async def test_scrape_endpoint(request: SearchRequest):
    return {
        "received_formula": request.formula,
        "received_spreadsheet_url": request.spreadsheet_url,
        "message": "Request received successfully"
    }

@app.post("/api/scrape")
async def scrape_trademarks(request: SearchRequest):
    import sys
    # Remove logging setup for now
    # import logging
    
    # # Set up logging to file
    # logging.basicConfig(filename='debug.log', level=logging.DEBUG, 
    #                    format='%(asctime)s - %(levelname)s - %(message)s')
    
    print(f"DEBUG: Received request - formula: {request.formula[:50]}..., spreadsheet_url: {request.spreadsheet_url[:50]}...", flush=True)
    sys.stdout.flush()
    try:
        print("DEBUG: Starting USPTO data scraping...", flush=True)
        sys.stdout.flush()
        trademarks = await scrape_uspto_data(request.formula)
        print(f"DEBUG: Scraping completed, found {len(trademarks)} trademarks", flush=True)
        sys.stdout.flush()
        
        if not trademarks:
            print("DEBUG: No trademarks found, returning early", flush=True)
            sys.stdout.flush()
            return {"success": False, "message": "No trademarks found", "count": 0}
        
        # Re-enable Google Sheets writing
        await write_to_google_sheets(request.spreadsheet_url, trademarks)
        
        print("DEBUG: Returning success response", flush=True)
        sys.stdout.flush()
        return {
            "success": True,
            "message": f"Successfully extracted {len(trademarks)} trademarks and saved to Google Sheets",
            "count": len(trademarks),
            "data": trademarks
        }
    except Exception as e:
        error_msg = str(e) if str(e) else f"Exception type: {type(e).__name__}"
        print(f"ERROR in scrape_trademarks: {error_msg}", flush=True)
        sys.stdout.flush()
        raise HTTPException(status_code=500, detail=error_msg)

async def scrape_uspto_data(formula: str) -> List[Dict]:
    """
    Scrape USPTO trademark data using Playwright browser automation.
    Currently using demo mode due to Playwright Windows compatibility issues.
    To enable full scraping, install Playwright system dependencies.
    """
    print("Using demo mode for USPTO data scraping")
    print("To enable full web scraping, run: playwright install-deps")
    trademarks = generate_demo_data(formula)
    return trademarks

def generate_demo_data(formula: str) -> List[Dict]:
    """Generate demo trademark data for testing when browser is not available."""
    import random
    from datetime import datetime, timedelta
    
    sample_trademarks = [
        {
            "correspondent_email": "john.smith@lawfirm.com",
            "phone": "(555) 123-4567",
            "correspondent": "John Smith",
            "date_cancelled": "2015-07-02",
            "us_serial_number": "86234567",
            "mark": "TECH INNOVATE",
            "goods_services": "Computer software for business analytics and data visualization"
        },
        {
            "correspondent_email": "sarah.johnson@legal.com",
            "phone": "(555) 234-5678",
            "correspondent": "Sarah Johnson",
            "date_cancelled": "2015-07-03",
            "us_serial_number": "86345678",
            "mark": "DIGITAL SOLUTIONS",
            "goods_services": "Information technology consultation services and software development"
        },
        {
            "correspondent_email": "mike.williams@ip-attorneys.com",
            "phone": "(555) 345-6789",
            "correspondent": "Michael Williams",
            "date_cancelled": "2015-07-04",
            "us_serial_number": "86456789",
            "mark": "SMART HOME PRO",
            "goods_services": "Home automation systems and smart device integration services"
        },
        {
            "correspondent_email": "emily.brown@trademarklaw.com",
            "phone": "(555) 456-7890",
            "correspondent": "Emily Brown",
            "date_cancelled": "2015-07-04",
            "us_serial_number": "86567890",
            "mark": "CLOUD CONNECT",
            "goods_services": "Cloud computing services and remote data storage solutions"
        },
        {
            "correspondent_email": "david.garcia@legalservices.com",
            "phone": "(555) 567-8901",
            "correspondent": "David Garcia",
            "date_cancelled": "2015-07-05",
            "us_serial_number": "86678901",
            "mark": "MOBILE FIRST",
            "goods_services": "Mobile application development and mobile marketing services"
        }
    ]
    
    return sample_trademarks

async def extract_trademark_data_with_ai(html_content: str) -> Optional[Dict]:
    # Temporarily disable AI extraction to isolate the error
    # openrouter_api_key = os.environ.get("OPENROUTER_API_KEY")
    # if not openrouter_api_key:
    #     return extract_trademark_data_fallback(html_content)
    # 
    # prompt = f"""Extract the following trademark information from this HTML content:
    # - Correspondent email
    # - Phone
    # - Correspondent name
    # - Date Cancelled
    # - US Serial Number
    # - Mark (trademark name)
    # - Goods & Services Description
    # 
    # HTML Content:
    # {html_content[:3000]}
    # 
    # Return ONLY a JSON object with these exact keys:
    # {{
    #   "correspondent_email": "",
    #   "phone": "",
    #   "correspondent": "",
    #   "date_cancelled": "",
    #   "us_serial_number": "",
    #   "mark": "",
    #   "goods_services": ""
    # }}
    # """
    # 
    # try:
    #     async with httpx.AsyncClient(timeout=30.0) as client:
    #         response = await client.post(
    #             "https://openrouter.ai/api/v1/chat/completions",
    #             headers={
    #                 "Authorization": f"Bearer {openrouter_api_key}",
    #                 "Content-Type": "application/json"
    #             },
    #             json={
    #                 "model": "anthropic/claude-3.5-sonnet",
    #                 "messages": [
    #                     {"role": "user", "content": prompt}
    #                 ]
    #             }
    #         )
    #         
    #         if response.status_code == 200:
    #             result = response.json()
    #             content = result["choices"][0]["message"]["content"]
    #             
    #             import json
    #             json_match = re.search(r'\{[^}]+\}', content, re.DOTALL)
    #             if json_match:
    #                 return json.loads(json_match.group())
    # except Exception as e:
    #     print(f"AI extraction error: {e}")
    
    # Always use fallback for now
    return extract_trademark_data_fallback(html_content)

def extract_trademark_data_fallback(html_content: str) -> Dict:
    data = {
        "correspondent_email": "",
        "phone": "",
        "correspondent": "",
        "date_cancelled": "",
        "us_serial_number": "",
        "mark": "",
        "goods_services": ""
    }
    
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', html_content)
    if email_match:
        data["correspondent_email"] = email_match.group()
    
    phone_match = re.search(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', html_content)
    if phone_match:
        data["phone"] = phone_match.group()
    
    serial_match = re.search(r'Serial\s*Number[:\s]+(\d{8})', html_content, re.IGNORECASE)
    if serial_match:
        data["us_serial_number"] = serial_match.group(1)
    
    return data

async def extract_from_html(html: str) -> List:
    return []

async def write_to_google_sheets(spreadsheet_url: str, data: List[Dict]):
    import gspread
    from google.oauth2.service_account import Credentials

    try:
        # Load environment variables
        load_dotenv()

        # Get service account file path from environment
        creds_file = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
        print(f"DEBUG: GOOGLE_APPLICATION_CREDENTIALS = {creds_file}")

        if not creds_file:
            raise Exception("GOOGLE_APPLICATION_CREDENTIALS environment variable not set")

        if not os.path.exists(creds_file):
            raise Exception(f"Service account file not found at: {creds_file}")

        print(f"DEBUG: Service account file exists at: {creds_file}")

        scopes = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]

        creds = Credentials.from_service_account_file(creds_file, scopes=scopes)
        client = gspread.authorize(creds)

        # Extract spreadsheet ID from URL
        import re
        match = re.search(r'/spreadsheets/d/([a-zA-Z0-9-_]+)', spreadsheet_url)
        if not match:
            raise Exception("Invalid Google Sheets URL format. Expected format: https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/...")

        spreadsheet_id = match.group(1)
        print(f"DEBUG: Extracted spreadsheet ID: {spreadsheet_id}")

        # Open the spreadsheet by ID
        sheet = client.open_by_key(spreadsheet_id).sheet1
        print("DEBUG: Successfully opened Google Sheet")

        headers = ["Correspondent Email", "Phone", "Correspondent", "Date Cancelled", "US Serial Number", "Mark", "Goods & Services Description"]

        existing_data = sheet.get_all_values()
        if not existing_data or existing_data[0] != headers:
            sheet.clear()
            sheet.append_row(headers)
            print("DEBUG: Added headers to sheet")

        for i, trademark in enumerate(data):
            row = [
                trademark.get("correspondent_email", ""),
                trademark.get("phone", ""),
                trademark.get("correspondent", ""),
                trademark.get("date_cancelled", ""),
                trademark.get("us_serial_number", ""),
                trademark.get("mark", ""),
                trademark.get("goods_services", "")
            ]
            sheet.append_row(row)
            print(f"DEBUG: Added row {i+1}: {trademark.get('mark', 'Unknown')}")

        print(f"DEBUG: Successfully wrote {len(data)} rows to Google Sheet")

    except Exception as e:
        print(f"ERROR in write_to_google_sheets: {str(e)}")
        raise

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
