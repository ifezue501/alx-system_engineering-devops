# creates a custom HTTP header
exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

file_line { 'custom-header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => 'add_header X-Served-By $hostname;',
  after  => 'listen 80 default_server;',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [Package['nginx'], File_line['custom-header']],
}
