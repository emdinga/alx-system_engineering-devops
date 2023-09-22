# Puppet manifest to install Flask with a specific version
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

