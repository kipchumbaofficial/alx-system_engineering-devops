# A puppet manifest to fix a wordpress server
$settings_file = '/var/www/html/wp-settings.php'

exec { 'fix-wordpress':
  command => "sed -i 's/phpp/php/g' ${settings_file}",
  path    => ['/bin','/usr/bin']
}
