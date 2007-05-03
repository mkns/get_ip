#!/usr/bin/perl -w

use strict;
use CGI qw( :all );

print header();

store_ip() if defined( param( "store" ) );

if ( !-e "ip" ) {
  print "No ip file found\n";
  exit 0;
}

open( FILE, "ip" ) or die $!;
my $ip = <FILE>;
chomp( $ip );
close( FILE );

print "IP address: $ip\n";

sub store_ip {
  open( FILE, "> ip" ) or die $!;
  print FILE $ENV{REMOTE_ADDR}, "\n";
  close( FILE );
}
