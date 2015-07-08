#!/usr/local/bin/python

# This script writes data to the icinga command file icinga.cmd and is intended to test passive checks.

# Import modules.
import argparse
import time

# Define variables.
command_file = '/var/spool/icinga/rw/icinga.cmd'

# Get command line arguments.
parser = argparse.ArgumentParser(description='Write to the icinga command file.')
parser.add_argument('--type', action='store', required=True, choices=['host', 'service'])
parser.add_argument('--target', action='store', required=True)
parser.add_argument('--result', action='store', required=True, choices=['0', '1', '2', '3'])
parser.add_argument('--data', action='store', required=True)
args = parser.parse_args()

# Get the current time in unix seconds as a string.
seconds = str(int(time.time()))

# Format the command.
if args.type == 'host':
	type = 'PROCESS_HOST_CHECK_RESULT'
else:
	type = 'PROCESS_SERVICE_CHECK_RESULT'
command = '[' + seconds + '] ' + type + ';' + args.target + ';' + args.result + ';' + args.data

# Write the data to the icinga command file.
with open(command_file, 'a') as command_file_handle:
	command_file_handle.write(command)
	command_file_handle.close()
