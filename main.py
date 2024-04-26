import paramiko
import time
import credentials

# alamat_host = credentials.host
# alamat_username = credentials.username
# alamat_password = credentials.password
# alamat_destinasi = credentials.destination

def mikrotik_ping(host, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, username=username, password=password)
        print(f"Terhubung ke {host}")

        stdin, stdout, stderr = ssh.exec_command("/ping count=10 address=1.1.1.1")

        while True:
            line = stdout.readline()
            if not line:
                break
            print(line.strip())

    except paramiko.AuthenticationException:
        print("Koneksi gagal, cek kembali username password atau IP address")
    except paramiko.SSHException as sshException:
        print(f"Gagal terhubung: {sshException}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        ssh.close()
        print("Connection closed")

host = credentials.host
username = credentials.username
password = credentials.password
mikrotik_ping(host, username, password)
