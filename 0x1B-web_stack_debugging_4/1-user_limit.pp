# changing limits
exec {'sed -i "s/20/10000" /etc/default/nginx':
  path => '/bin',
}
