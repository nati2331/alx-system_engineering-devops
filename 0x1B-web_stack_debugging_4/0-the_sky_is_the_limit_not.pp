# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Increase the traffic amount in /etc/default/nginx
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/bin:/bin',
  unless  => 'grep "4096" /etc/default/nginx',
}

# Restart Nginx service using the service command
exec { 'nginx-restart':
  command => '/usr/sbin/service nginx restart',
  path    => '/sbin:/bin:/usr/sbin:/usr/bin',
  require => Package['nginx'],
}

