#!/usr/bin/env python2

import os
import sys
import platform

from os.path import isfile, isdir, join

DRAKAR_PATH = os.environ.get('DRAKAR', '/mnt/drakar')
if not isdir(DRAKAR_PATH):
    raise OSError("No such directory: '{}'".format(DRAKAR_PATH))

SYSTEM = sys.platform + '-' + platform.machine()

sources = {
    'processing': {
        'linux2-x86_64': {
            'filename': 'processing-2.1-linux64.tgz', 
            'url': 'http://download.processing.org/processing-2.1-linux64.tgz',
            }
        }
    }


def get_archive(cutename):
    
    filename = sources[cutename][SYSTEM]['filename']
    # => filename-linux64.foo
    
    archives_path = join(DRAKAR_PATH, 'archives', SYSTEM)
    # => /mnt/drakar/archives/linux2-x86_64
    
    file_path = join(archives_path, filename)
    # => /mnt/drakar/archives/linux2-x86_64/filename-linux64.foo
    
    if not isfile(file_path):
        here = os.getcwd()
        source = sources[cutename][SYSTEM][url]
        
        os.makedirs(archives_path)
        os.chdir(archives_path)
        os.system('wget ' + source)
        os.chdir(here)
    
    if isfile(file_path):
        print(file_path)
        return file_path
    else:
        raise IOError("Could not obtain '{}' in Drakar".format(filename))

if __name__ == '__main__':
    for source in sources:
        answer = raw_input('Install {} ? [y/N] '.format(source))
        if answer in ('y', 'Y'):
            get_archive(source)
        
