from email_validator import validate_email, EmailNotValidError
import jwt
import secrets
import time

def is_valid_email(email):
    try:
        validity_check = validate_email(email=email)
        email = validity_check["email"]  
        return True
    except EmailNotValidError as e:
        return False
    
def generate_api_key():
    return secrets.token_hex(32)

def generate_access_token(api_key, tenant_id):
    payload = {
        'user_id': str(tenant_id),
        'expires': time.time() + 86400
    }
    token = jwt.encode(payload=payload, key=api_key, algorithm='HS256')
    return token