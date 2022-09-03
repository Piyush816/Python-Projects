from cryptography.fernet import Fernet

try:

    method = int(input("""
Please select a method:-
1.Encrypt
2.Decrypt
\n"""))
    # encrypt message
    if (method == 1):
        message = input("Enter your message you want to encrypt\n")
        # generating the key
        key = Fernet.generate_key()
        f = Fernet(key)
        # encrypting message
        encMessage = f.encrypt(bytes(message,'utf-8'))
        # print output
        print("***PLEASE STORE THIS KEY IN A SAFE PLACE TO DECRYPT THE MESSAGE***")
        print("***WITHOUT THIS KEY YOU WON'T BE ABLE TO DECRYPT THE MESSAGE***\n")
        print("Encrytion key is:- ",key.decode())
        print("Before encrypted:- ",message)
        print("After encrypted:- ",encMessage.decode())

    elif (method == 2):
        key = input("Enter your key\n")
        f = Fernet(bytes(key,"utf-8"))
        encMessage = input("Enter encrypted messaget\n")
        # decrypting the message
        decMessage = f.decrypt(bytes(encMessage,'utf-8'))
        print("Encrytion key is:- ",key)
        print("Encrypted message:- ",encMessage)
        print("Decrypted message:- ",decMessage.decode())


    else:
        raise ValueError("invalid Input")

except ValueError as err:
    if ("invalid literal for int()" in str(err)):
        print("Invalid method")
    else:print(err)

