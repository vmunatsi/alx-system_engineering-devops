# Set header with puppet

package { 'nginx':
  provider => 'gem',
}

file { 'holberton school':
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Holberton School',
}

file_line { 'Set rewrite':
  path    => '/etc/nginx/sites-available/default',
  match   => '^server {$',
  line    => 'server {\n\trewrite ^\/redirect_me https:\/\/www.google.com\/ permanent;',
  replace => 'true',
}

file { 'Display 404-no-found':
  path    => '/var/www/html/404_error.html',
  content => 'Ceci n\'est pas une page',
}

file_line { 'Set 404-no-found':
  path    => '/etc/nginx/sites-available/default',
  match   => '^server {$',
  line    => 'server {\n\terror_page 404 \/404_error.html;\n\tlocation = \/404_error.html {\n\t\troot \/var\/www\/html;\n\t\tinternal;\n\t}',
  replace => 'true',
}

file_line { 'Set header':
  path    => '/etc/nginx/sites-available/default',
  match   => 'location \/ {',
  line    => 'location \/ {\n\t\tadd_header X-Served-By \$hostname;\n',
  replace => 'true',
}

exec { 'service nginx restart':
  command => 'service nginx restart',
  path    => '/usr/bin/',
}
