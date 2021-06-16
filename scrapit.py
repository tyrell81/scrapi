#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##/usr/bin/env python

# https://python-scripts.com/scrapy-example
#
# python3 -m venv scrapy_env
# source scrapy_env/bin/activate

import logging, os, sys, subprocess, re, datetime


def main(argv):
    # Использование из cli: 
    # sudo ./scrapit.py creationwatches.com

    # set up logging to file
    logging.basicConfig(
        filename='scrapit.log',
        level=logging.DEBUG,   
        # format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
        format='%(name)s - %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )
    # set up logging to console
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)
    # logger
    logger = logging.getLogger(__name__)

    if len(argv) > 0:
        # logging.debug(str(len(sys.argv)) + " argv: " + str(argv), True)
        logging.debug(str(len(sys.argv)) + " argv: " + str(argv))
        for arg in argv:
            print("arg: " + arg)

    else:
        logging.debug("No args")


if __name__ == '__main__':
    main(sys.argv[1:])