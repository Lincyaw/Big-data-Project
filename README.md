# Big-data-Project

`wordcount`实验命令

在单机环境下跑

`hadoop jar ~/Documents/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.2.jar wordcount ~/Documents/Big-data-Project/input ~/Documents/Big-data-Project/output`

在伪分布式环境下跑:

`hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.2.jar wordcount input output`

伪分布式环境下： 相当于是一个虚拟的文件系统，zsh的那些提示都没了，狗屎

将要进行统计测试的文件`out.txt`放到`input`文件夹下

`bin/hdfs dfs -put out.txt input`

删除output文件夹

`bin/hdfs dfs rm -r output`