# Change to allow more request

exec { 'fix--for-nginx':
  command  => '/usr/bin/sudo /bin/sed -i "s/ULIMIT=\"\-n [0-9]*\"/ULIMIT=\"\-n 4096\"/g" /etc/default/nginx',
}
->exec { 'restart-nginx':
  command  => '/usr/bin/sudo /etc/init.d/nginx restart',
}
