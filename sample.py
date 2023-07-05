from Encryption import Encryption


class Sample:
    @staticmethod
    def encrypt(plaintext, shift):
        ciphertext = []

        for ch in plaintext:
            shifted_char = chr((ord(ch) + shift) % 65536)
            ciphertext.append(shifted_char)

        return ''.join(ciphertext)

    @staticmethod
    def decrypt(ciphertext, shift):
        plaintext = []

        for ch in ciphertext:
            shifted_char = chr((ord(ch) - shift + 65536) % 65536)
            plaintext.append(shifted_char)

        return ''.join(plaintext)

if __name__ == "__main__":
    messages = ["BALANCE / EMMAN / 11/11/1111 / 0123456789 / NEAR CITY / MODCLOUD / LIVING ROOM / 2 / 11000 / 1000 / 10000 / 0 / 2023-06-17 / 11289 / "]
    shift = 3
    ui = Encryption()
    for message in messages:
        encrypted_message = ui.encrypt(message)
        print(encrypted_message)
        decrypted_message = ui.decrypt("17303#&#1500#&#10#&#YFGQJ#&#GWFSI#Y#&#Bttijs#Yfgqj#&#INSNSL#WTTR#&#Mtti#Nsh.#&#2023-05-23#&#")
        print(decrypted_message)
