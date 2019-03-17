
def commaCode(list):
    string = ''
    for i in range (len(list)):
        if i == (len(list)-1):
            string = string + 'and ' + list[i]
            print(string)
        else:    
            string = string + list[i] + ', '
        
            
       
                        
spam = ['apples', 'bananas', 'tofu', 'cats']        
commaCode(spam)    
