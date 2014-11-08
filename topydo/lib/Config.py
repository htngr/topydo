# Topydo - A todo.txt client written in Python.
# Copyright (C) 2014 Bram Schoenmakers <me@bramschoenmakers.nl>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

import ConfigParser

class ConfigError(Exception):
    def __init__(self, p_text):
        self.text = p_text

    def __str__(self):
        return self.text

class _Config:
    def __init__(self, p_path=None):
        self.sections = ['topydo', 'tags', 'sort', 'ls']

        self.defaults = {
            # topydo
            'default_command': 'ls',
            'colors': '1',
            'highlight_projects_contexts': '1',
            'filename' : 'todo.txt',
            'archive_filename' : 'done.txt',

            # ls
            'list_limit': '-1',

            # tags
            'tag_start': 't',
            'tag_due': 'due',
            'tag_star': 'star',

            # sort
            'sort_string': 'desc:importance,due,desc:priority',
            'ignore_weekends': '1',
        }

        self.cp = ConfigParser.SafeConfigParser(self.defaults)

        files = ["/etc/topydo.conf", self._home_config_path(), ".topydo", "topydo.conf"]
        if p_path != None:
            files.append(p_path)

        self.cp.read(files)

        self._supplement_sections()

    def _supplement_sections(self):
        for section in self.sections:
            if not self.cp.has_section(section):
                self.cp.add_section(section)

    def _home_config_path(self):
        return os.path.join(os.getenv('HOME'), '.topydo')

    def default_command(self):
        return self.cp.get('topydo', 'default_command')

    def colors(self):
        try:
            return self.cp.getboolean('topydo', 'colors')
        except ValueError:
            return self.defaults['colors'] == '1'

    def highlight_projects_contexts(self):
        try:
            return self.cp.getboolean('topydo', 'highlight_projects_contexts')
        except ValueError:
            return self.defaults['highlight_projects_contexts'] == '1'

    def todotxt(self):
        return self.cp.get('topydo', 'filename')

    def archive(self):
        return self.cp.get('topydo', 'archive_filename')

    def list_limit(self):
        try:
            return self.cp.getint('ls', 'list_limit')
        except ValueError:
            return int(self.defaults['list_limit'])

    def sort_string(self):
        return self.cp.get('sort', 'sort_string')

    def ignore_weekends(self):
        try:
            return self.cp.getboolean('sort', 'ignore_weekends')
        except ValueError:
            return self.defaults['ignore_weekends'] == '1'

    def tag_due(self):
        return self.cp.get('tags', 'tag_due')

    def tag_start(self):
        return self.cp.get('tags', 'tag_start')

    def tag_star(self):
        return self.cp.get('tags', 'tag_star')

def config(p_path=None):
    """
    Retrieve the config instance.
    If a path is given, the instance is overwritten by the one that supplies an
    additional filename (for testability).
    """
    if not config.instance or p_path != None:
        try:
            config.instance = _Config(p_path)
        except ConfigParser.ParsingError as e:
            raise ConfigError(str(e))

    return config.instance

config.instance = None