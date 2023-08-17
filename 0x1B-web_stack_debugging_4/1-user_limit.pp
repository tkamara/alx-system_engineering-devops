# changing limits

exec {'hard limit fix':
  command => 'sed -i "s/5/20000/" /etc/security/limits.conf',
  path    => '/bin',
}

exec {'soft limit fix':
  command => 'sed -i "s/4/20000/" /etc/security/limits.conf',
  path    => '/bin',
}
