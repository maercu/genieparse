import genieparse
import json

if __name__ == '__main__':
   output = '''
   <OUTUPT>
   '''
   cmd = 'show xyz'
   os = 'ios'
   test = genieparse.parse(output, cmd, os)
   print(json.dumps(test, indent=1))