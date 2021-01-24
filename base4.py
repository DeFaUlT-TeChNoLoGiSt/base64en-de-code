import base64

def main():

    ask = raw_input('Decode and Encode : ')
    print('=================================')
    E = ['encode', 'Encode', 'ENCODE']
    D = ['decode', 'Decode', 'DECODE']

    def encode():
        print('here Encode')
        print('============')
        enex = raw_input('Enter Text To Encoding Base64: ')
        encoded = base64.b64encode(enex)
        print('_______________________')
        print(encoded)
        print('-----------------------')

    def decode():
        print('here Decode')
        print('============')
        deex = raw_input('Enter Base64 code To Decoding : ')
        decoded = base64.b64decode(deex)
        print('_______________________')
        print(decoded)
        print('-----------------------')

    if ask in E:
        encode()
    if ask in D:
        decode()
        

c1 = ['continue', 'Continue', 'c', 'edame']

e0 = ['Exit', 'exit', 'ex', 'khroj']

while True:
    ask2 = raw_input('Continue or Exit ? ')
    if ask2 in c1:
        main()   
    if ask2 in e0:
        exit()

