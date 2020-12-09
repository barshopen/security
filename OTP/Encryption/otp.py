class OTP:
    def __init__(self):
        with open("random_key", "r") as f:
            self.key = bytes.fromhex(f.read())

    def encrypt(self, message:str)->str:
        message = message.encode("ascii")

        return self.xor_with_key(message)

    def decrypt(self, cipher:str)->str:
        cipher = bytes.fromhex(cipher)
        xored =  self.xor_with_key(cipher)
        return bytes.fromhex(xored).decode("ascii")

    def xor_with_key(self, message_bytes:bytes):
        cipher = bytearray()
        for i,j in zip(self.key, message_bytes):
            cipher.append(i^j)

        return cipher.hex()

if __name__ == "__main__":
    h = OTP().encrypt("hello magshimim")
    print(h)
    print(OTP().decrypt(h))