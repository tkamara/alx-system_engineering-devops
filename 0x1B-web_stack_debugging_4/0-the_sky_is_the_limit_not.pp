exec {'correction':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/bin',
}

service {'nginx':
  ensure    => running,
  subscribe => Exec['correction'],
}
