import secrets
import hmac
import hashlib
class HMACGenerator:
    def generate_key(self):
        return secrets.token_hex(32)

    def compute_hmac(self, key, move):
        return hmac.new(bytes.fromhex(key), move.encode(), hashlib.sha256).hexdigest()