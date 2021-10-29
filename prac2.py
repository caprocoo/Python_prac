import re

# . (ca.e) : 하나의 문자를 의미
# ^ (^de) : 문자열의 시작 
# $ (se$) : 문자열의 끝
p = re.compile("ca.e")

def print_match(m):
    if m:
        print(m.group())
    else : 
        print("매칭되지 않음")

m = p.match("dd")
print_match(m)


