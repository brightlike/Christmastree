# 常用命令集

## 基础sh

ps aux|grep xxx 查询进程
tail -f n30 /xx/xxx/*.log 查log
find / -name "*.py" -exec grep -nH "test*" {} \; 深度文件内容查询
pip3 install xxx 安装包依赖
apt-get install / yum install 安装包


## ssh

ssh-keygen -t rsa -C "xxx@yyyy.com" 生成rsa公钥
cat ～/.ssh/id_rsa.pub 查看公钥
vim ~/.ssh/authorized_keys 加添服务器授权

windows系统操作
首先Windows操作系统需要安装git.
安装完成后,再到任意的文件夹内,点击右键.选择git bash here
打开之后,输入ssh-keygen,一路按enter键.
全部结束后,再到C:\Users\Administrator\.ssh 文件夹下,打开id_rsa.pub文件,复制文件内的公钥.
注意:.ssh是隐藏文件,需开启文件显示.


## git


git pull 拉代码
git push 推代码
git add 添加修改文件待提交
git commit -m "xxx" 提交
git branch 查看分支
git checkout xxx 切换分支
git merge xxx 合并其他分支代码


git stash 临时暂屏蔽
git stash pop 临时屏蔽取消
git rebase 变基 去掉旁线


git tag -a V1.2 -m 'release 1.2' 打标签
git push origin --tags 提交标签
git fetch origin tag V1.2 获取远程标签



## 数据库

### mysql

### mongo

