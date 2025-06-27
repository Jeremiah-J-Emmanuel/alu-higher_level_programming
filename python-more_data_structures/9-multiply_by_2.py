#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for key in  a_dictionary:
        a_dictionary[key] = a_dictionary[key] ** 2
    return(a_dictionary)


if __name__ == "__main__":
    multiply_by_2({'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16})
