#! Kills a process

exec {'kill-menow':
    command => 'pkill killmenow',
    path    => 'usr/bin',
}
