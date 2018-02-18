print('What is your name')
name = input()
if name.upper() == 'LUKE' or 'DAN':
  print('Hi {}'.format(name))
  print('What is your age')
  age = input()
  if age == 24:
      print('Hah you old as fuck')
  elif age == 23:
      print('Decent, decent')
  else: 
      print('YOU LIE')
else:
  print('Fuck off')
  
loop = True
while loop:
    print('Please enter password')
    password = input()
    if password.islower():
        print('Passwords must contain capital letters')
    elif password.isalpha():
        print('Passwords must contain at least one number')
    else:
        print('Please reenter password')
        reenter = input()
        if password == reenter:
            print('Thank you. Your password will now be sold on to Koreans')
            loop = False
