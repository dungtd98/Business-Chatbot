from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

def generate_key(text, salt, iterations):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
    )
    key = kdf.derive(text.encode('utf-8'))
    key = base64.urlsafe_b64encode(key)
    cipher_suite = Fernet(key)
    return cipher_suite
# encrypted_data = cipher_suite.encrypt(b"This message is being encrypted and cannot be seen!")
# print(cipher_suite.decrypt(encrypted_data).decode())