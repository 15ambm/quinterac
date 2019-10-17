#!c:\users\owner\documents\repos\quinterac\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Quinterac==0.1','console_scripts','hello'
__requires__ = 'Quinterac==0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Quinterac==0.1', 'console_scripts', 'hello')()
    )
