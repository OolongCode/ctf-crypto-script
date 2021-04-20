dict_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cipher = "oknqdbqmoq{kag_tmhq_xqmdzqp_omqemd_qzodkbfuaz}"
for j in range(26):
    plainer = ""
    for i in cipher:
        if i in dict_list:
            plainer += dict_list[(dict_list.index(i)-j)%26]

        else:
            plainer += i
    print(plainer)
