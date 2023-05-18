# changing limits
exec {'sed -i "s/20/10000" /etc/default/nginx':
  path => '/bin',
}

exec {'sed -i "s/50/10000" /etc/default/nginx':
  path => '/bin',
}
