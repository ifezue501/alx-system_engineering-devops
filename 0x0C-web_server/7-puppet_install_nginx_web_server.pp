# Install Nginx web server (w/ Puppet)
package { 'nginx':
  ensure => installed,
}

file_line { 'configure redirection':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'location /redirect_me { return 301 https://www.youtube.com/watch?v=dQw4w9WgXcQ; }',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
