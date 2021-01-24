import base64

print(" _____ _ _ _       _   ")
print("| ____| | (_) ___ | |_ ")
print("|  _| | | | |/ _ \| __|")
print("| |___| | | | (_) | |_ ")
print("|_____|_|_|_|\___/ \__|") 
print("_______________________")

ask = raw_input('Decode and Encode : ')
print('=================================')
E = 'encode'
D = 'decode'

#if ask == E:
#    print('Error. enter (encode)or(decode)')

#if ask != D:
#    print('Error. enter (encode)or(decode)')

def encode():
    print('here Encode')
    print('============')
    enex = raw_input('Enter Text To Encoding Base64: ')
    encoded = base64.b64encode(enex)
    print('_______________________')
    print encoded
    print('-----------------------')

def decode():
    print('here Decode')
    print('============')
    deex = raw_input('Enter Base64 code To Decoding : ')
    decoded = base64.b64decode(deex)
    print('_______________________')
    print decoded
    print('-----------------------')

if ask == E:
    encode()
elif ask != E D:
    #decode()
    print('test')

if ask == D:
    encode()
elif ask != D:
    #decode()
    print('test')