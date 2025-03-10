import os
import sys
import subprocess
import pkg_resources

def main():
    ihack = pkg_resources.resource_filename('instahack', 'ihack')
    if not os.access(ihack, os.X_OK): os.chmod(ihack, 0o755)
    sys.exit(subprocess.call([ihack] + sys.argv[1:]))

if __name__ == '__main__':
    main()