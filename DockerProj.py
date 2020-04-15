import docker

#create a docker client from the docker application running in the background.
client = docker.from_env()

#create a detached docker container with terminal functionality
container = client.containers.run("ubuntu",stdin_open=True,tty=True, detach = True)

#change container status from "created" to "running"
status = container.status
container.start()
container.reload()
status = container.status

#command loop - take user command as cmd, run cmd in container, return logs, repeat until "exit"
cmd = ""
while cmd != "exit":
    cmd = input("The following commands are available for you to use: echo, ls, touch, mkdir and rmdir\ntype \"exit\" to quit:\n")
    if cmd == "exit":
        break
    else:
        command=["/bin/sh", "-c", cmd]
        tuple = container.exec_run(command, tty=True,stdin=True,stdout=True)
        print(tuple[1])