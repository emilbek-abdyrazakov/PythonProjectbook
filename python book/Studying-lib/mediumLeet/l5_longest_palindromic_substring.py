def longestPalindrome(s):
    longest = ""
    # counterA = 0
    # counterB = 0
    # counterC = 0
    # for i in range(len(s)):
    #     counterA += 1
    #     for x in reversed(range(len(s)+1)):
    #         counterB += 1
    #         res = s[i: x]
    #         if res == res[::-1] and len(longest) < len(res):
    #             counterC += 1
    #             longest = res
    #         if len(s) - i <= len(longest):
    #             return longest + " counterA: " + str(counterA) + " counterB: " + str(counterB) + " counterC: " + str(
    #                 counterC)
    #         if x - i < len(longest):
    #             break

    # return longest + " counterA: " + str(counterA) + " counterB: " + str(counterB)  + " counterC: " + str(counterC)
    longest = ""
    counter1 = 0
    counter2 = 0
    counter3 = 0
    for i in range(len(s)):
        counter1+=1
        for x in reversed(range(len(s) + 1)):
            counter2+=1
            res = s[i: x]
            if res == res[::-1] and len(longest) < len(res):
                longest = res
            if len(longest) >= len(s)-i:
                return longest, counter1, counter2


# print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))
print(longestPalindrome("gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv"))
print(longestPalindrome("abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"))
print(longestPalindrome("nmngaowrbsssvihklwmuqshcddwlxrywrlwtennwfvrevgvhsvgeccfulmuvrcksdmgeqrblnlwoepefhcwhmgyvgcoyyygrmttyfycxwbqktpurlcfhzlakhmrddsydgygganpmaglaxyhfwjusukzcnakznygqplngnkhcowavxoiwrfycxwdkxqfcjqwyqutcpyedbnuogedwobsktgioqdczxhikjrbkmqspnxcpngfdwdaboscqbkwforihzqdcppxjksiujfvlpdjryewaxgmdgigvxdlstxwngtbdrrkfudjinzyxbdmkautclvvyguekuzwwetmsxittgtxbnvvrgasvnlogdiepltweaehubwelznidltzlbzdsrxmhjpkmylnwkdsxnpkplkdzywioluaqguowtbaoqzqgjfewphqcvlnwlojbxgomvxxkhwwykawegxubjiobizicuxzeafgautefsurgjlbhcfevqzsbhwxycrcaibdsgluczcuewzqupakbzmcvzsfodbmgtugnihyhqkvyeboqhqldifbxuaxqzxtyejoswikbzpsvzkxcndgeyvfnyrfbkhlalzpqjueibnodamgpnxlkvwvliouvejcpnakllfxepldfmdzszagkyhdgqqbkb"))
print(longestPalindrome("cstgvkbrxacmpxdxxktktvpdzcuxmnhvuxdgsmskgeeawzeikhtmhdvnccbrgifpzmiuytfmeyfoxsntrdtxeuxcqsndexbgfxnthqwveujqzemloooyddparbjcuiwpopjwvvmwblsamkhjhlnoxinkpsempexmipifsfwzxbetgvfnkngzxcpizwctpdlpngjpyovmjllxfiwktghkxvyelwjwdztujmunijfsfdvmhgqhlpouewgyznphlmccjmqaqncwbeqheohibafqfunfywmrvqvjygjwqoclijwkcfiuaiymeagdbwyejnvtosxylptbtyoahfzfmwzrkhzdamknleroffmsqcaryibamgdpcumlhrblypddzhaxfeztokgogzgvpfvlmetiwsamhdidmvxavleryfyakendwrbslcavlqkerrnvpuzhdgwzuyorxzbkzhxhpbvkflgxouvaavxrdzsjlgrmogzvlhhdidldsxqhrqlryaanffhxnutcycnczuedtrwcnfiqrtoafvdfnfhxhyjivzalozrbrajboecfyalisxxanduzraqdrbzsbkobaieqpzcawrunxucypqyjnmrlrlivrrwwhdpekeelsphhunzbhkkejvqfopjsuholutgmtnleqdrntbqgrobnuhqpdkbjtikijkdiwqvnxgajaaqgswrdamzv"))
# def longestPalindrome(s):
#     longest = ""
#     counterA = 0
#     counterB = 0
#     counterC = 0
#     for i in range(len(s)):
#         counterA += 1
#         for x in reversed(range(len(s) + 1)):
#             counterB += 1
#             res = s[i: x]
#             if res == res[::-1] and len(longest) < len(res):
#                 counterC += 1
#                 longest = res
#             # if len(s) - x <= len(longest)
#
#     return longest