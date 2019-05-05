# 一 安装ansible
# 1.	yum install -y wget #下载wget
# 2.	wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/rpel-7.repo
# 3.	yum install -y ansible


# 二 获取db组/opt目录下文件
#  1 ansible db -m command -a "ls /opt"
#  2 ansible db -m command -a "chdir=/ ls"


# 三 .创建xiaoqiang2用户，并设置密码为xiaoqiang
# 1 ansible db -m shell -a "useradd xiaoqiang3"#创建新用户
#  2.ansible db -m shell -a "echo 'xiaoqiang' | passwd xiaoqiang3"#这条命令既可以修改用户密码也可以给新用户设置密码


# 四..在/tmp目录下生成xiaoqiang.txt文件，文件的内容为"大弦嘈嘈如急雨，小弦切切如私语，嘈嘈切切错杂弹，大珠小珠落玉盘"
#  1 ansible db -m shell -a "touch /tmp/xiaoqiang.txt"
#  2 ansible db -m copy -a " content='大弦嘈嘈如急雨，小弦切切如私语，嘈嘈切切错 杂弹，大珠小珠落玉盘' dest=/tmp/xiaoqiang.txt"


# 五 将本地的网卡配置文件复制到远程机器上，并命名为network，用户为xiaoqiang2，用户组为xiaoqiang2，权限为744
#  1. ansible db -m copy -a " src=/etc/sysconfig/network-scripts/ifcfg-ens33 dest=/tmp/network group=xiaoqiang3 owner=xiaoqiang3 mode=755 "


# 六 将/etc/rc3.d目录复制到远程机器上，指定用户名为alex，权限为755
#  1. ansible db -m copy -a "src=/etc/rc3.d owner=alex mode=755 dest=/tmp/rc3.d "


# 七 将/etc/rc6.d目录下的文件复制到远程机器上
#  1. ansible db -m copy -a "src=/etc/rc3.d/ owner=alex mode=755 dest=/tmp/rc3.d "


# 八 写一个脚本获取web组的系统内核版本号
# 1.	cd /tmp
# 2.	vi a.sh
# 3.	在文本中写入 #!/bin/bash cat /proc/version wq!保存退出
# 4.	在管控机上执行 ansible db -m script -a "/tmp/a.sh"
#
