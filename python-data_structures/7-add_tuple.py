#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    fix = (0, 0)
    fix2 = (0,) 
    if len(tuple_a) == 0:
        tuple_a += fix
    if len(tuple_b) == 0:
        tuple_b += fix
    if  len(tuple_a) == 1:
        tuple_a += fix2
    elif len(tuple_b) == 1:
        tuple_b += fix2
    else:
        pass

    first_a = tuple_a[0]
    sec_a = tuple_a[1]

    first_b = tuple_b[0]
    sec_b = tuple_b[1]

    new_1 = first_a + first_b
    new_2 = sec_a + sec_b

    added = (new_1, new_2)
    return (added)


if __name__ == "__main__":
    add_tuple(tuple_a=(), tuple_b=())
