# 呆瓜的 Docker 學習筆記

> 以防本呆瓜哪天忘記, 在這裡紀錄了一些 docker 的使用筆記

## docker

- install: `sudo apt-get install docker`
  + `sudo usermod -aG docker <user_name>`
- build image: `docker build`
- view all image: `docker images -a`
- create container: `docker run <image_id>`
- view all container: `docker ps -a`
- get container port `docker port <container_id/container_name>`
- stop container: `docker stop <container_id/container_name>`
- restart container: `docker restart <container_id/container_name>`
- remove container: `docker rm <container_id/container_name>`
- remove image: `docker rmi <image_id/image_name>`

## MS SQL Server

- install: `sudo docker pull mcr.microsoft.com/mssql/server:2017-latest`
- build: `sudo docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=<YourStrong@Password>" -p 1433:1433 -d mcr.microsoft.com/mssql/server:2017-latest`
- change SA password: `sudo docker exec -it <container_id/container_name> /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "<YourStrong@Password>" -Q 'ALTER LOGIN SA WITH PASSWORD="<YourNewStrong@Password>"'`
- connect to SQL server: `sudo docker exec -it <container_id/container_name> "bash"`
- connect locally with sqlcmd: `/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "<YourNewStrong@Password>"`
- exit the `sqlcmd` command prompt: `QUIT`
- connect from outside the container: `sqlcmd -S <ip_address>,1433 -U SA -P "<YourNewStrong@Password>"`
