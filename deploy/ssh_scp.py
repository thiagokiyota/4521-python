#!/usr/bin/env python3

import paramiko
import scp
import sys

local = sys.argv[1]

client = paramiko.client.SSHClient()
pemkey = paramiko.RSAKey.from_private_key_file("/var/opt/4521/deploy/4521.pem")
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect("52.15.130.194", username="ubuntu", pkey=pemkey)
client.exec_command("rm -rf /tmp/DeployEC2")

handler = scp.SCPClient(client.get_transport())

handler.put("local", recursive=True, remote_path="/tmp")

handler.close()
client.close()
