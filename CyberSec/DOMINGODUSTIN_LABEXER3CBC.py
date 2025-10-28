import random

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def IV_Create():
    return ''.join(random.choice(alphabet) for _ in range(8))

def encrypt():
    while True:
        inp = input("Enter Plaintext (Max 24 characters): ").upper()
        
        if len(inp) > 24:
            print("Input too long! Maximum 24 characters.")
            continue

        while len(inp) % 8 != 0:
            print("Incorrect Input! Must be divisible by 8.")
            inp = input("Enter Plaintext (Max 24 characters): ").upper()
        
        key = input("Enter Key (Max 8 alphabetic characters): ").upper()
        while not set(key).issubset(set(alphabet)) or len(key) > 8 or len(key) < 8:
            print("Incorrect Key! Only 8 alphabetic characters allowed.")
            key = input("Enter Key: ").upper()

        iv = 'WKYRGMGN'
        print(f"IV: {iv}")

        blocks = [inp[i:i+8] for i in range(0, len(inp), 8)]
        ciphertext_blocks = []
        prev_block = 'WKYRGMGN'

        for block in blocks:
            enc_block = ""
            for j in range(8):
                mixed = alphabet[(alphabet.index(block[j]) + alphabet.index(prev_block[j])) % 26]
                enc_char = alphabet[(alphabet.index(mixed) + alphabet.index(key[j])) % 26]
                enc_block += enc_char
            ciphertext_blocks.append(enc_block)
            prev_block = enc_block

        print("Encrypted Blocks:", ciphertext_blocks)
        print("Final Ciphertext (IV + Ciphertext):", iv + ' | ' +  ''.join(ciphertext_blocks))
        break


def decrypt():
    while True:
        inp = input("Enter Ciphertext (Includes IV, divisible by 8): ").upper()

        if len(inp) < 16:
            print("Ciphertext too short! Must include 8-character IV + at least one block.")
            continue

        while len(inp) % 8 != 0:
            print("Incorrect Input! Must be divisible by 8.")
            inp = input("Enter Ciphertext (Includes IV): ").upper()

        key = input("Enter Key (8 characters): ").upper()
        while not set(key).issubset(set(alphabet)) or len(key) != 8:
            print("Incorrect Key! Only 8 alphabetic characters allowed.")
            key = input("Enter Key: ").upper()

        iv = inp[:8]
        blocks = [inp[i:i+8] for i in range(8, len(inp), 8)]

        plaintext_blocks = []
        prev_block = iv

        for block in blocks:
            dec_block = ""
            for j in range(8):
                temp = (alphabet.index(block[j]) - alphabet.index(key[j])) % 26
                orig_char = alphabet[(temp - alphabet.index(prev_block[j])) % 26]
                dec_block += orig_char
            plaintext_blocks.append(dec_block)
            prev_block = block

        print("Decrypted Text:", ''.join(plaintext_blocks))
        break

encrypt()
decrypt()
