import base64

def decode1(ans):
    return base64.b32decode(ans)

def decode2(ans):
    s=''
    for i in ans:
        x = ord(i) ^ 36
        x = x -36
        s += chr(x)

    return s

def decode3(ans):
    s=''
    for i in ans:
        x = ord(i)-25
        x = x ^ 36
        s += chr(x)

    return s

cipher = "UC7KOWVXWVNKNIC2XCXKHKK2W5NLBKNOUOSK3LNNVWW3E==="
plainer = decode3(decode2(decode1(cipher)))

print plainer

