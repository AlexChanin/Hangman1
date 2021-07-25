def normalize(t_name):
    # put your code here
    t_dict = {"é": "e", "ë": "e", "á": "a", "å": "a", "œ": "oe", "æ": "ae"}
    trans = t_name.maketrans(t_dict)
    return t_name.translate(trans)


name = input()
print(normalize(name))
