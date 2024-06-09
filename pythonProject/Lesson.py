Welcome to Ubuntu 22.04.3 LTS (GNU/Linux 5.15.146.1-microsoft-standard-WSL2 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

This message is shown once a day. To disable it please create the
/home/andrey/.hushlogin file.
andrey@WIN-DD1Q4R6SQRR:~$ /home/andrey/.hushlogin file
-bash: /home/andrey/.hushlogin: No such file or directory
andrey@WIN-DD1Q4R6SQRR:~$ sudo service redis-server start
[sudo] password for andrey:
andrey@WIN-DD1Q4R6SQRR:~$ redis-cli
127.0.0.1:6379> set user:name "Alisa"
OK
127.0.0.1:6379> get user:name
"Alisa"
127.0.0.1:6379> set user:age 18
OK
127.0.0.1:6379> exists user:age
(integer) 1
127.0.0.1:6379> exists user:diploma
(integer) 0
127.0.0.1:6379> get user:age
"18"
127.0.0.1:6379> del user:age
(integer) 1
127.0.0.1:6379> exists user:age
(integer) 0
127.0.0.1:6379> get user:age
(nil)
127.0.0.1:6379> set user:age 27
OK
127.0.0.1:6379> incr user:age
(integer) 28
127.0.0.1:6379> incr user:age 3
(error) ERR wrong number of arguments for 'incr' command
127.0.0.1:6379> incrby user:age 3
(integer) 31
127.0.0.1:6379> get user:age
"31"
127.0.0.1:6379> decr user:age
(integer) 30
127.0.0.1:6379> set user:surname "Smith" EX 10
OK
127.0.0.1:6379> get user:surname
(nil)
127.0.0.1:6379> set user:surname "Andrey" EX 30
OK
127.0.0.1:6379> get user:surname
"Andrey"
127.0.0.1:6379> ttl user:age
(integer) -1
127.0.0.1:6379> persist user:age
(integer) 0
127.0.0.1:6379> lpush user:skills "python" "redis" "sql"
(integer) 3
127.0.0.1:6379> llen user:skils
(integer) 0
127.0.0.1:6379> llen user:skills
(integer) 3
127.0.0.1:6379> rpush user:skills "java"
(integer) 4
127.0.0.1:6379> lrange user:skills 0 -1
1) "sql"
2) "redis"
3) "python"
4) "java"
127.0.0.1:6379> lrange user:skills 0 2
1) "sql"
2) "redis"
3) "python"
127.0.0.1:6379> lpop user:skills
"sql"
127.0.0.1:6379> lrange user:skills 0 -1
1) "redis"
2) "python"
3) "java"
127.0.0.1:6379> sadd user:greades 1 2 3
(integer) 3
127.0.0.1:6379> sadd user:grades 3
(integer) 1
127.0.0.1:6379> sadd user:grades 1
(integer) 1
127.0.0.1:6379> srem user:grades 2
(integer) 0
127.0.0.1:6379> srem user:grades 1
(integer) 1
127.0.0.1:6379> sismember user:grades 3
(integer) 1
127.0.0.1:6379> sismember user:grades 2
(integer) 0
127.0.0.1:6379> smembers user:grades
1) "3"
127.0.0.1:6379> hset user:password value 123
(integer) 1
127.0.0.1:6379> hgetall user:password
1) "value"
2) "123"
127.0.0.1:6379> hdel user:password value
(integer) 1
127.0.0.1:6379> hgetall user:password
(empty array)
127.0.0.1:6379> hset user:password value 123 data 456
(integer) 2
127.0.0.1:6379> hgetall user:password
1) "value"
2) "123"
3) "data"
4) "456"
127.0.0.1:6379> hdel user:password value
(integer) 1
127.0.0.1:6379> hgetall user:password
1) "data"
2) "456"
127.0.0.1:6379>
127.0.0.1:6379>
127.0.0.1:6379> 
(error) ERR unknown command '', with args beginning with:
127.0.0.1:6379> nano myfile.txt
(error) ERR unknown command 'nano', with args beginning with: 'myfile.txt'
127.0.0.1:6379>
127.0.0.1:6379>