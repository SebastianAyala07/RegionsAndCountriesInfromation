import hashlib

class CustomEncrypting():

    @classmethod
    def sha1_hexdigest(cls, str_to_encrypt):
        result_encrypt = hashlib.sha1(
            str(str_to_encrypt).encode('utf-8')
        )
        return result_encrypt.hexdigest()
