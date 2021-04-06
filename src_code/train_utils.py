from __future__ import absolute_import 
import smtplib
import time
import torch
import random
import numpy as np
import pandas as pd
from email.mime.text import MIMEText
from email.header import Header

#发送定制邮件  
#seed email to tell you when the model has been trained
#错误记录：带默认值的参数不能在 默认值参数后面
def send_success_email(title,text,From="924024667@qq.com",To=["924024667@qq.com"],password="gjwxgnptasjcbeie"):
    mail = MIMEText(text,'plain','utf-8')
    mail['Subject']=title
    mail['From']='Aibool@ai.com'
    mail['To']='user@ai.com'
    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.qq.com',25)
        smtp.login(From,password)
        smtp.sendmail(From,To,mail.as_string())
        print("success")
    except smtplib.SMTPException:
        print("error")
    smtp.quit()
#设置随机数种子
def set_seed(seed,n_gpu):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if n_gpu>0:
        torch.cuda.manual_seed_all(seed)

#计时器类
#timer class
class timer(object):
    def __init__(self):
        self.run_time = 0
    def start(self):
        self.run_time=time.time()
        print("时间开始了")
    def end(self):
        self.run_time=time.time()-self.run_time
        if self.run_time<1:
            self.run_time = '{:.6f} s'.format(self.run_time)
        else:
            self.run_time = '{:d} h {:d} min {:.6f} s'.format(int(self.run_time//3600),int(self.run_time//60%60),self.run_time%3600)
        return self.run_time