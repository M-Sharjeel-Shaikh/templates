import dns.resolver

# List of known disposable email domains (for simplicity, here are a few examples)
DISPOSABLE_EMAIL_DOMAINS = [
    "mailinator.com", "guerrillamail.com", "10minutemail.com", "tempmail.com"
]
# Function to check if an email is disposable
def is_disposable_email(domain: str) -> bool:
    return domain.lower() in DISPOSABLE_EMAIL_DOMAINS

# Function to check if domain has valid MX records
def validate_mx_record(domain: str) -> bool:
    try:
        # Query the MX records of the domain
        mx_records = dns.resolver.resolve(domain, 'MX')
        return bool(mx_records)
    except dns.resolver.NoAnswer:
        return False
    except dns.resolver.NXDOMAIN:
        return False
    except Exception:
        return False