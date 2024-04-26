import paramiko
import credentials

# alamat_host = credentials.host
# alamat_username = credentials.username
# alamat_password = credentials.password
# alamat_destinasi = credentials.destination

def mikrotik_traceroute_final(host, username, password, destination):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, username=username, password=password)
        print(f"Terhubung ke {host}")
        stdin, stdout, stderr = ssh.exec_command(f"/tool traceroute address={destination} count=1")
        output = stdout.read().decode()

        print(output)

    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials")
    except paramiko.SSHException as sshException:
        print(f"Could not establish SSH connection: {sshException}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ssh.close()
        print("Connection closed")

host = credentials.host
username = credentials.username
password = credentials.password
destination = credentials.destination
mikrotik_traceroute_final(host, username, password, destination)
