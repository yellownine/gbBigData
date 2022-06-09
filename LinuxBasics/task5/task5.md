# Урок 5. Устройство файловой системы Linux. Понятие Файла и каталога

## 1.
- Создать файл file1 и наполнить его произвольным содержимым.
```bash
vagrant@gbLinux:~/task5$ dd if=/dev/urandom of=file1 bs=1k count=1
1+0 records in
1+0 records out
1024 bytes (1.0 kB, 1.0 KiB) copied, 0.00047384 s, 2.2 MB/s
```  

- Скопировать его в file2.
```bash
vagrant@gbLinux:~/task5$ cp file1 file2
```

- Создать символическую ссылку file3 на file1.  

```bash
vagrant@gbLinux:~/task5$ ln -s file1 file3
vagrant@gbLinux:~/task5$ ls -la
total 16
drwxrwxr-x 2 vagrant vagrant 4096 Jun  9 13:17 .
drwxr-xr-x 7 vagrant vagrant 4096 Jun  9 13:11 ..
-rw-rw-r-- 1 vagrant vagrant 1024 Jun  9 13:12 file1
-rw-rw-r-- 1 vagrant vagrant 1024 Jun  9 13:13 file2
lrwxrwxrwx 1 vagrant vagrant    5 Jun  9 13:17 file3 -> file1
```  

- Создать жёсткую ссылку file4 на file1. Посмотреть, какие inode у файлов.
```bash
vagrant@gbLinux:~/task5$ ls -lai
total 20
131103 drwxrwxr-x 2 vagrant vagrant 4096 Jun  9 13:18 .
131074 drwxr-xr-x 7 vagrant vagrant 4096 Jun  9 13:11 ..
131105 -rw-rw-r-- 2 vagrant vagrant 1024 Jun  9 13:12 file1
131104 -rw-rw-r-- 1 vagrant vagrant 1024 Jun  9 13:13 file2
131106 lrwxrwxrwx 1 vagrant vagrant    5 Jun  9 13:17 file3 -> file1
131105 -rw-rw-r-- 2 vagrant vagrant 1024 Jun  9 13:12 file4
```  
Inode для file1 и file4 совпадают!

- Удалить file1. Что стало с остальными созданными файлами? Попробовать вывести их на экран.
```bash
vagrant@gbLinux:~/task5$ ls -lai
total 16
131103 drwxrwxr-x 2 vagrant vagrant 4096 Jun  9 13:20 .
131074 drwxr-xr-x 7 vagrant vagrant 4096 Jun  9 13:11 ..
131104 -rw-rw-r-- 1 vagrant vagrant 1024 Jun  9 13:13 file2
131106 lrwxrwxrwx 1 vagrant vagrant    5 Jun  9 13:17 file3 -> file1
131105 -rw-rw-r-- 1 vagrant vagrant 1024 Jun  9 13:12 file4
```
"Рабочей" осталась только жесткая ссылка на file1, символьную ссылку терминал подсветил красным!  

```bash
vagrant@gbLinux:~/task5$ cat file3
cat: file3: No such file or directory
vagrant@gbLinux:~/task5$ cat file4
-?⺩a?????/k???=?U?XN?;ؿҀ^?L??
...
```

## 2.
- Дать созданным файлам другие, произвольные имена. Создать новую символическую ссылку. Переместить ссылки в другую директорию.

```bash
vagrant@gbLinux:~/task5$ mv file2 elif2
vagrant@gbLinux:~/task5$ ls
elif2  file3  file4
vagrant@gbLinux:~/task5$ ln -s elif2 elif3
vagrant@gbLinux:~/task5$ mkdir links
vagrant@gbLinux:~/task5$ mv elif3 links/
vagrant@gbLinux:~/task5$ mv file3 links/
vagrant@gbLinux:~/task5$ mv file4 links/
vagrant@gbLinux:~/task5$ ls
elif2  links
vagrant@gbLinux:~/task5$ cd links/
vagrant@gbLinux:~/task5/links$ ls
elif3  file3  file4
```
При перемещении в другу директорию символьная ссылка "потеряла" свой референс.

## 3.
- Создать два произвольных файла.  

```bash
vagrant@gbLinux:~/task5$ touch file5
vagrant@gbLinux:~/task5$ touch file6
```

- Первому присвоить права на чтение и запись для владельца и группы, только на чтение — для всех.  

