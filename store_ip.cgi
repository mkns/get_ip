#!/usr/bin/perl -w

use strict;
use LWP::Simple;

die "Need URL as parameter!" unless defined( $ARGV[0] ) && length( $ARGV[0] );

my $response = get $ARGV[0];
