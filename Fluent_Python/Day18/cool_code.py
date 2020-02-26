print("\033c")

print("\t\033[35;1;6;4;5mBest Tuesday Ever!\033[0m\n")

from dis import dis
import opcode

from operator import mul
from functools import partial

def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


from functools import partial
picture = partial(tag, 'img', cls='pic-frame')

import pdb; pdb.set_trace()




