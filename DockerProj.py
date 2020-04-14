import docker

client = docker.from_env()
container = client.containers.run("ubuntu",stdin_open=True,tty=True, detach = True)
status = container.status
container.start()
status = container.status
cmd = ""
while cmd != "exit":
    cmd = input("The following commands are available for you to use: echo, ls , cd, touch, and ping\ntype \"exit\" to quit:\n")
    if cmd == "exit":
        break
    else:
        container.exec_run(cmd)
        print(container.logs())