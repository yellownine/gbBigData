# Урок 7. Управление пакетами и репозиториями. Основы сетевой безопасности  

## 1. Подключить репозиторий с nginx любым удобным способом, установить nginx и потом удалить nginx, используя утилиту dpkg.
Создаем файл с описанием репозитория для nginx
```bash
vagrant@gbLinux:~$ sudo nano /etc/apt/sources.list.d/nginx.list
```
Добавляем в него строчку (у меня тоже версия focal)
```
deb http://nginx.org/packages/ubuntu focal nginx
```
Регистрируем ключ для авторизации в репозитории
```bash
vagrant@gbLinux:~$ curl -fsSL https://nginx.org/keys/nginx_signing.key | sudo apt-key add -
OK
```
Обновляем локальный индекс репозиториев
```bash
vagrant@gbLinux:~$ sudo apt update
Get:1 http://nginx.org/packages/ubuntu focal InRelease [3,587 B]
..
```
Оказалось, что этот репозиторий не поддерживает релизы с архитектурой i386, но в списках был и другой репозиторий для nginx
Устанавливаем nginx  
```bash
vagrant@gbLinux:~$ sudo apt install nginx
```
Удаляем с помощью dpkg
```bash
vagrant@gbLinux:~$ man dpkg
vagrant@gbLinux:~$ dpkg -r nginx
dpkg: error: requested operation requires superuser privilege
vagrant@gbLinux:~$ sudo dpkg -r nginx
(Reading database ... 42003 files and directories currently installed.)
Removing nginx (1.22.0-1~focal) ...
Processing triggers for man-db (2.9.1-1) ...
```
2. Установить пакет на свой выбор, используя snap.  
```bash
vagrant@gbLinux:~$ man snap
vagrant@gbLinux:~$ sudo snap install --stable nginx
```
После непродолжительного гугленья пришел к выводу, что пакетов для работы в оболочке то ли нет, то ли они не популярны, а у меня нет Иксов в Linux. Sorry.

3. Настроить iptables: разрешить подключения только на 22-й и 80-й порты.
Сначала попробовал оставить только порт 80 и потерял свою ВМ. Перезапустился и сделал так:
```bash
vagrant@gbLinux:~$ sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
vagrant@gbLinux:~$ sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
vagrant@gbLinux:~$ sudo iptables -A INPUT -j DROP
vagrant@gbLinux:~$
vagrant@gbLinux:~$ sudo iptables -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         
ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:http
ACCEPT     tcp  --  anywhere             anywhere             tcp dpt:ssh
DROP       all  --  anywhere             anywhere            
Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         
Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         
vagrant@gbLinux:~$
```
4. Настроить проброс портов локально с порта 80 на порт 8080.  
Сейчас на это не хватает времени, но разберусь попозже - настройка сети мне очень интересна.
