
def repeatedString(s, n):
    """
    >>> repeatedString("aba",11)
    7
    >>> repeatedString("aba",str(11))
    Traceback (most recent call last):
      ...
    TypeError: unsupported operand type(s) for //: 'str' and 'int'
    """
    string = s
    letters = n
    a_count = string.count("a")
    string_count = a_count*(letters//len(string))
    residual_count = letters % len(string)
    string_residual_count = 0
    for i in range(residual_count):
        if string[i] == "a":
            string_residual_count += 1
    return string_residual_count + string_count

#Wrong peace of code
    """if letters >= 10**6 and second_count != 0:
        print("enters firs if")
        return first_count + 1
    elif second_count == 0:
        print("enters second if")
        return first_count
    else:
        print("enters third if")
        remain_string = string[:second_count]
        return first_count + remain_string.count("a")
"""

if __name__ == "__main__":
    import doctest
    s = {"aba":11,
         "ojowrdcpavatfacuunxycyrmpbkvaxyrsgquwehhurnicgicmrpmgegftjszgvsgqavcrvdtsxlkxjpqtlnkjuyraknwxmnthfpt":685118368975,
         "epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq":549382313570,
         "aedbdaeaddadddcedcbbabdccbecaecaccdbebeeadadcaabbaabbaeeeecaddbcdecbbdccdebaaebecdaaabbcdeccbabaabce":731869010806,
         "cfimaakj":554045874191,
         "a":1000000000000,
         "udjlitpopjhipmwgvggazhuzvcmzhulowmveqyktlakdufzcefrxufssqdslyfuiahtzjjdeaxqeiarcjpponoclynbtraaawrps":872514961806,
         "aab":882787,
         "bcbccacaacbbacabcabccacbccbababbbbabcccbbcbcaccababccbcbcaabbbaabbcaabbbbbbabcbcbbcaccbccaabacbbacbc":649606239860,
         "babbaabbabaababaaabbbbbbbababbbabbbababaabbbbaaaaabbaababaaabaabbabababaabaabbbababaabbabbbababbaabb":860622337747,
         "ebcdddafdfeffaddbceddebafbbebebbbcefcbcdfbaabecfaaeeaaffdfccffbdeeaabcfeecfcecbfebacefebdfaeedadebdf":561984209086
         }
    #print(repeatedString("aba",str(11)))
    doctest.testmod()




