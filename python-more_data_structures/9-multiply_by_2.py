#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for key in  new_dictionary:
        new_dictionary[key] = new_dictionary[key] ** 2
    return(new_dictionary)


if __name__ == "__main__":
    multiply_by_2({'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16})
