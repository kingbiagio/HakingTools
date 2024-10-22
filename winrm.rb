#!/usr/bin/ruby
print "USAGE - ./WinRM.rb\n"
print "USAGE - rlwrap ./WinRM.rb\n"
require 'winrm'
conn = WinRM::Connection.new( 
  #endpoint: 'https://IP:PORT/wsman',
  #transport: :ssl,
  user: 'USER',
  password: 'PASS',
  domain: 'CHILD',
  #:no_ssl_peer_verification => true
)
class String
  def tokenize
    self.
      split(/\s(?=(?:[^'"]|'[^']*'|"[^"]*")*$)/).
      select {|s| not s.empty? }.
      map {|s| s.gsub(/(^ +)|( +$)|(^["']+)|(["']+$)/,'')}
  end
end

print "<--- RUBY WinRM --->\n"
print "\n"
command = ""
conn.shell(:powershell) do | shell|
until command == "exit\n" do
print "PS> "
command = gets
output = shell.run(command) do |stdout, stderr|
STDOUT.print(stdout)
STDERR.print(stderr)
end
end
print "Bye\n"
end
