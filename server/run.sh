source ~/.bashrc
cd /project/server
nginx
redis-server /conf/redis.conf
mongod --config /conf/mongod.conf --fork
conda activate py390
python start.py
