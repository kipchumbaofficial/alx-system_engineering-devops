# A Puppet file that changes an OS configuration to allow a user
# 'holberton' to login and open files without error

# Increase hard file limit for user holberton
exec { 'increase-hard-file-limit':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for user holberton
exec { 'increase-soft-file-limit':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
