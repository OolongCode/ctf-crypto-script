dict_list = {
             '01':'a',
             '1000':'b',
             '1010':'c',
             '100':'d',
             '0':'e',
             '0010':'f',
             '110':'g',
             '0000':'h',
             '00':'i',
             '0111':'j',
             '101':'k',
             '0100':'l',
             '11':'m',
             '10':'n',
             '111':'o',
             '0110':'p',
             '1101':'q',
             '010':'r',
             '000':'s',
             '1':'t',
             '001':'u',
             '0001':'v',
             '011':'w',
             '1001':'x',
             '1011':'y',
             '1100':'z'
             }

cipher="11 111 010 000 0 1010 111 100 0 00 000 000 111 00 10 1 0 010 0 000 1 00 10 110"
plainer=""

cipher_arr = cipher.split(" ")
for i in cipher_arr:
    plainer += dict_list[i]

print(plainer)

