FROM dadoha/centos7.4.1708
SHELL ["/bin/bash", "--login", "-c"]
RUN curl --output /etc/yum.repos.d/CentOS-Base.repo http://mirrors.163.com/.help/CentOS7-Base-163.repo
ENV TZ "Asia/Shanghai"
ENV WORK_PATH /usr/local/
COPY conf/ /conf
ENV MONGODB_NAME mongodb-linux-x86_64-rhel70-4.4.15
ENV MONGODB_SRC https://fastdl.mongodb.org/linux/$MONGODB_NAME.tgz
ENV REDIS_URL https://packages.redis.io/redis-stack/redis-stack-server-7.0.6-RC2.rhel7.x86_64.tar.gz
ENV NGINX_URL http://nginx.org/download/nginx-1.21.6.tar.gz

ENV PATH=$WORK_PATH/mongodb/$MONGODB_NAME/bin:$PATH
# mongodb
RUN curl --output $WORK_PATH/$MONGODB_NAME.tgz $MONGODB_SRC \
    && mkdir -p $WORK_PATH/mongodb \ 
    && tar zxvf $WORK_PATH/$MONGODB_NAME.tgz -C $WORK_PATH/ \ 
    && rm $WORK_PATH/$MONGODB_NAME.tgz \ 
    && mv $WORK_PATH/$MONGODB_NAME/ $WORK_PATH/mongodb \ 
    && mkdir -p /data/db \ 
    && mkdir -p /data/log \
    && mongod --config /conf/mongod.conf --fork

# redis
ENV PATH=$WORK_PATH/redis/bin:$PATH
RUN curl --output $WORK_PATH/redis.tar.gz $REDIS_URL \
    && tar zxvf $WORK_PATH/redis.tar.gz -C $WORK_PATH/ \
    && rm $WORK_PATH/redis.tar.gz \
    && mv $WORK_PATH/redis-stack-server-7.0.6-RC2 $WORK_PATH/redis \
    && redis-server /conf/redis.conf

RUN yum -y install which lsof wget gcc gcc-c++ mesa-libGL automake autoconf libtool make git zlib-devel pcre-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel

# conda
ENV PATH /opt/conda/bin:$PATH
RUN curl -O https://mirrors.bfsu.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh \ 
    && bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda \
    && rm Miniconda3-latest-Linux-x86_64.sh \
    && ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh \
    && source /root/.bashrc \
    && conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ \
    && conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/ \
    && conda config --set show_channel_urls yes \
    && conda create -n py390 python=3.9 -y \
    && cp /conf/pip.conf /etc/pip.conf

# node
RUN curl -sL https://rpm.nodesource.com/setup_16.x | bash - && \
    yum install -y nodejs

# pnpm
ENV PNPM_HOME="/root/.local/share/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN npm config set registry https://registry.npmmirror.com \
    && npm install pnpm -g \
    && pnpm config set registry https://registry.npmmirror.com \
    && pnpm add http-server

# nginx
ENV PATH=/opt/nginx/sbin:$PATH
RUN curl --output $WORK_PATH/nginx.tar.gz $NGINX_URL \
    && tar zxvf $WORK_PATH/nginx.tar.gz -C $WORK_PATH/ \
    && rm $WORK_PATH/nginx.tar.gz \
    && cd $WORK_PATH/nginx-1.21.6 \
    && ./configure --prefix=/opt/nginx \
    && make -j16 \
    && make install \
    && cp /conf/nginx.conf /opt/nginx/conf/ -f

COPY . /project/

# client
RUN cd /project/client \
    && pnpm install \
    && pnpm build \
    && nginx 
EXPOSE 8080

# server
RUN cd /project/server \
    && bash \
    && source ~/.bashrc \
    && conda activate py390 \
    && pip install -r requirements.txt \
    && pip install -r /project/sdk/yolov5/requirements.txt
EXPOSE 5001
WORKDIR /project/server


CMD ["bash", "/project/server/run.sh"]
