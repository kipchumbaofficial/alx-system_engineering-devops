# A Manifest file to configure a new ubuntu server

# Update apt-get
exec {'update':
    command => '/usr/bin/apt-get update',
}

# Install nginx
-> package {'nginx':
    ensure => 'present',
}
-> file_line {'add-header':
    path  => '/etc/nginx/nginx.conf',
    match => 'http {',
    line  => "http{\n\tadd_header \"${hostname}\";",
    }
-> exec {'restart':
    command => '/usr/sbin/service nginx restart'
}

