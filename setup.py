#!/usr/bin/env python

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters import setup

setup(name='telegrams',
      version='1.0',
      description='Python Distribution Utilities',
      author='Greg Ward',
      author_email='gward@python.net',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['distutils', 'distutils.command'],
     )
