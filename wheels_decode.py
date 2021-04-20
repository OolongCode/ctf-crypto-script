dict_list = {
            '1':'ZWAXJGDLUBVIQHKYPNTCRMOSFE',
            '2':'KPBELNACZDTRXMJQOYHGVSFUWI',
            '3':'BDMAIZVRNSJUWFHTEQGYXPLOCK',
            '4':'RPLNDVHGFCUKTEBSXQYIZMJWAO',
            '5':'IHFRLABEUOTSGJVDKCPMNZQWXY',
            '6':'AMKGHIWPNYCJBFZDRUSLOQXVET',
            '7':'GWTHSPYBXIZULVKMRAFDCEONJQ',
            '8':'NOZUTWDCVRJLXKISEFAPMYGHBQ',
            '9':'XPLTDSRFHENYVUBMCQWAOIKZGJ',
            '10':'UDNAJFBOWTGVRSCZQKELMXYIHP',
            '11':'MNBVCXZQWERTPOIUYALSKDJFHG',
            '12':'LVNCMXZPQOWEIURYTASBKJDFHG', 
            '13':'JZQAWSXCDERFVBGTYHNUMKILOP'
            }

key=[2,3,7,5,13,12,9,1,8,10,4,11,6]
cipher="NFQKSEVOQOFNP"
cipher_arr=[]
plainer_arr=[]
plainer_list=[]
index = 0

for i in key:
    cipher_arr.append(dict_list[str(i)])

for j in cipher_arr:
    location = j.index(cipher[index])
    str_get = j[location:] + j[:location]
    plainer_arr.append(str_get)
    index += 1

for i in range(len(plainer_arr[0])):
    str_get=""
    for j in plainer_arr:
        str_get += j[i]
    print str_get.lower()


