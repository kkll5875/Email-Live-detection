import email


def readTarget():
    email_list = []
    for line in open('target.txt'):
        # print(line,end='')
        line = line.replace('\n','')
        email_list.append(line)
    return email_list
    # print(email_list)
   