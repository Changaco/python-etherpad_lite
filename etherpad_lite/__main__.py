# This file is part of a program licensed under the terms of the GNU Lesser
# General Public License version 3 (or at your option any later version)
# as published by the Free Software Foundation.
#
# If you have not received a copy of the GNU Lesser General Public License
# along with this file, see <http://www.gnu.org/licenses/>.


from argparse import Action, ArgumentParser, SUPPRESS
import os
import shlex

from . import EtherpadLiteClient, EtherpadException


try:
    input = raw_input
except NameError:
    pass


dict_ = lambda l: dict(a.split('=', 1) for a in l)

class Dict(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, dict_(values))

p = ArgumentParser()
p.add_argument('-a', '--api-version', default=SUPPRESS, type=int)
p.add_argument('-p', '--base-params', default=SUPPRESS, nargs='*', action=Dict, metavar='key=value')
p.add_argument('-t', '--timeout', default=SUPPRESS, type=int)
p.add_argument('-u', '--base-url', default=SUPPRESS)
args = p.parse_args()

c = EtherpadLiteClient(**args.__dict__)

if os.isatty(0):
    import readline
    print('=> Welcome to the Etherpad Lite shell !')
    print('=> Command example: createPad padID=test text="Lorem ipsum dolor sit amet."')

while True:
    try:
        split_line = shlex.split(input('% '))
    except (EOFError, KeyboardInterrupt):
        print()
        exit(0)
    cmd, params = split_line[0], dict_(split_line[1:])
    try:
        print(c(cmd, **params) or 'ok')
    except EtherpadException as e:
        print(e)
