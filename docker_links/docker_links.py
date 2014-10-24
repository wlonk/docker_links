# -*- coding: utf-8 -*-
import os
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse


def docker_link(env_variable, overrides=None):
    if overrides is None:
        overrides = {}
    url = urlparse(os.environ.get(env_variable, ''))
    # Do overrides here.
