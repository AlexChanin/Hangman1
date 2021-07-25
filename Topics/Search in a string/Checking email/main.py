def check_email(string):
    return " " not in string \
           and "@" in string \
           and string.find('@') > 0 \
           and string.rfind('.') - string.rfind('@') > 1
