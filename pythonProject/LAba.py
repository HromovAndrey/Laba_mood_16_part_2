andrey@WIN-DD1Q4R6SQRR:~$ sudo service redis-server star
[sudo] password for andrey:
Usage: /etc/init.d/redis-server {start|stop|restart|force-reload|status}
andrey@WIN-DD1Q4R6SQRR:~$ redis-cli
127.0.0.1:6379> set name:"John Doe"
(error) ERR wrong number of arguments for 'set' command
127.0.0.1:6379> set user:name
(error) ERR wrong number of arguments for 'set' command
127.0.0.1:6379> set name:user "John Doe"
OK
127.0.0.1:6379> get name
(nil)
127.0.0.1:6379> rpush fruits:"apple"
(error) ERR wrong number of arguments for 'rpush' command
127.0.0.1:6379> rpush:fruits"apple"
(error) ERR unknown command 'rpush:fruitsapple', with args beginning with:
127.0.0.1:6379> lpush:fruits "apple"
(error) ERR unknown command 'lpush:fruits', with args beginning with: 'apple'
127.0.0.1:6379> lpush name:fruits "apple"
(integer) 1
127.0.0.1:6379> lpush name:fruits "banana"
(integer) 2
127.0.0.1:6379> lpush name:fruits "orange"
(integer) 3
127.0.0.1:6379> lrange name: 0 -1
(empty array)
127.0.0.1:6379> lrange name:fruits 0 -1
1) "orange"
2) "banana"
3) "apple"
127.0.0.1:6379> hmset user:1 name "Alica" age 25
OK
127.0.0.1:6379> hgetall user:1
1) "name"
2) "Alica"
3) "age"
4) "25"
127.0.0.1:6379> sadd name:tags "red"
(integer) 1
127.0.0.1:6379> sadd name:tags "green"
(integer) 1
127.0.0.1:6379> sadd name:tags "blue"
(integer) 1
127.0.0.1:6379> sismember name:tags
(error) ERR wrong number of arguments for 'sismember' command
127.0.0.1:6379> sismember name:tags 1
(integer) 0
127.0.0.1:6379> smembers name:tags
1) "red"
2) "green"
3) "blue"
127.0.0.1:6379> incr counter
(integer) 1
127.0.0.1:6379> get counter
"1"
127.0.0.1:6379> del name
(integer) 0
127.0.0.1:6379> del user
(integer) 0
127.0.0.1:6379> hdel name
(error) ERR wrong number of arguments for 'hdel' command
127.0.0.1:6379> exists name
(integer) 0
127.0.0.1:6379> setex message 60 "Hello, Python"
OK
127.0.0.1:6379> flushall
OK
127.0.0.1:6379> geoa geo_locations 13.361389 38.115556 "Palermo"
(error) ERR unknown command 'geoa', with args beginning with: 'geo_locations' '13.361389' '38.115556' 'Palermo'
127.0.0.1:6379> geoadd geo_locations 13.361389 38.115556 "Palermo"
(integer) 1
127.0.0.1:6379> geoadd geo_locations 15.087269 37.502669 "Catania"
(integer) 1
127.0.0.1:6379> geoadd geo_locations 13.583333 37.316667 "Agrigento"
(integer) 1
127.0.0.1:6379> hset students "John" 90
(integer) 1
127.0.0.1:6379> hset students "Alice" 85
(integer) 1
127.0.0.1:6379> hset students "Bob" 78
(integer) 1
127.0.0.1:6379> hgetall students
1) "John"
2) "90"
3) "Alice"
4) "85"
5) "Bob"
6) "78"
127.0.0.1:6379> hset students "Alice" 95
(integer) 0
127.0.0.1:6379> hgetall students
1) "John"
2) "90"
3) "Alice"
4) "95"
5) "Bob"
6) "78"
127.0.0.1:6379> pfadd unique_user "user1"
(integer) 1
127.0.0.1:6379> pfadd unique_user "user2"
(integer) 1
127.0.0.1:6379> pfadd unique_user "user3"
(integer) 1
127.0.0.1:6379> multi
OK
127.0.0.1:6379(TX)> rpush tasks "task1"
QUEUED
127.0.0.1:6379(TX)> hmset project:1 name "Project1" status "in-progress"
QUEUED
127.0.0.1:6379(TX)> exec
1) (integer) 1
2) OK
127.0.0.1:6379> redis-cli shutdown
(error) ERR unknown command 'redis-cli', with args beginning with: 'shutdown'
127.0.0.1:6379>