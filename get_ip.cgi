#!/usr/bin/perl -w

use strict;
use CGI qw( :all );

print header(), start_html( -title => 'get_ip' );

store_ip() if defined( param( "store" ) );

if ( !-e "ip" ) {
  print "No ip file found\n";
  exit 0;
}

open( FILE, "ip" ) or die $!;
my $text = <FILE>;
chomp( $text );
close( FILE );

my ( $ip, $time ) = split( "\t", $text );
print "<pre>IP address: $ip\nStored at $time</pre>", end_html();

sub store_ip {
  open( FILE, "> ip" ) or die $!;
  print FILE $ENV{REMOTE_ADDR}, "\t", scalar( localtime() ), "\n";
  close( FILE );
}
