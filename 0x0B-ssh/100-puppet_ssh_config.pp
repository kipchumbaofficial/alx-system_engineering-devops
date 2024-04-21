# Puppet file to edit a config

file {'/home/kipchumba/.ssh/config':
    ensure  => present,
    content => "Host 107.22.144.84\n    IdentityFile ~/.ssh/school\n    PasswordAuthentication no",
}
