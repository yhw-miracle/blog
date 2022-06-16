sudo adduser git

ssh-keygen -t rsa -C 'yhw_software@qq.com'

su git

cd

ssh-keygen -t rsa -C 'yhw_software@qq.com'

touch .ssh/authorized_keys

su yhw-miracle

cd

cat .ssh/id_rsa_pub >> /home/git/authorized_keys

