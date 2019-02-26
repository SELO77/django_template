from importlib import import_module


main_settings = import_module('core.settings.main')
for attr in dir(main_settings):
    if attr.startswith('__'):
        continue

    locals()[attr] = getattr(main_settings, attr)
