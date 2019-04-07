#!/usr/bin/env python3

from coll import Collider, md5pad, filter_disallow_binstrings
import os
import base64

# We generate a file of the form:
"""
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#

diff = '''<one of 2 collision blocks>'''
same = '''<first of the 2 collision blocks>'''

if (same == diff):
    print "good"

else:
    print "evil"
"""


collider = Collider(blockfilter=filter_disallow_binstrings([b'\0', b"'''"]))

prefix1 = b"""#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#"""
prefix2 = b"""\ndiff = '''"""

# Ensure prefix is a multiple of 64 bytes
prefix = prefix1 + md5pad(prefix1 + prefix2, b' ') + prefix2

# Load the first half of the collision files that opens the 'diff' variable delcaration
collider.bincat(prefix)
# Fill in the 'diff' variable with 2 different blocks that may be chosen
collider.safe_diverge()

postfix = b"""'''
same = '''"""

c1, c2 = collider.get_last_coll()

postfix += c1

postfix += b"""'''

if (same == diff):
    print "MD5 is secure!"

else:
    print "Just kidding!"

"""

# Close the 'diff' variable string and declare the 'same' variable to always have the 1st collision block
# Thus for one file: same == diff, but for the other: same != diff
collider.bincat(postfix)

# Write out the good and evil scripts
cols = collider.get_collisions()

GOOD = 'out_py_good.py'
EVIL = 'out_py_evil.py'
GOOD = 'MD5_is_secure.py'
EVIL = 'Just_kidding.py'

with open(GOOD, 'wb') as good:
    good.write(next(cols))
    
with open(EVIL, 'wb') as evil:
    evil.write(next(cols))

os.system('chmod +x {} {}'.format(GOOD, EVIL))

#nc = Netcat('140.112.31.96', 10150)
#nc.read()

with open(GOOD, 'rb') as R:
    #nc.write(bytes(base64.b64encode(R.read()))[2:-1])
    print (str(base64.b64encode(R.read()))[2:-1])

with open(EVIL, 'rb') as R:
    #nc.write(str(base64.b64encode(R.read()))[2:-1])
    print (str(base64.b64encode(R.read()))[2:-1])

