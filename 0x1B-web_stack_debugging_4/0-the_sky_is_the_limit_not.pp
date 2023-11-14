#  fix our stack so that we get to 0

exec { 'replace':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
  returns  => [0],
}
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => Exec['replace'],
}
exec { 'replace':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  notify   => Service['nginx'],
  returns  => [0],
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}
exec { 'replace':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  notify   => Service['nginx'],
  returns  => [0],
  logoutput => true,
}

