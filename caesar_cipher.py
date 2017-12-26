plaintext=input("Enter message")  # Enter any message you want to Encryypt

alphabet="abcdefghijklmnopqrstuvwxyz"
key=3           #Give any Key value in this case i gave 3
cipher=''

for c in plaintext:
    if c in alphabet:
        cipher += alphabet [(alphabet.index(c)+key)%len(alphabet)]

print("Your Encrypted message is : " + cipher)


