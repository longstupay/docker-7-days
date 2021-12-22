#拉取PHP的开发环境
FROM php:7.4-cli 

#将当前目录的文件和文件夹复制到容器的myapp的目录之下
COPY . /usr/src/myapp   

#让容器的工作目录为myapp
WORKDIR /usr/src/myapp

#使用PHP CLI来执行工作目录下的index.php文件
CMD [ "php", "./index.php" ]