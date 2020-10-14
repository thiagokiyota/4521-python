#!/usr/bin/env python3

import boto3

ec2 = boto3.resource("ec2")

#### Criar um security group ####
# security_group = ec2.create_security_group(
#     GroupName = "Grupo Script",
#     Description = "Criado por script"
# )
# print(security_group)

#### Listar os security groups ####
# security_groups = ec2.security_groups.all()
# for group in security_groups:
#     print(group.group_name, group.group_id)

#### Criar e remover regras em um security group ####
# security_group = ec2.SecurityGroup("sg-9a922af0")
# security_group.authorize_ingress(
#     FromPort = 80,
#     ToPort = 80,
#     CidrIp = "0.0.0.0/0",
#     IpProtocol = "tcp"
# )
# security_group.revoke_ingress(
#     FromPort = 80,
#     ToPort = 80,
#     CidrIp = "0.0.0.0/0",
#     IpProtocol = "tcp"
# )

#### Apagar um security group ####
# security_group.delete()

#### Listar todas as instancias EC2 ####
# instances = ec2.instances.all()
# for instance in instances:
#     print(instance.instance_id, instance.instance_type)

#### Listar instancias utilizando filtro ####
# filtered_instances = ec2.instances.filter(
#     Filters = [
#         {
#             "Name": "instance-state-name",
#             "Values": ["running"]
#         }
#     ]
# )
# for instance in filtered_instances:
#     print(instance.instance_id, instance.instance_type)

#### Criar uma instancia EC2 ####
# new_instance = ec2.create_instances(
#     ImageId = "ami-6a003c0f",
#     InstanceType = "t2.micro",
#     MinCount = 1,
#     MaxCount = 1,
#     KeyName = "4521",
#     SecurityGroupIds = "sg-5dad1537"
# )
# print(new_instance)

# print(ec2.instances.filter(InstanceIds=["i-09044bb4b518e61c5"]).stop())
# print(ec2.instances.filter(InstanceIds=["i-09044bb4b518e61c5"]).start())
# print(ec2.instances.filter(InstanceIds=["i-09044bb4b518e61c5"]).reboot())
# print(ec2.instances.filter(InstanceIds=["i-09044bb4b518e61c5"]).terminate())
