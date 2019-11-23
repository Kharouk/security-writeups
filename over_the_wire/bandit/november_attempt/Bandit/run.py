import paramiko

client = paramiko.SSHClient()
hostname = "bandit.labs.overthewire.org"
username = input("What level do you want to access? [int]: ")
password = input(f"What is the flag won from from level bandit{int(username) - 1}? ")
port = 2220

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, port=port, username=f"bandit{username}", password=password)


def exec_command():
    print(f"You're in.\nHere is the connection if needed:\nssh {hostname} "
          f"-lbandit{username} -p{port}\nPassword is {password}")
    correct = "n"
    flag = ""
    command = ""
    while correct != "y":
        command = input("What command did you want to use? ")
        ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(command)
        flag = "".join(ssh_stdout.readlines())
        flag = flag.replace("\n", "")
        print(flag)
        correct = input('did you get the flag? [y,n]: ')
    else:
        file = open('passwords.txt', 'a')
        file.write(f"bandit{username} - {flag} - `{command}`\n".strip())
        file.close()
        print(f"You just hacked the bandit{username} level. Great job!")


if __name__ == '__main__':
    exec_command()