import paramiko

# 创建SSHClient 实例对象
ssh = paramiko.SSHClient()

# 信任远程机器，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接远程机器 地址 接口 用户名 密码
ssh.connect(
    '192.168.3.8',
    22,
    'wangzhixin',
    '123456'
)
ssh.exec_command('操作linux代码')
