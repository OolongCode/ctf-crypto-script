cipher = "/119/101/108/99/111/109/101/116/111/97/116/116/97/99/107/97/110/100/100/101/102/101/110/99/101/119/111/114/108/100"
plainer = ""
cipher_arr = cipher[1:].split('/')
for i in cipher_arr:
    plainer += chr(int(i))

print plainer
