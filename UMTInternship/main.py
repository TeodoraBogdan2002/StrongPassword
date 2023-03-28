
def strong_password(s):
    # Initializez variabila count cu 0, variabila cu care voi contoriza cate inserari de litera mare(in cazul in care
    # nu este nicio litera mare), inserari de litera mica(in cazul in care
    #     # nu este nicio litera mica) sau inserari de cifre
    count = 0
    has_repeating = False

    # daca lungimea string.ului este mai mica decat 6, vom face cel putin 6-len(string) schimbari
    # daca lungimea string.ului este mai mare decat 20, vom face cel putin len(string)-20 schimbari
    if len(s) < 6:
        # in cazul in care este un triplet de caractere identice in string.ul de len<6 atunci pe langa cele 6-len
        # (string) schimbari, va mai trebuie inlocuit si unul dintre caracterele din triplet, dat fiind faptul ca daca
        # string.ul este de mai putin de 6 caractere, adica cel mult 5, atunci avem cel mult un triplet, deci necesita
        # maxim o scimbare + 6 -len(string) schimbari
        for c in range(len(s)):
            if c > 1 and s[c] == s[c - 1] and s[c - 1] == s[c - 2]:
                has_repeating = True
        if has_repeating:
            count += 1
        count += 6 - len(s)
    elif len(s) > 20:
    # in cazul in care este un triplet de caractere identice in string.ul de len<6 atunci pe langa cele len(string)-20
        #         schimbari, va mai trebuie inlocuit si unul dintre caracterele din fiecare triplet, deci count = count
        # + numar triplete, nu necesita verificare de existenta a literelor mici/mari sau a cifrelor, pentru ca odata
        # cu o schimbare din triplet se poate adauga in acel triplet o litera mare sau o litera mica sau o cifra
        triplete=0
        for c in range(len(s)):
            if c > 1 and s[c] == s[c - 1] and s[c - 1] == s[c - 2]:
                triplete+=1
        if has_repeating:
            count+=triplete
        count += len(s) - 20
    else:
        # daca string.ul are lungime intre 6 si 20 atunci vom verifica daca contine litere mari/mici sau cifre
        has_lowercase = False
        has_uppercase = False
        has_digit = False
        nrtriplets=0
        for c in range(len(s)):
            # has_lowercase ,has_uppercase ,has_digit devin true in cazul in care nu avem nicio cifra, nicio litera mare/ mica
            has_lowercase |= s[c].islower()
            has_uppercase |= s[c].isupper()
            has_digit |= s[c].isdigit()
            # daca are un triplet de caractere, vom creste numarul de triplete cu 1
            if c > 1 and s[c] == s[c-1] == s[c-2]:
                    nrtriplets+=1
        # in cazul in care cuvantul are cel putin o litera mare, o litera mica sau o cifra, dar daca sunt triplete de
        # caractere, atunci se va face cate o schimbare in fiecare triplet, in cazul in care avem triplete, dar avem
        # litera mare, litera mica, cifra atunci vom face scibari doar in triplete, iar daca dar avem
        # litera mare, litera mica, cifra dar nu avem triplete atunci count ramane 0
        if has_digit or has_uppercase or has_lowercase:
                count+=nrtriplets
        # daca nu are litere mare/ nu are litere mici sau nu are cifre, crestem numarul de schimbari
        elif not has_lowercase:
            count += 1
        elif not has_uppercase:
            count += 1
        elif not has_digit:
            count += 1
    return count


print(strong_password("Paroool9aaa")) #--->2
