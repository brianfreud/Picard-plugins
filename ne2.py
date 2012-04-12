PLUGIN_NAME = '$ne2'
PLUGIN_AUTHOR = 'Brian Schweitzer'
PLUGIN_DESCRIPTION = 'Adds an $ne2 function'
PLUGIN_VERSION = "0.2"
PLUGIN_API_VERSIONS = ["0.12", "0.13", "0.14", "0.15", "0.16"]

from picard.script import register_script_function

def func_ne2(parser, x, *args):
    for i in (i for i in args if i == x):
        return ""
    return "1"

register_script_function(func_ne2, "ne2")



