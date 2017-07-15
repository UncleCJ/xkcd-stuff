#!/usr/bin/env python
"""replace_textnodes (-y | --node-values) <yaml file with mappings id: string> (-x | --xml-file) <xml file to be modified>

Outputs the modified XML to stdout.
"""

import sys
from yaml import safe_load
from xml.etree.ElementTree import parse
from getopt import gnu_getopt
from getopt import GetoptError

def replace_nodes(node_values, xml_file):
    y = safe_load(file(node_values, 'r'))
    x = parse(file(xml_file, 'r'))

    for e in x.getiterator():
        if ('id' in e.attrib) and (e.attrib['id'] in y):
            e.text = y[e.attrib['id']]

    x.write(sys.stdout, 'utf-8')

def usage(output=sys.stdout):
    print >>output, 'Usage:'
    print >>output, __doc__

def main(argv=None):
    if argv is None:
        argv = sys.argv

    xml_file = None
    node_values = None

    try:
        opts, args = gnu_getopt(argv[1:], "hy:x:", ["help", "node-values=", "xml-file="])
        if len(args) > 0:
            raise GetoptError('Illegal parameter supplied.')
        for (k, v) in opts:
            if k in ('-y', '--node-values'):
                node_values = v
            elif k in ('-x', '--xml-file'):
                xml_file = v
            elif k in ('-h', '--help'):
                usage()
                sys.exit(0)
        if xml_file is None:
            raise GetoptError('No xml file supplied.')
        if node_values is None:
            raise GetoptError('No node values file supplied.')

    except GetoptError, err:
        print >>sys.stderr, str(err) + '\n'
        usage(sys.stderr)
        sys.exit(2)

    replace_nodes(node_values, xml_file)

if __name__ == '__main__':
    main()
