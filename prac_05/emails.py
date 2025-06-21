"""
Emails
Estimate: 20 minutes
Actual:    minutes
"""

#Extract and format a guessed name from the email.
def extract_name(email):
    parts = email.split('@')[0].split('.')
    name = ' '.join(part.title() for part in parts)
    return name