# 开启mongodb
workspace=/Users/class-undefined/code/projects/AcademicGarbage
mongod --config $workspace/scripts/res/mongod.conf --fork

# 开启redis
redis-server $workspace/scripts/res/redis.conf
