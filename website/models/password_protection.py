import bcrypt

def hash_password(password: str) -> bytes:
    # Generate a salt
    salt = bcrypt.gensalt()
    
    # Hash the password along with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    return hashed_password

def check_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password)
