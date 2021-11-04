import genieparse.genieparse as gp
import json

if __name__ == '__main__':
   output = '''
   Cisco IOS Software, s2t54 Software (s2t54-ADVIPSERVICESK9-M), Version 15.2(1)SY6, RELEASE SOFTWARE (fc5)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Fri 09-Feb-18 11:27 by prod_rel_team

ROM: System Bootstrap, Version 12.2(50r)SYS3, RELEASE SOFTWARE (fc1)

ch-ins-33ru21-cs-00 uptime is 1 year, 8 weeks, 6 days, 16 hours, 52 minutes
Uptime for this control processor is 1 year, 8 weeks, 6 days, 16 hours, 44 minutes
System returned to ROM by power on
System restarted at 21:03:47 MEST Wed Sep 2 2020
System image file is "bootdisk:s2t54-advipservicesk9-mz.SPA.152-1.SY6.bin"
Last reload reason: power-on



This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

cisco WS-C6509-E (M8572) processor (revision ) with 1785856K/262144K bytes of memory.
Processor board ID SMC13010067
 CPU: MPC8572_E, Version: 2.2, (0x80E80022)
 CORE: E500, Version: 3.0, (0x80210030)
 CPU:1500MHz, CCB:600MHz, DDR:600MHz
 L1:    D-cache 32 kB enabled
        I-cache 32 kB enabled

Last reset from power-on
7 Virtual Ethernet interfaces
99 Gigabit Ethernet interfaces
50 Ten Gigabit Ethernet interfaces
2543K bytes of non-volatile configuration memory.

Configuration register is 0x2102


   '''
   cmd = 'show version'
   os = 'ios'
   test = gp.parse(output, cmd, os)
   print(json.dumps(test, indent=1))