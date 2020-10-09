#!/usr/bin/env python3

import docker

docker_con = docker.DockerClient("192.168.0.200:2376")

# container = docker_con.containers.run(
#     'debian:latest', '/bin/bash',
#     name='learn', detach=True, tty=True
# )

# print(container)


# for container in docker_con.containers.list(all=True):
#     print(container)

# learn_container = docker_con.containers.get("flask-app")
# learn_container.stop()
# learn_container.start()
# print(learn_container.stats(stream=False))
# learn_container.attach()
# learn_container.remove()
# print(learn_container.exec_run("ls -la"))
