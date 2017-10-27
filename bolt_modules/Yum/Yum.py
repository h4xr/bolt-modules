'''
File: Yum.py
Description: Yum module for package management
Author: Saurabh Badhwar <sbadhwar@redhat.com>
Date: 27/10/2017
'''
import subcommand

class Yum(object):
    """Yum package management module

    Manages the system level packages by issuing the commands such as update,
    install, remove, etc.
    """

    def __init__(self):
        """Initialize the Yum module"""

        self.errors = []

    def handle_payload(self, payload):
        """Handle the incoming payload

        Raises:
            RuntimeError

        Keyword arguments:
        payload -- The payload to be handled
        """

        if payload['plugin_name'] != 'Yum':
            raise RuntimeError("Invalid payload")

        executable_command = self.__parse_payload(payload)

    def execute_command(self, command):
        """Execute the command

        Keyword arguments:
        command -- The command to be executed

        Returns:
            Integer
        """

        result = subprocess.check_output([command], shell=True)
        return result

    def __parse_payload(self, payload):
        """Parse the payload to generate a valid command

        Keyword arguments:
        payload -- The validated payload

        Returns:
            String
        """

        executable = ''

        command = payload['command']
        subcommand = payload['subcommand']
        override = payload['override']
        packages = payload['packages']

        if self.__validate_command(command):
            executable = command

        if self.__validate_subcommand(subcommand):
            executable = executable + ' ' + subcommand

        package_list = self.__get_package_list(packages)
        if package_list != None:
            executable = executable + ' ' + package_list

        if override == True:
            executable = executable + ' ' + '-y'

        return executable


    def __validate_command(self, command):
        """Validate the command

        Keyword arguments:
        command -- The command to be executed

        Returns:
            Boolean
        """

        if command == 'yum':
            return True

        return False

    def __validate_subcommand(self, subcommand):
        """Validate the subcommand

        Keyword arguments:
        subcommand -- The subcommand to be validated

        Returns:
            Boolean
        """

        if subcommand in ['install', 'remove', 'list']:
            return True

        return False

    def __get_package_list(self, packages):
        """Get the package list

        Keyword arguments:
        packages -- The comma seperated list of packages

        Returns:
            String | None
        """

        package_list = ''

        if packages == '' or packages == None:
            return None

        for package in packages.split(','):
            package_list = package_list + package + ' '

        return package_list
