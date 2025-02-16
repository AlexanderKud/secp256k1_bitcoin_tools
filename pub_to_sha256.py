import hashlib

def sha256(data):
    digest = hashlib.new("sha256")
    digest.update(bytes.fromhex(data))
    return digest.digest().hex()
    
pub = "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798"
print(sha256(pub))

