# A Puppet script increases the amount of traffic an Nginx server can handle
# Increase the ULIMIT of the default nginx file
exec { 'fix-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
-> exec { 'nginx-restarter':
  command => 'sudo nginx restart',
  path    => '/etc/init.d/'
}
