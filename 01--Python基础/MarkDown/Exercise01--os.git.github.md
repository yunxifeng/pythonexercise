# 操作系统
- 管理软硬件资源,给运行软件提供一个统一调用平台
- 操作系统分类
  - Dos->(借鉴Apple)->Windows
  - Unix(很多高端软件都是基于Unix开发出来的)
    - Minix, Linux
    - MacOS
  - 注: - GUI:图形用户界面
        - ubuntu: Gnome
        - xubuntu: xface+ubuntu
        - kubuntu: kde+ubuntu
        - 优qilin: 国版ubuntu
        - xubuntu16(年份).04(月份,ubuntu一般每年4月和10月更新) LTS(长期支持版本,稳定)
# GIT
## 起源
   - 个人文件的版本控制，多方控制
   - 版本控制：CVS, SVN, BitKeeper（samba破解）， git（linus写的，分布式，开源）
   - 2008年：github上线， linux就在github上
   - 关于版本控制的产品：
       - 集中式：cvs，svn
	   - 分布式：github开源, bitbuckets私人(好用,免费,了解一下,创建一个)
	   - 分享精神:blog+github
   - 注：自由网，p2p
## linux下安装git:
   >sudo su (切换管理员)
   >密码:
   >apt-git install git(安装git)   
注:>aptitude search git(在软件仓库里搜索下git) aptitude show git(显示一下git)
   >pwd(显示当前路径)
   >mkdir:创建文件夹
   >cd :改变路径
   >ll:显示文件及文件夹, >ll -a:显示隐藏文件或文件夹, >ls:
   >touch *.*:创建文件 
   >vi *.*:编辑文件
   >cat *.*:查看文件
   - 在linux终端里可以直接使用
   
## 基本使用:
  - 创建仓库.git
      >git init(初始化一个仓库)
  - 向暂存区添加文件
      >git add (*.*)
  - 向仓库提交文件
      >git commit -m "备注信息" (*.*)
	  注:备注信息强制添加
  - 显示工作树(工作状态)
      >git status
  - 删除文件
      >git rm *.*(把删除这个动作提交到暂存区了)
	  >git commit -m "备注信息"(把删除动作提交到仓库,生成一个删除版本的版本号version)
  - 查看日志
      >git log
  - 版本回滚
      >git reset --hard 版本号
  - 提交到远程仓库
      >git remote add origin 仓库地址
      >git push (-u origin master) 
  - 克隆仓库
      >git clone 仓库地址
- 一些基本概念
  - 工作区:
  - 暂存区:
  - 仓  库:
  - version:版本号
  注: 工作区添加到暂存区(add),暂存区提交到仓库(commit),仓库克隆到工作区(clone)  
  
 