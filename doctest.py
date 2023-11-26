"""
>>> sys.tracebacklimit = 0
>>> assert sys.version_info > (3, 10, 1), \
'Python 3.11+ is required'
"""

import sys

print('Your Python version:', sys.version[:6])

