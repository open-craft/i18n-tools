#!/usr/bin/env python
"""
Utility for cleaning up your local directory after switching between
branches with different translation levels (eg master branch, with only
reviewed translations, versus dev branch, with all translations)
"""
from __future__ import print_function
import os

from i18n import config, Runner
from i18n.execute import execute


def clean_conf_folder(locale):
    """Remove the configuration directory for `locale`"""
    dirname = config.CONFIGURATION.get_messages_dir(locale)
    command = "rm -rf {}".format(dirname)
    print(command)
    try:
        execute(command)
    except Exception as exc:
        print("Encountered error {}; continuing...".format(exc))
        return


def clean_configuration_directory():
    """
    Remove the configuration directories for all locales
    in CONFIGURATION.translated_locales
    """
    for locale in config.CONFIGURATION.translated_locales:
        clean_conf_folder(locale)

class BranchCleanup(Runner):
    def run(self, args):
        clean_configuration_directory()

main = BranchCleanup()

if __name__ == '__main__':
    main()
