# -*- coding: utf-8 -*-
#
# Copyright: (c) 2018, F5 Networks Inc.
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os
import json
import pytest
import sys

if sys.version_info < (2, 7):
    raise pytest.skip("F5 Ansible modules require Python >= 2.7")

from ansible.module_utils.basic import AnsibleModule

try:
    from library.modules.{{ module }} import ApiParameters
    from library.modules.{{ module }} import ModuleParameters
    from library.modules.{{ module }} import ModuleManager
    from library.modules.{{ module }} import ArgumentSpec

    # In Ansible 2.8, Ansible changed import paths.
    from test.units.compat import unittest
    from test.units.compat.mock import Mock
    from test.units.compat.mock import patch

    from test.units.modules.utils import set_module_args
except ImportError:
    from ansible.modules.network.f5.{{ module }} import ApiParameters
    from ansible.modules.network.f5.{{ module }} import ModuleParameters
    from ansible.modules.network.f5.{{ module }} import ModuleManager
    from ansible.modules.network.f5.{{ module }} import ArgumentSpec

    # Ansible 2.8 imports
    from units.compat import unittest
    from units.compat.mock import Mock
    from units.compat.mock import patch

    from units.modules.utils import set_module_args


fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures')
{% raw %}fixture_data = {}{% endraw %}


def load_fixture(name):
    path = os.path.join(fixture_path, name)

    if path in fixture_data:
        return fixture_data[path]

    with open(path) as f:
        data = f.read()

    try:
        data = json.loads(data)
    except Exception:
        pass

    fixture_data[path] = data
    return data


class TestParameters(unittest.TestCase):
    def test_module_parameters(self):
        raise SkipTest('You must write your own module param test. See examples, then remove this exception')
        # args = dict(
        #     monitor_type='m_of_n',
        #     host='192.168.1.1',
        #     port=8080
        # )
        #
        # p = ModuleParameters(params=args)
        # assert p.monitor == 'min 1 of'
        # assert p.host == '192.168.1.1'
        # assert p.port == 8080

    def test_api_parameters(self):
        raise SkipTest('You must write your own API param test. See examples, then remove this exception')
        # args = dict(
        #     monitor_type='and_list',
        #     slowRampTime=200,
        #     reselectTries=5,
        #     serviceDownAction='drop'
        # )
        #
        # p = ApiParameters(params=args)
        # assert p.slow_ramp_time == 200
        # assert p.reselect_tries == 5
        # assert p.service_down_action == 'drop'


class TestManager(unittest.TestCase):
    def test_create(self, *args):
        raise SkipTest('You must write a creation test')
