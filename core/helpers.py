import collections
import os

from django.utils import six


def flatten(d, parent_key='', sep='__'):
    items = []
    for key, value in d.iteritems():
        if not isinstance(key, six.string_types):
            raise TypeError("Dictionary keys must be strings")
        new_key = sep.join((parent_key, key)) if parent_key else key
        if isinstance(value, collections.MutableMapping):
            items.extend(flatten(value, parent_key=new_key).items())
        else:
            items.append((new_key, value))
    return dict(items)


def unflatten(d, sep='__'):
    result = {}
    for key, value in d.iteritems():
        keys_chain = key.split(sep)[::-1]
        root = result
        while len(keys_chain) > 1:
            root = root.setdefault(keys_chain.pop(), {})
        root[keys_chain.pop()] = value
    return result


def handle_uploaded_file(f, target_path, target_name):
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    full_path = os.path.join(target_path, target_name)
    with open(full_path, 'w') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
