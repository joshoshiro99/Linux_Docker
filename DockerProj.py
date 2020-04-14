import docker

#create a docker client from the docker application running in the background.
client = docker.from_env()

#create a detached docker container with terminal functionality
container = client.containers.run("ubuntu",stdin_open=True,tty=True, detach = True)

#debugging docker status remaining as "created" only
status = container.status
container.start()
status = container.status

#command loop - take user command as cmd, run cmd in container, return logs, repeat until "exit"
cmd = ""
while cmd != "exit":
    cmd = input("The following commands are available for you to use: echo, ls , cd, touch, and ping\ntype \"exit\" to quit:\n")
    if cmd == "exit":
        break
    else:
        container.exec_run(cmd)
        print(container.logs())