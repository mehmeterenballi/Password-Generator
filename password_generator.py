import math


def password_creator():

    sub_domain = input("The site address's sub domain or the site name or the account name "
                       "for password you want to create: ")
    password_number = int(input("What number are you creating password for this account?\n"))
    password = ""
    letter_array = [sub_domain[i:i+3] for i in range(0, len(sub_domain) + 1, 1)]
    english_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                       "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                       "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                       "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    dict_of_words = {i: english_alphabet[i] for i in range(0, len(english_alphabet))}

    loop_boolean = True
    condition_count = 0
    loop_count = 0

    print(dict_of_words)
    print(letter_array)

    # n**3 + n**2 + n
    while loop_boolean:
        if sub_domain.__len__() < 10:
            for n in range(0, 10):
                sub_domain = sub_domain + dict_of_words[(n**8) % 51]
                print(sub_domain)
            for i in dict_of_words:
                if sub_domain[condition_count] is None:
                    break
                if sub_domain[condition_count] in dict_of_words[i]:  # is i
                    password = password + dict_of_words.get(((password_number*(i**3) + password_number*(i**2) +
                                                              password_number*i) % 51))
                    condition_count += 1
                    print(password)
            # password = password + dict_of_words
        elif sub_domain.__len__() >= 10:
            for i in dict_of_words:
                if sub_domain[condition_count] is None:
                    break
                if sub_domain[condition_count] in dict_of_words[i]:  # is i
                    password = password + dict_of_words.get(((password_number * (i ** 3) + password_number * (i ** 2) +
                                                              password_number * i) % 51))
                    condition_count += 1
                    print(password)
            # password = password + dict_of_words


password_creator()
"""
    while loop_boolean:
        """
"""
        if len(password) == 10 and len(sub_domain) == 10:
            loop_boolean = False
        if len(password) == 10 and len(sub_domain) > 10:
            loop_boolean = True
        if len(sub_domain) > len(password) > 10:
            loop_boolean = True
        """
"""
        if len(password) == 10:
            loop_boolean = False
        else:
            loop_boolean = True
            password = password + (math.log(, password_number + 2))
"""
