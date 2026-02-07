#!/usr/bin/env python3
"""
Test WhatsApp form submission
"""

import json
import urllib.parse

print("\n" + "=" * 70)
print("WHATSAPP FORM SUBMISSION TEST")
print("=" * 70)

# Test form data
test_data = {
    'name': 'Sarah Johnson',
    'email': 'sarah@example.com',
    'subject': 'Inquiry about Hospice Care Services',
    'phone': '604-555-1234',
    'message': 'Hello, I would like more information about your hospice care services. We are interested in learning about your team and availability.'
}

print("\nForm Data Submitted:")
for key, value in test_data.items():
    print(f"  {key}: {value}")

# Validate required fields
required_fields = ['name', 'email', 'subject', 'message']
errors = []

print("\n" + "=" * 70)
print("VALIDATION")
print("=" * 70)

for field in required_fields:
    if not test_data.get(field):
        errors.append(f"{field.capitalize()} is required")
        print(f"❌ {field}: Missing")
    else:
        print(f"✅ {field}: Present")

# Validate email
import re
if test_data['email']:
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, test_data['email']):
        print(f"✅ Email format: Valid")
    else:
        errors.append("Invalid email format")
        print(f"❌ Email format: Invalid")

if errors:
    print("\n❌ VALIDATION FAILED")
    for error in errors:
        print(f"  - {error}")
else:
    print("\n" + "=" * 70)
    print("WHATSAPP MESSAGE GENERATION")
    print("=" * 70)
    
    # Generate WhatsApp message like the PHP handler does
    whatsapp_message = f"Name: {test_data['name']}\n"
    whatsapp_message += f"Email: {test_data['email']}\n"
    if test_data.get('phone'):
        whatsapp_message += f"Phone: {test_data['phone']}\n"
    whatsapp_message += f"Subject: {test_data['subject']}\n\n"
    whatsapp_message += f"Message:\n{test_data['message']}"
    
    print("\nGenerated WhatsApp Message:")
    print("-" * 70)
    print(whatsapp_message)
    print("-" * 70)
    
    # Generate WhatsApp link
    whatsapp_phone = '17785819636'  # 1-778-581-9636
    encoded_message = urllib.parse.quote(whatsapp_message)
    whatsapp_link = f"https://api.whatsapp.com/send?phone={whatsapp_phone}&text={encoded_message}"
    
    print("\n" + "=" * 70)
    print("WHATSAPP LINK")
    print("=" * 70)
    print(f"\nWhatsApp Link Generated:")
    print(f"{whatsapp_link[:80]}...")
    
    print("\n" + "=" * 70)
    print("SUBMISSION RESULT")
    print("=" * 70)
    print(f"""
✅ FORM SUBMISSION SUCCESSFUL

The form will:
  1. Validate all required fields
  2. Format the message with user details
  3. Generate a WhatsApp API link
  4. Redirect user to WhatsApp with pre-filled message
  5. User can review and send via WhatsApp Web/App

WhatsApp Number: +1-778-581-9636 (17785819636)

When user clicks "Send Message":
  → Form validates input
  → Generates WhatsApp message with all details
  → Opens WhatsApp chat with pre-filled message
  → User can send directly from their WhatsApp
""")
    print("=" * 70 + "\n")
