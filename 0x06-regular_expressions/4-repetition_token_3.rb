#!/usr/bin/env ruby
# Ruby script that accepts one argument and 
# pass it to a regular expression matching method
# regex doesn't contain square brackets

puts ARGV[0].scan(/hbt*n/).join
