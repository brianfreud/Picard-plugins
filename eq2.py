PLUGIN_NAME = '$eq2'
PLUGIN_AUTHOR = 'Brian Schweitzer'
PLUGIN_DESCRIPTION = 'Adds an $eq2 function'
PLUGIN_VERSION = "0.2.2"
PLUGIN_API_VERSIONS = ["0.12", "0.13", "0.14", "0.15"]

from picard.script import register_script_function

def func_eq2(parser, x, *args):
    for i in (i for i in args if i == x):
        return "1"
    return ''

register_script_function(func_eq2, "eq2")



