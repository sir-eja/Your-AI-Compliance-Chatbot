import re

PII_PATTERNS = {
    "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "phone": r"\+?\d{10,15}",
}

def redact_sensitive_info(text):
    for pattern in PII_PATTERNS.values():
        text = re.sub(pattern, "[REDACTED]", text)
    return text

# Example Usage
print(redact_sensitive_info("Contact me at john.doe@gmail.com or +1234567890"))
