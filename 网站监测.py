import pandas as pd
import requests
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def red_Excel():
    file_path = r'资产白名单 .xlsx'
    raw_data = pd.read_excel(file_path, header=0)
    data = raw_data.values

    # 读取表中部分字段
    for i in data:
        name = i[0]
        url = i[2]
        t = str(i[7]).replace('\n', '')
        flage = i[3]

        if url.find('http') == 0:
            pass
        else:
            url = 'http://' + url

        # 发送请求验证网站状态
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Core/1.94.175.400 QQBrowser/11.1.5155.400'}
        try:
            resp = requests.get(url, timeout=5, headers=header)
            resp.encoding = 'utf-8'
            html = resp.text
            status_code = resp.status_code
            length = len(html)
            # print('网页响应码：' + str(status_code), end='\t')
            # print('网页内容长度：' + str(length), end='\t')
            list = [name, url, flage, t, status_code, length]
            message.append(list)
            if status_code == 200 and length > 0:
                pass
                # print(name + '\t' + url + '\t' + flage + '\t' + '网页访问正常 True', end='\t')

            else:
                pass
                # print(name + '\t' + url + '\t' + flage + '\t' + '网页访问失败 False', end='\t')
        except:
            # print(str(name) + '\t' + str(url) + '\t' + str(flage) + '\t' + '网页访问失败 False', end='\t')
            list = [name, url, flage, t, 0, 0]
            message.append(list)

    save()
    return message


def save():
    with open('2.txt', mode='w') as wstream:
        for i in message:
            for j in i:
                # print(j)
                wstream.write(str(j) + '\t')
            wstream.write('\n')


def mail(message):
    my_sender = '1213144536@qq.com'  # 发件人邮箱账号
    my_pass = 'odeydtxkeqhsgjbg'  # 发件人邮箱密码
    # my_user = 'demokaluo@gmail.com'  # 收件人邮箱账号，我这边发送给自己
    my_user = '1213144536@qq.com'  # 收件人邮箱账号，我这边发送给自己
    try:
        mail_msg = """
                   <p>Python 自动化检测脚本...</p>
                   <table border="1" cellspacing="0" cellpadding="10">

           			<tr>
           			    <td>ID</td>
           				<td>网站名称</td>
           				<td>地址</td>
           				<td>访问方式</td>
           				<td>开放时间</td>
           				<td>响应码</td>
           				<td>长度</td>
           			</tr>
                   """
        a=1
        for i in range(len(message)):
            mail_msg = mail_msg + '''
                       <tr>
                       <td>{}</td>
           				<td>{}</td>
           				<td><a href="{}">{}</a></td>
           				<td>{}</td>
           				<td>{}</td>
           				<td>{}</td>
           				<td>{}</td>
           			</tr>
           			'''
            mail_msg = mail_msg.format(a,message[i][0], message[i][1], message[i][1], message[i][2], message[i][3],
                                       message[i][4],
                                       message[i][5], )
            a+=1
        mail_msg = mail_msg + '</table>'
        # print(mail_msg)
        # msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
        msg = MIMEText(mail_msg, 'html', 'utf-8')
        msg['From'] = formataddr(["网络安全运维日志", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "系统运行白名单"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        print("邮件发送成功")

    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print("邮件发送失败")


if __name__ == '__main__':
    message = []
    a = red_Excel()
    mail(a)
