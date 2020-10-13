#!/usr/bin/env python3

import paramiko

client = paramiko.client.SSHClient()

client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect("192.168.0.200", username="root", password="4linux")

#### Executar comando ####
# stdin, stdout, stderr = client.exec_command("ls -al")

# if stdout.channel.recv_exit_status() == 0:
#     print(stdout.read().decode("utf-8"))
# else:
#     print(stderr.read().decode("utf-8"))


#### Executar comando com entrada ####
# stdin, stdout, stderr = client.exec_command("read minha_variavel \n echo $minha_variavel")

# stdin.write("Valor x\n")
# stdin.flush()

# print(stdout.read().decode("utf-8"))