### Conda使用指南

#### 1. 创建环境
```shell script
# 创建一个名为python38的环境，指定python版本是3.5
> conda create --name python38 python=3.8
```

#### 2. 激活已创建环境
```shell script
# 安装好环境后，使用activate激活某个环境
> conda activate python38   # for windows
> source activate python38 # for Linux & Mac

# 使用deactivate关闭某个环境
> conda deactivate python38   # for windows
> source deactivate python38 # for Linux & Mac
```

#### 3. 删除已创建环境
```shell script
> conda remove --name python38 --all
```

#### 4. 查看已创建环境
```shell script
> conda info -e
> conda env list
```

#### 5. 安装已创建环境的python库
```shell script
# 安装当前环境的python库
> conda install numpy

# 安装某个环境的python库
> conda install -n python38 numpy 
```

#### 6. 查看已创建环境的python库
```shell script
# 查看当前环境下已安装的python库
> conda list

# 查看指定环境下已安装的python库
> conda list -n python38

# 查看python库信息
> conda search numpy

# 更新python库
> conda update -n python38 numpy

# 删除python库
> conda remove -n python38 numpy
```

#### 7. 设置国内镜像
```shell script
# 添加Anaconda的TUNA镜像
> conda config --add channels  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ 

# # TUNA的help中镜像地址加有引号，需要去掉 # 设置搜索时显示通道地址 
> conda config --set show_channel_urls yes
```