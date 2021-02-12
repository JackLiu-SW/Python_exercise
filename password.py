correct_password = '123456'
retry = 3
while retry > 0:
    password = input('Please enter your password:')
    if password == '123456':
        print('Success!!')
        break
    else:
        retry = retry - 1
        if retry == 0:
            print('Retry over 3 times, please try it later.')
        else:
            print('Incorrect password, please enter password again. Remaining retry times: ', retry)

