#!/usr/bin/env python3

import jenkins

jenkins_con = jenkins.Jenkins(
    "http://192.168.0.200:8080",
    username="4linux", password="4linux123"
)

# print(jenkins_con.get_whoami())
# print(jenkins_con.get_version())

# jenkins_con.create_job('Teste', jenkins.EMPTY_CONFIG_XML)

# queue = jenkins_con.build_job('Python-Job')
# print(jenkins_con.get_queue_item(queue))

# print(jenkins_con.get_jobs())

# print(jenkins_con.get_job_config("Python-Job"))

# xml = jenkins.EMPTY_CONFIG_XML
# jenkins_con.reconfig_job("Python-Job", xml)