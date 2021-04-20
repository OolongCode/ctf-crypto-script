def decrype(cipher,key):
    cipher_len = len(cipher)
    if cipher_len%key == 0:
        key = cipher_len / key
    else:
        key = cipher_len / key + 1
    result = {x:'' for x in range(key)}
    for i in range(cipher_len):
        a = i%key;
        result.update({a:result[a]+cipher[i]})
    plainer=""
    for i in range(key):
        plainer = plainer + result[i]
    print plainer

cipher="felhaagv{ewtehtehfilnakgw}"
for n in range(2,20):
    decrype(cipher,n)


