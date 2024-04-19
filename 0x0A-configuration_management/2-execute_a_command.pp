#! Kills a process

exec {'killmenow':
    command => 'usr/bin/pkill killmenow',
    path    => ['usr/bin'],
}
