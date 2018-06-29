#!/usr/bin/python


import sys
from datetime import *

try:
    from scapy.all import *
    from logging import *
    from termcolor import *
    conf.verb = 0
except ImportError:
    print '[!] Failed to import required library "Scapy" "Termcolor"'
    print '[+] Install requires library by typing "pip install library"'
    print '[!] Quitting ...'
    sys.exit(1)

class ArpEnumerator(object):
    def __init__(self, interface=False, passive=False, range=False):
        self.interface        = interface
        self.passive          = passive
        self.range            = range
        self.discovered_hosts = {}
        self.filter           = 'arp'
        self.starttime        = datetime.now()

    def passive_handler(self, pkt):
        try:
            if not pkt[ARP].psrc in self.discovered_host.keys():
                print "%s - %s" %(pkt [ARP].psrc, pkt[ARP].hwsrc)
                self.discovered_hosts [pkt [ARP].psrc] = pkt[ARP].hwsrc
        except Exception:
            return
        except KeyboardInterrupt:
            return
    
    def passive_sniffer(self):
        if not self.range:
            print '[!] No IP/Subnet Given, Sniffing on all Network ..'
            print '[*] Starting Passive Scan ...'
        else:
            self.filter += 'and (net%s)' %(self.range)
        print '[*] Sniffing started on %s\n' %(self.interface)
        try:
            sniff(filter=self.filter, prn=self.passive_handler, store=0)
        except Exception:
            print '[!] An ERROR Occured'
            print '[*] Stopping..'
            return
        print '\n[*] Sniffing Stopped ..'
        self.duration = datetime.now() - self.starttime
        print '[*] Sniff Duration: %s' %(self.duration)
    
    def active_scan(self):
        print '[*] Starting Active Scan on Network..'
        sys.stdout.flush()
        try:
            ans = srp(Ether(dst ='FF:FF:FF:FF:FF:FF')/ARP(pdst = self.range), timeout = 2, iface = self.interface, inter = 0.1)[0]
        except Exception:
            print '[!] QUITTING.. An ERROR Occured'
            return
        print '<[+] SHOWING DISCOVERED HOSTS "[ACTIVE SCAN]">\n'
        for snd, rcv in ans:
            self.discovered_hosts[rcv[ARP].psrc] = rcv[ARP].hwsrc
            print '%s - %s' %(rcv[ARP].psrc, rcv[ARP].hwsrc)
        print '[*] Scan Complete..'
        self.duration = datetime.now() - self.starttime
        print '[*] Scan Duration: %s' % (self.duration)
        return
    def output_results(self, path):
        print '[+] Writing on Output File..'
        try:
            with open(path, 'w') as file:
                file.write('Discovered Hosts:\n')
                for key, val in self.discovered_hosts.items():
                    file.write('%s - %s\n' %(key, val))
                file.write('\n[+] Scan Duration:%s\n' % (self.duration))
            print '\n[+] ..Succesfully Wrote to %s..' % (path)
            return
        except IOError:
            print '[!] UNABLE to Write Output File..'
            return

if __name__ == '__main__' :
    import argparse
    parser = argparse.ArgumentParser(description = '< ARP SENDER TOOL V 1.1>')
    parser = argparse.ArgumentParser(description ='Author: ScinkaBestia')
    parser.add_argument('-i', '--interface EX: wlan0', help ='Network Interface', action ='store', dest ='interface', default =False)
    parser.add_argument('-r', '--range', help ='Network Range IP/CIDR', action ='store', dest='range', default= False)
    parser.add_argument('--passive', help= 'Enabling PASSIVE MODE, only Sniffing (No ARP sent)', action= 'store_true', dest='passive', default=False)
    parser.add_argument('-o', '--output', help='Output Scan to given File', action= 'store' , dest= 'file', default= False)
    args = parser.parse_args()

    if not args.interface:
        parser.error('[!] No Interface given..')
    elif (not args.passive) and (not args.range):
        parser.error('[!] No Range Specified fot Scan..')
    else:
        pass

if args.passive:
    if not not args.range:
        enum = ArpEnumerator(interface = args.interface, passive=True, range=args.range)
        enum.passive_sniffer()
    else:
        enum = ArpEnumerator(interface = args.interface, passive = True)
        enum.passive_sniffer()
else :
    enum = ArpEnumerator(interface = args.interface, range = args.range)
    enum.active_scan()
    if not not args.file:
        enum.output_results(args.file)