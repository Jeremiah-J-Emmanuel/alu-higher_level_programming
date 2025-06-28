#!/usr/bin/python3
def roman_to_int(roman_string):
    thousands = {"0":"", "1":"M", "2":"MM", "3":"MMM"}
    
    hundreds = {"0":"", "1":"C", "2":"CC", "3":"CCC", "4":"CD", "5":"D",
                "6":"DC", "7":"DCC", "8":"DCCC", "9":"CM"}

    tens = {"0":"", "1":"X", "2":"XX", "3":"XXX", "4":"XL",
            "5":"L","6":"LX", "7":"LXX", "8":"LXXX", "9":"XC"}

    units = {"0":"", "1":"I", "2":"II", "3":"III", "4":"IV", "5":"V",
                "6":"VI", "7":"VII", "8":"VIII", "9":"IX"}
    
    if type(roman_string) != type("a string"):
        return None
    else:
        new_str = []
        roman_reversed = roman_string[::-1]
        count = 0
        for i in roman_reversed:
            if count == 0:
                dictionary = units
            elif count == 1:
                dictionary = tens
            elif count == 2:
                dictionary = hundreds
            else:
                dictionary = thousands

            new_str.append(dictionary.get(i))
            count = count + 1
        rev = []
        idx = -1
        try:
            for idx in range(-1, -6):
                rev.append(new_str[idx])
        except ValueError:
            pass
        separator = ""
        joined = separator.join(rev)
        return joined
    

if __name__ == "__main__":
    print(roman_to_int("76"))