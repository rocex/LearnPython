import smtplib
from email.mime.text import MIMEText
from tkinter import *
import tkinter.messagebox as messagebox
import sys


class MailGUI:  # 定义邮件管理窗口类
    def __init__(self):
        self.root = Tk()
        self.root.title('邮件发放器')

        workArea = Frame(self.root, width=500, height=500)
        workArea.pack()

        # 初始化窗口
        labelframe = LabelFrame(workArea, padx=5, pady=10)  # text can empty
        labelframe.pack(fill='both')

        # 定义变量，保存客户输入结果
        self.v_subject = StringVar()
        self.v_receiver = StringVar()
        self.v_content = StringVar()

        self.v_smtpServer = StringVar()
        self.v_smtpUser = StringVar()
        self.v_smtpPassword = StringVar()

        # 接收人
        receiver_frame = Frame(labelframe, width=400, height=50)
        receiver_frame.pack(fill='y')
        Label(receiver_frame, width=20, pady=5, justify='left', text='接收人').pack(side='left')
        Entry(receiver_frame, width=50, textvariable=self.v_receiver).pack(side='left')

        # 主题
        subject_frame = Frame(labelframe, width=400, height=50)
        subject_frame.pack(fill='y')
        Label(subject_frame, width=20, pady=5, justify='left', text='主题  ').pack(side='left')
        Entry(subject_frame, width=50, textvariable=self.v_subject).pack(side='right')

        # 邮件内容
        content_frame = Frame(labelframe, width=400, height=50)
        content_frame.pack(fill='y')
        Label(content_frame, width=20, pady=5, justify='left', text='内容  ').pack(side='left')
        self.T_content = Text(content_frame, width=50, height=4)
        self.T_content.pack(side='right')

        # SMTP 服务器
        smtpServer = Frame(labelframe, width=400, height=50)
        smtpServer.pack(fill='y')
        Label(smtpServer, width=20, pady=5, justify='left', text='SMTP 服务器').pack(side='left')
        Entry(smtpServer, width=50, textvariable=self.v_smtpServer).pack(side='right')

        # SMTP 账号
        smtpUser = Frame(labelframe, width=400, height=50)
        smtpUser.pack(fill='y')
        Label(smtpUser, width=20, pady=5, justify='left', text='SMTP 账号').pack(side='left')
        Entry(smtpUser, width=50, textvariable=self.v_smtpUser).pack(side='right')

        # SMTP 密码
        smtpPassword = Frame(labelframe, width=400, height=50)
        smtpPassword.pack(fill='y')
        Label(smtpPassword, width=20, pady=5, justify='left', text='SMTP 密码').pack(side='left')
        Entry(smtpPassword, width=50, textvariable=self.v_smtpPassword).pack(side='right')

        # 发送按钮
        btn_frame = Frame(labelframe, width=400, height=50, bg='#CCCCCC')
        btn_frame.pack(fill='y')
        sand_btn = Button(btn_frame, text=' 发 送 ', padx=3, pady=2, state='active', command=self.runSendMail)
        sand_btn.pack()

        self.root.mainloop()

    def runSendMail(self):
        # messagebox.askquestion(title='发送邮件',message='发送?')
        receiver = self.v_receiver.get()
        sub = self.v_subject.get()
        to_list = receiver.split(',')
        content = str(self.T_content.get('0.0', END)).strip()

        self.initSMTP(str(self.v_smtpUser.get()), str(
            self.v_smtpServer.get()), str(self.v_smtpPassword.get()))
        self.sendMail(sub, to_list, content)
        messagebox.showinfo(title='系统提示', message='发送成功')

    def initSMTP(self, mail_user, mail_server_name, mail_password):
        self.mail_user = mail_user + mail_server_name
        self.mail_password = mail_password
        self.mail_server_name = mail_server_name
        self._smtp = smtplib.SMTP_SSL()
        self._smtp.connect(self.findMailServer())
        self._smtp.login(self.mail_user, self.mail_password)

    def sendMail(self, sub, to_list, mail_body):
        msg = MIMEText(mail_body, _subtype='plain', _charset='utf-8')
        msg["Accept-Language"] = "zh-CN"
        msg["Accept-Charset"] = "ISO-8859-1,utf-8"
        msg['Subject'] = sub
        msg['From'] = self.mail_user
        msg['To'] = ";".join(to_list)
        self._smtp.sendmail(self.mail_user, to_list, msg.as_string())
        self._smtp.quit()

    def findMailServer(self):
        server_name = str(self.mail_server_name).strip()
        server_dict = {'@sina.com': 'smtp.sina.com',
                       '@126.com': 'smtp.126.com',
                       '@163.com': 'smtp.163.com',
                       '@qq.com': 'smtp.qq.com'}
        return server_dict[server_name]

try:
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    MailGUI()
except Exception as ex:
    print(ex)
