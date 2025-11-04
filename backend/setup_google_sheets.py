import os
import json

def setup_google_sheets_credentials():
    """
    Setup Google Sheets credentials from environment or file
    """
    creds_json = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")
    
    if creds_json:
        try:
            creds = json.loads(creds_json)
            print("✓ Google Sheets credentials found in environment")
            return True
        except json.JSONDecodeError:
            print("✗ Invalid JSON in GOOGLE_SERVICE_ACCOUNT_JSON")
            return False
    
    if os.path.exists("service-account.json"):
        print("✓ Found service-account.json file")
        with open("service-account.json", "r") as f:
            os.environ["GOOGLE_SERVICE_ACCOUNT_JSON"] = f.read()
        return True
    
    print("\n" + "="*60)
    print("GOOGLE SHEETS SETUP REQUIRED")
    print("="*60)
    print("\nTo use Google Sheets integration:")
    print("1. Go to https://console.cloud.google.com/")
    print("2. Create a new project or select existing one")
    print("3. Enable Google Sheets API")
    print("4. Create a Service Account")
    print("5. Download the JSON key file")
    print("6. Either:")
    print("   - Set GOOGLE_SERVICE_ACCOUNT_JSON environment variable with the JSON content")
    print("   - Or save the file as 'service-account.json' in the backend directory")
    print("\nNote: Share your Google Sheet with the service account email")
    print("="*60 + "\n")
    
    return False

if __name__ == "__main__":
    setup_google_sheets_credentials()
