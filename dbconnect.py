import MySQLdb
import sshtunnel

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com'),
    ssh_username='smyu24', ssh_password='/',
    remote_bind_address=('1.mysql.pythonanywhere-services.com', 3306)
) as tunnel:
    connection = MySQLdb.connect(
        user='smyu24',
        passwd='/',
        host='127.0.0.1', port=tunnel.local_bind_port,
        db='smyu24$1',
    )
    # Do stuff
    connection.close()