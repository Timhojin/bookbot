def get_num_words(content):
    to_list = content.split()
    return len(to_list)

def count_characters(content):
    unique_chars = {}
    for c in content:
        char = c.lower()
        if char not in unique_chars:
            unique_chars[char] = 1
        else:
            unique_chars[char] += 1

    return unique_chars

def sort_on(dict):
    return dict["num"]

def rsort_by_num(dict):
    listed = []
    for key in dict:
        new_dic = {
            "name": key,
            "num": dict[key]
        }
        listed.append(new_dic)

    listed.sort(reverse=True, key=sort_on)
    return listed