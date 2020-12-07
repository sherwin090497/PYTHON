import hashlib

def Encryption(input):
    buttonInput = hashlib.sha512(input.encode())
    encryptedInput = buttonInput.hexdigest()
    key = Compare(encryptedInput)
    return key

def Compare(compareInput):
    key = 'ff078a828af9cacd6a7c28489222d18c0daf9cf673eea6ef91a060de9a889034b17aa6164fd7f388e99d2af7384f9e7bd044ecf7b39f65d151ecdcfdcfb86e0b'
    if key == compareInput:
        return 0
    else:
        return 1

### TESTING ###
buttonInput = input()
result = Encryption(buttonInput)
if result == 0:
    print("password matched")
if result == 1:
    print("no match")