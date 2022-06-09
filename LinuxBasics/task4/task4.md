## 1. Потоки ввода/вывода.
- Создать файл, используя команду echo.  
```bash
vagrant@gbLinux:~$ echo 'sometext for new file' > newfile
vagrant@gbLinux:~$ cat newfile
sometext for new file  
```
- Используя команду cat, прочитать содержимое всех файлов каталога etc, ошибки перенаправить в отдельный файл.  
```bash
vagrant@gbLinux:~$ cat /etc/* 2> errors.log
```

## 2. Конвейер (pipeline).
- Использовать команду cut на вывод длинного списка каталога, чтобы отобразить только права доступа к файлам.
```bash
vagrant@gbLinux:~$ ls /etc -la | grep '^-' | cut -d' ' -f1  
```  
- Затем отправить в конвейере этот вывод на sort и uniq, чтобы отфильтровать все повторяющиеся строки.  
```bash
vagrant@gbLinux:~$ ls /etc -la | grep '^-' | cut -d' ' -f1 | sort | uniq
```

## 3. Управление процессами.  
- Изменить конфигурационный файл службы SSH: /etc/ssh/sshd_config, отключив аутентификацию по паролю PasswordAuthentication no. Выполните рестарт службы systemctl restart sshd (service sshd restart), верните аутентификацию по паролю, выполните reload службы systemctl reload sshd (services sshd reload). В чём различие между действиями restart и reload?
```bash
vagrant@gbLinux:~$ sudo nano /etc/ssh/sshd_config
```  
...редактируем, как сказано в задании.  
```bash
vagrant@gbLinux:~$ systemctl restart sshd
==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-units ===
Authentication is required to restart 'ssh.service'.
Multiple identities can be used for authentication:
 1.  vagrant,,, (vagrant)
 2.  ,,, (sudo2)
Choose identity to authenticate as (1-2): 1
Password:
==== AUTHENTICATION COMPLETE ===   
```  
...опять редактируем, как сказано в задании.
```bash
vagrant@gbLinux:~$ systemctl reload sshd
==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-units ===
Authentication is required to reload 'ssh.service'.
Multiple identities can be used for authentication:
 1.  vagrant,,, (vagrant)
 2.  ,,, (sudo2)
Choose identity to authenticate as (1-2): 1
Password:
==== AUTHENTICATION COMPLETE ===
```
Reload отличается от Restart тем, что reload не останавливает процесс, а просто говорит процессу перечитать файл настроек/конфигурации.   
- Создайте файл при помощи команды cat > file_name, напишите текст и завершите комбинацией ctrl+d. Какой сигнал передадим процессу?
```bash
sometextvagrant@gbLinux:~$ cat > newfile2
some text for new file 2
vagrant@gbLinux:~$ cat newfile2
some text for new file 2
```
Ctrl+d передает процессу сигнал EOF. Оболочка, получив EOF в stdin, реагирует выходом из процесса.

## 4. Сигналы процессам.
- Запустите mc. Используя ps, найдите PID процесса, завершите процесс, передав ему сигнал 9.
```bash
vagrant@gbLinux:~$ sudo apt install mc
Reading package lists... Done
...
vagrant@gbLinux:~$ mc
vagrant@gbLinux:~$ ps -a | grep mc
  13336 pts/0    00:00:00 mc
vagrant@gbLinux:~$ kill -s 9 13336
```
