import paramiko


def executeCommand(cmd):
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd,  get_pty=True)
    ssh_stdout.channel.close()
    ssh_stderr.channel.close()
    print("$ " + cmd)
    stdout = ssh_stdout.read().decode('UTF-8')
    stderr = ssh_stderr.read().decode('UTF-8')
    if stdout != '':
        print(stdout)
    if stderr != '':
        print(stderr)


server_details = open("C:\\Users\\akshay.aradhya\\Documents\\API Keys\\RHEL_1.txt", "r")
HOST = server_details.readline().rstrip('\n')
PORT = 22
USER = server_details.readline().rstrip('\n')
PASS = server_details.readline().rstrip('\n')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, username=USER, password=PASS)

# executeCommand("cd chat-memory;nohup java -cp 'lib/*' com.arise.chat.memory.App &")

# executeCommand("cd chat-server/arise-chat-server-1.0-SNAPSHOT/bin; sudo -S -p'" +
#                PASS + "' nohup bash arise-chat-server -Dhttp.port=80 &")

executeCommand("echo 'hi'")


ssh.close()
