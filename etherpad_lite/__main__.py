from argparse import Action, ArgumentParser, ArgumentTypeError, SUPPRESS
import os
import shlex

from . import EtherpadLiteClient, EtherpadException


try:
    input = raw_input
except NameError:
    pass


def dict_(l):
    s = [a.split('=', 1) for a in l]
    e = [a[0] for a in s if len(a) == 1]
    if e:
        raise ArgumentTypeError('argument is not of the form "key=value": %s' % e[0])
    return dict(s)


class Dict(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, dict_(values))

p = ArgumentParser()
p.add_argument('-a', '--api-version', default=SUPPRESS)
p.add_argument('-p', '--base-params', default=SUPPRESS, nargs='*', action=Dict, metavar='key=value')
p.add_argument('-t', '--timeout', default=SUPPRESS, type=int)
p.add_argument('-u', '--base-url', default=SUPPRESS)
try:
    args = p.parse_args()
except ArgumentTypeError as e:
    print(e)
    exit(1)

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
    if not split_line:
        continue
    cmd = split_line[0]
    try:
        params = dict_(split_line[1:])
    except ArgumentTypeError as e:
        print(e)
        continue
    try:
        print(c(cmd, **params) or 'ok')
    except EtherpadException as e:
        print(e)
