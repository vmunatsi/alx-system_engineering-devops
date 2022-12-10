# Configured to use the private key ~/.ssh/holberton

file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  match   => '^   PasswordAuthentication',
  line    => '   PasswordAuthentication no',
  replace => 'true',
}
file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => '   IdentityFile ~/.ssh/holberton',
}
