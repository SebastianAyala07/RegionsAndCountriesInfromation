import hashlib

class CustomEncrypting():

    @classmethod
    def sha1_hexdigest(cls, str_to_encrypt):
        result_encrypt = hashlib.sha1(
            str(str_to_encrypt).encode('utf-8')
        )
        return result_encrypt.hexdigest()

    # @classmethod
    # def byte_list_to_binary_string(cls, bytes):
    #     result = ""
    #     for byte in bytes:
    #         byte_str = "{0:b} ".format(byte).rjust(8, '0')
    #         result += byte_str
    #     return result

