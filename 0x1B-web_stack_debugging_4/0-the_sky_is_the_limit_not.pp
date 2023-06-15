# fix failed request error

exec { 'replace':
  provider =>  shell,
  command  =>  'echo "ULIMIT=\"-n 4096\"" > /etc/default/nginx',
  before   =>  Exec['nginx-restart'],
  }


exec { 'nginx-restart':
  provider =>  shell,
  command  => 'sudo service nginx restart',
  }
