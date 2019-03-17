#Reverse Cipher
#https://www.nostarch.com/crachkingcodes/(BSD Licensed)



def translate(message):
    translated = ''
    i = len(message) - 1
    while i>=0:
        translated = translated + message[i]
        i = i - 1
    print(translated)    

print('What would you like to encrypt?')
message = input()
translate(message)


