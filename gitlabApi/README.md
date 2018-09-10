本仓库主要为了封装gitlabApi以实现自动化操作
v0.0.1
初始封装参数：

'-sg', '-sp', '-su', '-sgi', '-spi', '-sui', '-sgm', '-sgp', '-spm', "cg", "cp", "cu", "tp","cgm", "cpm", "egm", "epm", "rgm", "rpm", "dg", "dp", "du", "bu", "ubu"

二次封装参数(界面输待完善)：

'sg', 'sp', 'su'

使用示例:

执行：

查询用户

	python outPutOfGitlab.py -normal -su

查询组基本信息

	python outPutOfGitlab.py -normal -sg

查询组详细信息

	python outPutOfGitlab.py -normal -sg -a

查询项目基本信息

	python outPutOfGitlab.py -normal -sp

查询项目详细信息

	python outPutOfGitlab.py -normal -sp -a

查询项目组详细信息

	python outPutOfGitlab.py -admin -sgp test -m



创建定制组：

        修改CreateCustomMadeGroup.json文件，然后执行

	python CreateCustomMadeGroup.py -admin

计划：

一次封装增加Get key


二次封装继续调整输出
