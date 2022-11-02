def key(pswrd, letter): 
    if pswrd == '1' and letter == 'a':
        letter = 'm'
    if pswrd == '2' and letter == 'a':
        letter = 'v'
    if pswrd == '3' and letter == 'a':
        letter = 'e'
    if pswrd == '1' and letter == 'd':
        letter = 'y'
    if pswrd == '2' and letter == 'd':
        letter = 'l'
    if pswrd == '3' and letter == 'd':
        letter = 'a'
    if pswrd == '1' and letter == 'm':
        letter = 'b'
    if pswrd == '2' and letter == 'm':
        letter = 'q'
    if pswrd == '3' and letter == 'm':
        letter = 'd'
    
    return letter 
            
cleaned_data = ''          
e_data = "adm" 
password = input()


for x in password: 
    cleaned_data.concatnate(key(x, e_data)) 

print(cleaned_data)
    
