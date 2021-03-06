#!/usr/bin/env python

import csv

class Conf:
        def __init__(self, conf_dir, conf_file):
                self.conf_dir = conf_dir
                self.conf_file = conf_file
                self.conf_settings = {}
                self._process_conf()

        def _process_conf(self):
                """Open conf file and store conf settings"""
                # TODO - is there a python module for handling conf files that I should be using instead
                with open(self.conf_dir + self.conf_file, 'r') as conf_file:
                        confreader = csv.reader(conf_file, delimiter='=')
                        for row in confreader:
                                if len(row) == 2:
                                        conf_key = str(row[0]).strip()
                                        conf_val = str(row[1]).replace('$CONF_DIR', self.conf_dir).strip()
                                        self.conf_settings[conf_key] = conf_val

        def display_conf_settings(self):
                """Display conf settings"""
                for key, value in self.conf_settings.iteritems():
                        print '"' + key + '" : "' + value + '"'







