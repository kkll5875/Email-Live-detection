from socket import socket, AF_INET, SOCK_STREAM
import time
import ReadTarget
import fire
def checkEmail(smtp_host,smtp_port):
    bufsize = 1024
    smtphost = smtp_host
    smtpport = smtp_port
    
    emails_list = []
    emails_list = ReadTarget.readTarget()
    live_email = []
    socket_con = socket(AF_INET,SOCK_STREAM)
    try:
        socket_con.connect((smtphost,smtpport))
        print("Socket 连接成功")
    except:
        print("Socket 连接失败")
    socket_con_recv = socket_con.recv(bufsize).decode('utf-8')
    print("=="+socket_con_recv)
    if socket_con_recv[:3] != '220':
        print('250 replay not received from server250 replay not received from server')
    socket_con.send('EHLO hello\r\n'.encode('utf-8'))
    ehlo_reback = socket_con.recv(bufsize).decode('utf_8')
    print("发送 EHLO"+ehlo_reback)
    
    socket_con.send('MAIL FROM:<aaa@aaa.com>\r\n'.encode('utf-8'))
    from_reback = socket_con.recv(bufsize).decode('utf-8')
    print('发送From信息:'+from_reback)

    print(type(emails_list))
    for x in range(len(emails_list)):
        target_email = emails_list[x]
        send_data = "RCPT TO:<"+target_email+">\r\n"
        socket_con.send(send_data.encode('utf-8'))
        
        check_email_reback = socket_con.recv(bufsize).decode('utf-8')
        if check_email_reback[:3] =='250':
            print('此邮箱存活：'+emails_list[x])
            print(check_email_reback)
            # live_email = emails_list[x]
            # email_list.append(line)
            live_email.append(emails_list[x])
        elif 'recipient is not exist' in check_email_reback:
            print('此邮箱不存在：'+emails_list[x])
        else:
            print('其他错误，请查看错误信息：'+check_email_reback)
    print("发现如下存活的邮件账号：")
    for n in range(len(live_email)):
        print(live_email[n])
    #  生成存活的文件
    # live_email[1].find('@')
    if len(live_email) > 0:
        email_name = live_email[0][live_email[0].find('@')+1:]
        file_name = email_name+'_'+str(int(time.time()))+'.txt'
        new_file = open(file_name,'w')
        for m in range(len(live_email)):
            new_file.writelines(live_email[m]+'\n')
        new_file.close()
        print("保存存活的邮箱文件："+file_name)
    # now = int(time.time())
    # file_name = smtp_host+str(now)

if __name__ == '__main__':
    use_tools = '''
    -------------------------------------------------------------------------
    | 参数1：目标smtp邮件服务器地址，可通过命令[nslookup -type=mx domain] 查看
    | 参数2：目标smtp邮件服务器端口，通常为25                                 
    | 命令格式: python main.py smtp_server 25                               
    -------------------------------------------------------------------------
    '''

    print(use_tools)
    fire.Fire(checkEmail)

