dict_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

cipher="8842101220480224404014224202480122"
cipher_array = cipher.split("0")
cipher_arr = []
flag = ""

for i in cipher_array:
    k = 0
    for j in range(len(i)):
        k += int(i[j])
    cipher_arr.append(k)
for m in cipher_arr:
    flag += dict_list[m-1]

print flag
