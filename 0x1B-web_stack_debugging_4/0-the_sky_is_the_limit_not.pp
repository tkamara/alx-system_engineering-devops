# ensuring Nginx requests don't fail
exec {'correction':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/bin',
}

exec {'service nginx restart':
  path => '/usr/bin'
}