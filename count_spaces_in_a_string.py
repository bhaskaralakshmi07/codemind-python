def count_special_character(string): 
    special_char= 0
   
    for i in range(0, len(string)):  
      
        ch = string[i]

        if (string[i].isalpha()):  
            continue
        elif (string[i].isdigit()):
            continue
            
        else: 
            special_char += 1
            
            
    if special_char >= 1:    
        print("{}".format(special_char))  
    else:
        print("There are no Special Characters in this String.")
  
# Driver Code
if __name__ == '__main__' : 
    string = input()
    count_special_character(string)