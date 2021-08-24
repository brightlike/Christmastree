# 常用工具集


## crontab
系统自带定时任务
cron是一个linux下 的定时执行工具，可以在无需人工干预的情况下运行作业。
　　service crond start    //启动服务
　　service crond stop     //关闭服务
　　service crond restart  //重启服务
　　service crond reload   //重新载入配置
　　service crond status   //查看服务状态

crontab -e 写规则
crontab -l 查看当前所有规则
crontab -r 清除所有规则


格式
# m h dom mon dow user	command
30 * * * * root cd / && run-parts --report /etc/cron.hourly

## nmap
查询端口等
nmap -sS 192.168.0.1 -p* |grep open



## nginx
代理、转发 负载等

### 方向代理示例
 server {
 listen 80;
 server_name xxx;
 access_log /var/log/nginx/xxx.access_log;
 error_log /var/log/nginx/xxx.error_log;

 location /static/  {
     alias /data/vhost/xxx/static/;
     expires      30d;
 }

 location / {
     proxy_pass http://127.0.0.1:8080;
 proxy_redirect off;
     proxy_set_header        Host    $host;
     proxy_set_header        REMOTE_ADDR     $remote_addr;
     proxy_set_header        X-Forwarded-For $proxy_add_x_forwarded_for;
     real_ip_recursive on;
 proxy_max_temp_file_size 0;
     proxy_connect_timeout      90;
     proxy_send_timeout         90;
     proxy_read_timeout         90;
     proxy_buffer_size          4k;
     proxy_buffers              4 32k;
     proxy_busy_buffers_size    64k;
     proxy_temp_file_write_size 64k;
 }
}

