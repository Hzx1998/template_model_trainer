## 项目训练模板   



1. 实现了部分训练工具类和方法   
2. 设置了常用的工程目录   
3. 后续会持续更新工具类

当前方法和类：
1. send_success_email(title,text,From,To,password)   
其中From所用邮箱需要开启smtp功能，title为邮件主题，text为邮件内容，password为smtp功能密钥。
2. timer() 计时器类，提供start和end方法end方法返回最终运行时间
3. set_seed(seed) 设置随机数种子包括random np.random torch.manual_seed,多卡随机种子



..... 未完待续
