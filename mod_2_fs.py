#!/usr/bin/env python
import sys


class BadArguments(Exception):
    pass


def parse_module_path(module_path, ext=None):
    """
    :param module_path: the python path to the module
    :param ext: Optional extension for the file, defaults to py

    >> parse_module_path(citadel.analytics.report)
    citadel/analytics/report.py
    """
    ext = ext or 'py'
    file_name = "/".join(module_path.split('.'))
    return '%s.%s' % (file_name, ext)


if __name__ == "__main__":
    try:
        module_path = sys.argv[1]
    except IndexError:
        raise BadArguments('plox pass a module')
    try:
        ext = sys.argv[2].strip()
    except:
        ext = None

    sys.stdout.write(parse_module_path(module_path, ext))
