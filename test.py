from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
text = 'my-secret-text'
salt = b'my-random-salt'
iterations = 100000
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=iterations,
)
key = kdf.derive(text.encode('utf-8'))
key = base64.urlsafe_b64encode(key)
cipher_suite = Fernet(key)
encrypted_data = cipher_suite.encrypt(("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").encode())
print(encrypted_data)