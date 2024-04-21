# Puppet file to edit a config

file_line {'PasswordAuth':
    ensure => present,
    path   => '/etc/ssh/sshd_config',
    line   => '    PasswordAuthentication no',
}

file_line {'Set private':
    ensure => present,
    path   => '/etc/ssh/sshd_config',
    line   => '    IdentityFile ~/.ssh/school',
}
