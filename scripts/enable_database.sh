# 开启mongodb
workspace=/home/class-undefined/code/AcademicGarbage
mongod --config $workspace/scripts/res/mongod.conf --fork

# 开启redis
redis-server $workspace/scripts/res/redis.conf
