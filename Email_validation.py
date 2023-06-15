# It will check if your entered email is valid or not.

print('---Email Validation---')

email = input('Enter your Email :')
a, b, c = 0, 0, 0

if len(email) >= 6:

    if email[0].isalpha():

        if ('@' in email) and (email.count('@') == 1):

            if (email[-4] == '.') or (email[-3] == '.'):

                for item in email:

                    if item == item.isspace():
                        a = 1

                    elif item.isalpha():

                        if item == item.upper():
                            b = 1

                        elif item == item.lower():
                            continue

                    elif item.isdigit():
                        continue

                    elif item == '.' or item == '_' or item == '#' or item == '$' or item == '@':
                        continue

                    else:
                        c = 1

                if a == 1 or b == 1 or c == 1:
                    print('Your email is not valid...')

                else:
                    print('Your email is valid...')

            else:
                print('Your email is not valid...')

        else:
            print('Your email is not valid...')

    else:
        print('Your email is not valid...')

else:
    print('Your email is not valid...')

