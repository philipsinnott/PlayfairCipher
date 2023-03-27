import PlayfairCipher as playfair

print("Plaintext: ")
plaintext = input()
print("Key: ")
key = input()
matrix = playfair.create_matrix(key)
for i in matrix:
    print(i)
print("------------------")
print("Unencrypted: " + plaintext)
print("Encrypted: " + playfair.encrypt_playfair(matrix, plaintext))

if __name__ == "__main__":
    pass