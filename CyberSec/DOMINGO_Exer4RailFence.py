while True:
    try:
        key = int(input("Enter key (number of rails) between 2 and 10: "))
        if 2 <= key <= 10:
            break
        else:
            print("Key must be between 2 and 10. Try again.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

while True:
    pt = input("Enter plaintext (max length 20 characters): ")
    pt = ''.join(pt.split()) 
    if len(pt) <= 20 and pt.isalpha():
        break
    else:
        print("Plaintext must be max 20 alphabetic characters (spaces ignored). Try again.")

# Encryption
rails = ['' for _ in range(key)]
row = 0
direction = 1

for char in pt:
    rails[row] += char
    if row == 0:
        direction = 1
    elif row == key - 1:
        direction = -1
    row += direction

ciphertext = ''.join(rails)
print("Ciphertext:", ciphertext)


# Decryption
rail_matrix = [['\n' for _ in range(len(ciphertext))] for _ in range(key)]

row = 0
direction = 1
for col in range(len(ciphertext)):
    rail_matrix[row][col] = '*'
    if row == 0:
        direction = 1
    elif row == key - 1:
        direction = -1
    row += direction

index = 0
for i in range(key):
    for j in range(len(ciphertext)):
        if rail_matrix[i][j] == '*' and index < len(ciphertext):
            rail_matrix[i][j] = ciphertext[index]
            index += 1

result = []
row = 0
direction = 1
for col in range(len(ciphertext)):
    result.append(rail_matrix[row][col])
    if row == 0:
        direction = 1
    elif row == key - 1:
        direction = -1
    row += direction

decrypted_text = ''.join(result)
print("Decrypted text:", decrypted_text)
