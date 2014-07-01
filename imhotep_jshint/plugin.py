from imhotep.tools import Tool
import os
import re

class JSHint(Tool):
    response_format = re.compile(r'^(?P<filename>.*): ' \
        r'line (?P<line_number>\d+), col \d+, (?P<message>.*)$')
    jshintrc_filename = '.jshintrc'

    def process_line(self, dirname, line):
        "myapp.js: line 27, col 14, you messed up"
        line = line[len(dirname) + 1:]  # +1 for trailing slash to make relative
        match = self.response_format.search(line)
        if match is not None:
            return match.groups()

    def get_file_extensions(self):
        return ['.js']

    def get_command(self, dirname, **kwargs):
        cmd = "jshint "
        config_path = os.path.join(dirname, self.jshintrc_filename)
        if os.path.exists(config_path):
            cmd += "--config=%s" % config_path
        return cmd
