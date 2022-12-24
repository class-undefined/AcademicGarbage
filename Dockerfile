FROM centos:7

# Install MongoDB
RUN yum update -y && \
    yum install -y wget && \
    wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add - && \
    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.2.list && \
    yum install -y mongodb-org=4.2.23 mongodb-org-server=4.2.23 mongodb-org-shell=4.2.23 mongodb-org-mongos=4.2.23 mongodb-org-tools=4.2.23 && \
    yum clean all

# Install Redis
RUN yum update -y && \
    yum install -y wget && \
    wget http://download.redis.io/releases/redis-7.0.4.tar.gz && \
    tar xzf redis-7.0.4.tar.gz && \
    cd redis-7.0.4 && \
    make && \
    make install && \
    yum clean all

# Install Node.js
RUN curl -sL https://rpm.nodesource.com/setup_16.x | bash - && \
    yum install -y nodejs

CMD ["bash"]
