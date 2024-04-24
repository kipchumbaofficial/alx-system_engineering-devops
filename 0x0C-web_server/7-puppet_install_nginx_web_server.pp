# A Puppet manifest that configures a server. It:
# - Updates the server
# - Installs an Nginx server
# - Configures the Nginx web server
package {'nginx':
    ensure   => 'present';
}

exec {'nginx installation':
    command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
    provider => shell,
}

exec {'Message':
    command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
    provider => shell,
}

exec {'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/www.youtube.com/watch?v=QH2-TGUlwu4;\\n\\t}/" /etc/nginx/sites-available/default':
    provider => shell,
}

exec {'run':
    command  => 'sudo service nginx restart',
    provider => shell,
}
