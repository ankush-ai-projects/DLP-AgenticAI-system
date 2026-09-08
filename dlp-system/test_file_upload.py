"""
File Upload Test Script
Run: python test_file_upload.py
"""
import requests
import json

BASE_URL = "http://localhost:8001/api/v1"

# Step 1: Login
print("🔐 Logging in...")
login_response = requests.post(
    f"{BASE_URL}/auth/login",
    data={
        "username": "ankush",
        "password": "Test@1234"
    }
)

if login_response.status_code != 200:
    print(f"❌ Login failed: {login_response.text}")
    exit(1)

token = login_response.json()["access_token"]
print(f"✅ Token received: {token[:20]}...")

# Step 2: Upload TXT file
print("\n📄 Uploading TXT file...")
with open("test_data/sample_pii.txt", "rb") as f:
    txt_response = requests.post(
        f"{BASE_URL}/scans/upload",
        headers={"Authorization": f"Bearer {token}"},
        files={"file": ("sample_pii.txt", f, "text/plain")}
    )

if txt_response.status_code == 200:
    result = txt_response.json()
    print(f"✅ TXT Scan Complete!")
    print(f"   Total Findings: {result['total_findings']}")
    print(f"   Risk Summary: {json.dumps(result['risk_summary'], indent=2)}")
    print(f"\n   Findings:")
    for finding in result['findings'][:5]:  # First 5
        print(f"   - {finding['entity_type']}: {finding['value']} (confidence: {finding['confidence']:.2f})")
else:
    print(f"❌ TXT Upload failed: {txt_response.text}")

# Step 3: Upload CSV file
print("\n📊 Uploading CSV file...")
with open("test_data/sample_pii.csv", "rb") as f:
    csv_response = requests.post(
        f"{BASE_URL}/scans/upload",
        headers={"Authorization": f"Bearer {token}"},
        files={"file": ("sample_pii.csv", f, "text/csv")}
    )

if csv_response.status_code == 200:
    result = csv_response.json()
    print(f"✅ CSV Scan Complete!")
    print(f"   Total Findings: {result['total_findings']}")
    print(f"   Risk Summary: {json.dumps(result['risk_summary'], indent=2)}")
else:
    print(f"❌ CSV Upload failed: {csv_response.text}")

# Step 4: Get scan history
print("\n📜 Fetching scan history...")
history_response = requests.get(
    f"{BASE_URL}/scans/history/me",
    headers={"Authorization": f"Bearer {token}"}
)

if history_response.status_code == 200:
    history = history_response.json()
    print(f"✅ Total Scans: {history['total']}")
    print(f"\n   Recent Scans:")
    for scan in history['scans'][:3]:
        print(f"   - ID: {scan['id']}, File: {scan['filename']}, Risk: {scan['risk_level']}")
else:
    print(f"❌ History fetch failed: {history_response.text}")

print("\n🎉 Test Complete!")
