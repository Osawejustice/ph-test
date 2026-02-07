#!/usr/bin/env python3
"""
Form submission test script for OpenHearts Homecare contact form
"""

import json
import sys

# Simulate form data
test_data = {
    'name': 'John Doe',
    'email': 'john@example.com',
    'subject': 'Test Inquiry',
    'message': 'This is a test message from the form.',
    'phone': '1-555-123-4567'
}

print("=" * 60)
print("FORM SUBMISSION TEST")
print("=" * 60)
print("\nForm Data:")
for key, value in test_data.items():
    print(f"  {key}: {value}")

# Validate required fields
required_fields = ['name', 'email', 'subject', 'message']
errors = []

print("\n" + "=" * 60)
print("VALIDATION RESULTS")
print("=" * 60)

for field in required_fields:
    if field not in test_data or not test_data[field]:
        errors.append(f"{field.capitalize()} is required")
        print(f"❌ {field}: Missing")
    else:
        print(f"✅ {field}: Valid")

# Validate email format
if test_data['email']:
    import re
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, test_data['email']):
        print(f"✅ email format: Valid")
    else:
        errors.append("Please enter a valid email")
        print(f"❌ email format: Invalid")

print("\n" + "=" * 60)
print("SUBMISSION STATUS")
print("=" * 60)

if errors:
    print("\n❌ SUBMISSION FAILED")
    print("\nErrors:")
    for error in errors:
        print(f"  - {error}")
    sys.exit(1)
else:
    print("\n✅ SUBMISSION SUCCESSFUL")
    print("\nThe form would be sent to: info@openheartshomecare.net")
    print(f"\nSubject: New Contact Form Submission - {test_data['subject']}")
    print("\nEmail Content:")
    print("-" * 60)
    print(f"Name: {test_data['name']}")
    print(f"Email: {test_data['email']}")
    print(f"Phone: {test_data['phone']}")
    print(f"Subject: {test_data['subject']}")
    print(f"Message:\n{test_data['message']}")
    print("-" * 60)
    sys.exit(0)
