#!/usr/bin/python3
def best_score(a_dictionary):
    sort_dict = sorted(a_dictionary.items())
    norm_dict = dict(sort_dict)
    count = 0
    if len(sort_dict) == 0:
        return None
    else:
        last_key = list(norm_dict.keys())[-1]
        return last_key


if __name__ == "__main__":
    print(best_score({'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}))
    