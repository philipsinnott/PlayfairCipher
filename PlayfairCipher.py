def create_bigrams(string):
    for i in range(2, len(string), 2):
        if (len(string) - 1 > i):
            if (string[i] == string[i+1]):
                string=string[:i+1] + "x" + string[i+1:]
    if odd(string):
        string = string[:] + "x"
    return string

def odd(plaintext):
    if len(plaintext) % 2 != 0:
        return True
    return False

# Create Matrix
def create_matrix(key):
    # Initially stores list of all lowercase letters in the alphabet
    alphabet = list(map(chr, range(97, 123)))
    
    # Removes letters which are already in the key
    for i in key:
        if (i in alphabet):
            alphabet.remove(i)
            
    # Remove duplicates in key
    k = []
    for i in key:
        if (i not in k):
            k.append(i)
    
    # Insert each letter in the key
    for i in reversed(k):
        alphabet.insert(0, i)
 
    # Since the alphabet has 26 letters, and we want a 5x5 = 25 element matrix, we will omit one letter, in this case "j".
    if (alphabet.index("j") - alphabet.index("i") == 1):
        alphabet.remove("j")
    
    # If "j" still present in filler alphabet, remove it and append "z" at end as it will be missing
    for i in range(len(k), len(alphabet)):
        if (alphabet[i] == "j"):
            alphabet.remove("j")
            alphabet.append("z")
    # Transform 1D list into a 2D list with each sublist containing 5 letters
    alphabet = transform_2d(alphabet)
    return alphabet
    # Display 5x5 matrix visually
    #for i in alphabet:
    #    print(i)

def transform_2d(one_dim_list):
    two_dim_list = []
    curr = 0
    stop = 30 # i.e. 25
    step = 5
    for i in range(5):
        # Save the next 5 elements and append to 2D list
        curr_list = one_dim_list[curr:curr+step]
        two_dim_list.append(curr_list)
        # Increase curr value with 5 each iteration
        curr = curr + step
    return two_dim_list

# Get coordinates of any element in the list
def get_coords(matrix, char):
    index = []
    
    for i, j in enumerate(matrix):
        #print(i, j)
        for k, l in enumerate(j):
            #print(k, l)
            if (l == char):
                index.append(i) # row
                index.append(k) # col
    return index

# 2D list --> 1D list
def transform_1d(block):
    res = []
    for i in block:
        res.extend(i)
    return res

def plaintext_contains_j(plaintext):
    if ("j" in plaintext):
        plain = ""
        for i in plaintext:
            if (i == "j"):
                plain += "i"
            else:
                plain += i
        return plain
    else:
        return plaintext

def encrypt_playfair(mat, plaintext):
    plaintext = plaintext_contains_j(plaintext)
    cipher = []
    for i in range(0, len(plaintext) - 1, 2):
        n1 = get_coords(mat, plaintext[i])
        n2 = get_coords(mat, plaintext[i+1])
        
        # Same column
        if (n1[1] == n2[1]):
            k1 = (n1[0] + 1) % 5 # take letter below (going back to the top if at the bottom using mod 5)
            m1 = n1[1] # stay in same column
            
            k2 = (n2[0] + 1) % 5
            m2 = n2[1]
            cipher.append(mat[k1][m1])
            cipher.append(mat[k2][m2])
        
        # Same row
        elif (n1[0] == n2[0]):
            m1 = (n1[1] + 1) % 5 # take letter to the right (going back to the leftmost element if at the rightmost pos using mod 5)
            k1 = n1[0] # stay in same row
            
            m2 = (n2[1] + 1) % 5
            k2 = n2[0]
            cipher.append(mat[k1][m1])
            cipher.append(mat[k2][m2])
        
        # Create rectangle
        else:
            k1 = n1[0]
            m1 = n1[1]
            
            k2 = n2[0]
            m2 = n2[1]
            
            cipher.append(mat[k1][m2])
            cipher.append(mat[k2][m1])
    cipher = "".join(cipher)
    return cipher