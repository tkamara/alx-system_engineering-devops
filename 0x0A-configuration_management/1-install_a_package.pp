# installing a package

exec {'flask':
  command => '/usr/bin/pip3 install Flask -V 2.1.0',
}
