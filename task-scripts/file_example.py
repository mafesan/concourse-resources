#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print('Writing file...')
with open('my_file.txt', 'w') as wfile:
    wfile.write('This is an example from python\r\n')

print('Done.')
