import re


class ConfigReplacer(object):
    def __init__(self, fname):
        if not fname:
            raise ValueError('File name parameter is not set')
        self.fname = fname
        self.deps_url_re = re.compile(r'(#)(.*)(",?)')
        self.skip_deps = ['', '<DEFAULT>', ]
        self.config = ''

    def configure(self, deps_url=None, skip_deps=None):
        if deps_url is not None:
            self.deps_url_re = re.compile(deps_url)
        if skip_deps is not None:
            self.skip_deps = skip_deps

    def replace_fn(self, s, name, value):
        return self.deps_url_re.sub(value, s) if name in s else s

    def replace(self, name, value):
        configfile = open(self.fname)
        replace_name = '"{}"'.format(name)
        replace_value = '\g<1>{}\g<3>'.format(value)
        self.config = "".join(self.replace_fn(s, replace_name, replace_value) for s in configfile)

    def get_config(self):
        return self.config

    def write(self):
        configfile = open(self.fname, 'w')
        configfile.write(self.config)

    def process(self, name, value):
        self.replace(name, value)
        self.write()

    def __str__(self):
        return '<ConfigReplacer "{}">'.format(self.fname)
