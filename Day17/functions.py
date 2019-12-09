print('\033c')

print("\t\033[35;1;6;4;5mMonday Back From Re:invent!\033[0m\n")


# from faker import Faker
from dis import dis
import opcode
from inspect import signature


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


def clip(text, max_len=80):
    """Return text clipped at the last space before or after max_len"""

    end = None

    if len(text) > max_len:
	# What does rfind do?
        space_before = text.rfind(' ', 0, max_len)

        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # no spaces were found
        end = len(text)
    return text[:end].rstrip()


def f(a, *b, c, d=None, **attrs):
    pass







import inspect

sig = inspect.signature(tag)

my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
          'src': 'sunset.jpg', 'cls': 'framed'}
bound_args = sig.bind(**my_tag)

# for name, value in bound_args.arguments.items():
#     print(name, '=', value)




# def cool_func(a:str):
def cool_func(a:"literally whatever I want > 190") -> "HAHAHHAHA":
    print("So Cool")

# cool_func(1)
cool_func("hello")
import pdb; pdb.set_trace()














