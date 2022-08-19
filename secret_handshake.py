'''
00001 = wink
00010 = double blink
00100 = close your eyes
01000 = jump
10000 = Reverse the order of the
operations in the secret handshake.
'''

def commands(binary_str):
    code_list = ['wink','double blink','close your eyes','jump']
    handshake = []
    i = -1
    while i > -abs(len(binary_str)):
        if binary_str[i] == '1':
            handshake.append(code_list[abs(i+1)])
        i -= 1
    if binary_str[0] == '1':
        handshake.reverse()
    return handshake

print(commands('11111'))