```bash
vagrant@gbLinux:~/task5$ chmod 664 file5
vagrant@gbLinux:~/task5$ ls -la
total 16
drwxrwxr-x 3 vagrant vagrant 4096 Jun  9 13:39 .
drwxr-xr-x 7 vagrant vagrant 4096 Jun  9 13:11 ..
-rw-rw-r-- 1 vagrant vagrant 1024 Jun  9 13:13 elif2
-rw-rw-r-- 1 vagrant vagrant    0 Jun  9 13:39 file5
-rw-rw-r-- 1 vagrant vagrant    0 Jun  9 13:39 file6
drwxrwxr-x 2 vagrant vagrant 4096 Jun  9 13:30 links
```  

- Второму присвоить права на чтение и запись только для владельца.  

```bash
vagrant@gbLinux:~/task5$ chmod 600 file6
vagrant@gbLinux:~/task5$ ls -la
total 16
drwxrwxr-x 3 vagrant vagrant 4096 Jun  9 13:39 .
drwxr-xr-x 7 vagrant vagrant 4096 Jun  9 13:11 ..
-rw-rw-r-- 1 vagrant vagrant 1024 Jun  9 13:13 elif2
-rw-rw-r-- 1 vagrant vagrant    0 Jun  9 13:39 file5
-rw------- 1 vagrant vagrant    0 Jun  9 13:39 file6
drwxrwxr-x 2 vagrant vagrant 4096 Jun  9 13:30 links
```

## 4.
- Создать группу developer и нескольких пользователей, входящих в неё.
```bash
vagrant@gbLinux:~/task5$ sudo groupadd developer
vagrant@gbLinux:~/task5$ sudo useradd -g developer frontend
vagrant@gbLinux:~/task5$ sudo useradd -g developer backend
vagrant@gbLinux:~/task5$ sudo useradd -g developer qaEngeneer
vagrant@gbLinux:~/task5$ cat /etc/group | grep develope
developer:x:1005:
vagrant@gbLinux:~/task5$ cat /etc/passwd | grep 1005
frontend:x:1004:1005::/home/frontend:/bin/sh
backend:x:1005:1005::/home/backend:/bin/sh
qaEngeneer:x:1006:1005::/home/qaEngeneer:/bin/sh
```  

- Создать директорию для совместной работы. Сделать так, чтобы созданные одними пользователями файлы могли изменять другие пользователи этой группы.
```bash
vagrant@gbLinux:~/task5$ mkdir developers_src
vagrant@gbLinux:~/task5$ sudo chown frontend:developer developers_src/
vagrant@gbLinux:~/task5$ sudo chmod -R 655 developers_src/
vagrant@gbLinux:~/task5$ cd developers_src/
vagrant@gbLinux:~/task5/developers_src$ ls -la
total 8
drw-r-xr-x 2 frontend developer 4096 Jun  9 14:01 .
drwxrwxr-x 4 vagrant  vagrant   4096 Jun  9 14:01 ..
```

## 5. * Создать в директории для совместной работы поддиректорию для обмена файлами, но чтобы удалять файлы могли только их создатели.
```bash
vagrant@gbLinux:~/task5/developers_src$ sudo mkdir share
vagrant@gbLinux:~/task5/developers_src$ sudo chown frontend:developer share
vagrant@gbLinux:~/task5/developers_src$ ls -lh
total 4.0K
drwxr-xr-x 2 frontend developer 4.0K Jun  9 14:33 share
vagrant@gbLinux:~/task5/developers_src$ sudo chmod +t share/
vagrant@gbLinux:~/task5/developers_src$ ls -lh
total 4.0K
drwxr-xr-t 2 frontend developer 4.0K Jun  9 14:33 share
```

## 6. * Создать директорию, в которой есть несколько файлов. Сделать так, чтобы открыть файлы можно было посмотреть, только зная имя файла, а через ls список файлов посмотреть было нельзя.
```bash
vagrant@gbLinux:~/task5/developers_src$ sudo mkdir strickted
vagrant@gbLinux:~/task5/developers_src$ cd strickted/
vagrant@gbLinux:~/task5/developers_src/strickted$ touch strickted_file
touch: cannot touch 'strickted_file': Permission denied
vagrant@gbLinux:~/task5/developers_src/strickted$ sudo touch strickted_file
vagrant@gbLinux:~/task5/developers_src/strickted$ cd ..
vagrant@gbLinux:~/task5/developers_src$ ls strickted/
strickted_file
vagrant@gbLinux:~/task5/developers_src$ sudo chmod 333 strickted/
vagrant@gbLinux:~/task5/developers_src$ ls strickted/
ls: cannot open directory 'strickted/': Permission denied
```
