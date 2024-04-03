#!/usr/bin/python3
import string
_ = __import__('os').write(1, bytes(getattr(string, 'ascii_uppercase'), 'utf-8') + b'\n')
