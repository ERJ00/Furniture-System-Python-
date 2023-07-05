class Encryption:
    SHIFT = 5

    @staticmethod
    def encrypt(plaintext):
        ciphertext = []

        for ch in plaintext:
            if ch.isupper():
                encrypted_char = chr((ord(ch) - ord('A') + Encryption.SHIFT) % 26 + ord('A'))
                ciphertext.append(encrypted_char)
            elif ch.islower():
                encrypted_char = chr((ord(ch) - ord('a') + Encryption.SHIFT) % 26 + ord('a'))
                ciphertext.append(encrypted_char)
            elif ch == ' ':
                ciphertext.append('#')
            elif ch == '/':
                ciphertext.append('&')
            else:
                ciphertext.append(ch)

        return ''.join(ciphertext)

    @staticmethod
    def decrypt(ciphertext):
        plaintext = []

        for ch in ciphertext:
            if ch.isupper():
                decrypted_char = chr((ord(ch) - ord('A') - Encryption.SHIFT + 26) % 26 + ord('A'))
                plaintext.append(decrypted_char)
            elif ch.islower():
                decrypted_char = chr((ord(ch) - ord('a') - Encryption.SHIFT + 26) % 26 + ord('a'))
                plaintext.append(decrypted_char)
            elif ch == '#':
                plaintext.append(' ')
            elif ch == '&':
                plaintext.append('/')
            else:
                plaintext.append(ch)

        return ''.join(plaintext)
