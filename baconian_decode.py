dict_list={
            'aaaaa':'a',
            'aaaab':'b',
            'aaaba':'c',
            'aaabb':'d',
            'aabaa':'e',
            'aabab':'f',
            'aabba':'g',
            'aabbb':'h',
            'abaaa':'i',
            'abaab':'j',
            'ababa':'k',
            'ababb':'l',
            'abbaa':'m',
            'abbab':'n',
            'abbba':'o',
            'abbbb':'p',
            'baaaa':'q',
            'baaab':'r',
            'baaba':'s',
            'baabb':'t',
            'babaa':'u',
            'babab':'v',
            'babba':'w',
            'babbb':'x',
            'bbaaa':'y',
            'bbaab':'z'
            }
cipher = "aaaaabaabbbaabbaaaaaaaabaababaaaaaaabbabaaabbaaabbaabaaaababaabaaabbabaaabaaabaababbaabbbabaaabababbaaabbabaaabaabaabaaaabbabbaabbaabaabaaabaabaabaababaabbabaaaabbabaabba"
plainer = ""
cipher_arr = []
[cipher_arr.append(cipher[i:i+5]) for i in range(0,len(cipher),5)]
for i in cipher_arr:
    plainer =plainer+dict_list[i]
print plainer
