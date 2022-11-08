print("WELCOME!")

while True:

    print("1 - Latin Alphabet to Cyrillic Alphabet.\n" + "2 - Information of Alphabet Table\n" + "3 - Close the program.")
    mod = input("Choose selection: ")
    if mod == "1":
        metin = input(("Write here: "))

        if metin in "a" or "A":
            metin = metin.replace("a", "a")
            metin = metin.replace("A", "Б")

        if metin in "b" or "B":
            metin = metin.replace("b", "б")
            metin = metin.replace("B", "Б")

        if metin in "v" or "V":
            metin = metin.replace("v", "в")
            metin = metin.replace("V", "В")

        if metin in "w" or "W":
            metin = metin.replace("w", "в")
            metin = metin.replace("W", "В")

        if metin in "g" or "G":
            metin = metin.replace("g", "г")
            metin = metin.replace("G", "Г")

        if metin in "d" or "D":
            metin = metin.replace("d", "б")
            metin = metin.replace("D", "Б")

        if metin in "e" or "E":
            metin = metin.replace("e", "e")
            metin = metin.replace("E", "E")

        if metin in "jo" or "Jo" or "yo" or "Yo":
            metin = metin.replace("jo", "ё")
            metin = metin.replace("Jo", "Ё")
            metin = metin.replace("yo", "ё")
            metin = metin.replace("Yo", "Ё")

        if metin in "zh" or "Zh":
            metin = metin.replace("zh", "ж")
            metin = metin.replace("Zh", "Ж")

        if metin in "z" or "Z":
            metin = metin.replace("z", "з")
            metin = metin.replace("Z", "З")

        if metin in "i" or "I":
            metin = metin.replace("i", "и")
            metin = metin.replace("I", "И")

        if metin in "j" or "J":
            metin = metin.replace("j", "й")
            metin = metin.replace("J", "Й")

        if metin in "k" or "K":
            metin = metin.replace("k", "к")
            metin = metin.replace("K", "К")

        if metin in "l" or "L":
            metin = metin.replace("l", "л")
            metin = metin.replace("L", "Л")

        if metin in "m" or "M":
            metin = metin.replace("m", "м")
            metin = metin.replace("M", "М")

        if metin in "n" or "N":
            metin = metin.replace("n", "н")
            metin = metin.replace("N", "Н")

        if metin in "o" or "O":
            metin = metin.replace("o", "о")
            metin = metin.replace("O", "О")

        if metin in "p" or "P":
            metin = metin.replace("p", "п")
            metin = metin.replace("P", "П")

        if metin in "r" or "R":
            metin = metin.replace("r", "р")
            metin = metin.replace("R", "Р")

        if metin in "s" or "S":
            metin = metin.replace("s", "с")
            metin = metin.replace("S", "C")

        if metin in "t" or "T":
            metin = metin.replace("t", "т")
            metin = metin.replace("T", "Т")

        if metin in "u" or "U":
            metin = metin.replace("u", "у")
            metin = metin.replace("U", "У")

        if metin in "f" or "F":
            metin = metin.replace("f", "ф")
            metin = metin.replace("F", "Ф")

        if metin in "h" or "H" or "x" or "X":
            metin = metin.replace("h", "х")
            metin = metin.replace("x", "х")
            metin = metin.replace("H", "Х")
            metin = metin.replace("X", "Х")

        if metin in "c" or "C":
            metin = metin.replace("c", "ц")
            metin = metin.replace("C", "Ц")

        if metin in "ch" or "Ch":
            metin = metin.replace("ch", "ч")
            metin = metin.replace("Ch", "Ч")

        if metin in "sh" or "Sh":
            metin = metin.replace("sh", "ш")
            metin = metin.replace("Sh", "Ш")

        if metin in "shh" or "Shh" or "shch" or "Shch":
            metin = metin.replace("shh", "щ")
            metin = metin.replace("Shh", "Щ")
            metin = metin.replace("shch", "щ")
            metin = metin.replace("Shch", "Щ")

        if metin in "''" or "#" or "Q" or "q":
            metin = metin.replace("''", "ъ")
            metin = metin.replace("#", "ъ")
            metin = metin.replace("q", "ъ")
            metin = metin.replace("Q", "Ъ")

        if metin in "y" or "Y":
            metin = metin.replace("y", "ы")
            metin = metin.replace("Y", "Ы")

        if metin in "'":
            metin = metin.replace("'", "ь")

        if metin in "je" or "ä" or "Je" or "Ä":
            metin = metin.replace("je", "э")
            metin = metin.replace("Je", "Э")
            metin = metin.replace("ä", "э")
            metin = metin.replace("Ä", "Э")

        if metin in "ju" or "Ju" or "yu" or "Yu" or "ü" or "Ü":
            metin = metin.replace("ju", "ю")
            metin = metin.replace("Ju", "Ю")
            metin = metin.replace("yu", "ю")
            metin = metin.replace("Yu", "Ю")
            metin = metin.replace("ü", "ю")
            metin = metin.replace("Ü", "Ю")

        if metin in "ja" or "Ja" or "ya" or "Ya":
            metin = metin.replace("ja", "я")
            metin = metin.replace("Ja", "Я")
            metin = metin.replace("ya", "я")
            metin = metin.replace("Ya", "Я")

        print(metin)

    elif mod == "3":
        exit()

    elif mod == "2":
        print("----------------------\n" +
                "А -> A	Р -> R\n" +
                "Б -> B	C -> S\n" +
                "В -> V|W	Т -> T\n" +
                "Г -> G	У -> U\n" +
                "Д -> D	Ф -> F\n" +
                "Е ->E	Х -> H|X\n" +
                "Ё -> Jo|Yo|Ë	Ц -> C\n" +
                "Ж -> Zh    Ч -> Ch\n" +
                "З -> Z	Ш -> Sh\n" +
                "И -> I	Щ -> Shh|Shch\n" +
                "Й -> J	Ъ -> ''|#|Q\n" +
                "К -> K Ы -> Y\n" +
                "Л -> L Ь -> '\n" +
                "М -> M Э -> Je|Ä\n" +
                "Н -> N Ю -> Ju|Yu|Ü\n" +
                "О -> O Я -> Ja|Ya\n" +
                "П  -> P\n" + "----------------------\n")

    else:
        print("Wrong choose!")
