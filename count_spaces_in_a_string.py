def check_space(string):
    count = 0
    for i in string:
        if i == " ":
            count += 1
         
    return count
string =input()
print(check_space(string))
    