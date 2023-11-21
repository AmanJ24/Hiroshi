def first_non_repeating_letter(string):
    answer = [i for i in string if string.lower().count(i) == 1]
    return '' if answer == [] else answer


first_non_repeating_letter("sTreSS")    