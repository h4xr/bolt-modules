'''
File: structures.py
Description: Structures related to the Yum module
Author: Saurabh Badhwar <sbadhwar@redhat.com>
Date: 27/10/2017
'''

class Message(object):
    """Message structure for the yum module"""

    structure = {
        'plugin_name': 'Yum',
        'command': 'yum',
        'override': 'yes',
        'subcommand': '',
        'packages': ''
    }

    def __init__(self):
        """Initialize the Message Object"""

        self.plugin_name = 'Yum'
