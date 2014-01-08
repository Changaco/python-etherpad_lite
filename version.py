# This program is placed into the public domain.

__all__ = ('get_version')

from os.path import dirname, isdir, join
import re
from subprocess import Popen, PIPE

version_re = re.compile('^Version: (.+)$', re.M)

def get_version():
    d = dirname(__file__)

    if isdir(join(d, '.git')):
        # Get the version using "git describe".
        cmd = 'git describe --tags --match [0-9]*'.split()
        try:
            proc = Popen(cmd, stdout=PIPE)
            version = proc.communicate()[0].decode().strip()
            if proc.returncode != 0:
                raise OSError()
        except OSError:
            print('Unable to get version number from git tags')
            exit(1)

        # PEP 386 compatibility
        if '-' in version:
            version = '.post'.join(version.split('-')[:2])

    else:
        # Extract the version from the PKG-INFO file.
        with open(join(d, 'PKG-INFO')) as f:
            version = version_re.search(f.read()).group(1)

    return version


if __name__ == '__main__':
    print(get_version())
