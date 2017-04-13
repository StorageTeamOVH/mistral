# Copyright 2017 - Brocade Communications Systems, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from oslo_log import log as logging

from mistral.executors import base as exe
from mistral.executors import default_executor as d_exe
from mistral.executors import remote_executor as r_exe
from mistral.tests.unit.executors import base


LOG = logging.getLogger(__name__)


class PluginTestCase(base.ExecutorTestCase):

    def tearDown(self):
        exe.cleanup()
        super(PluginTestCase, self).tearDown()

    def test_get_local_executor(self):
        executor = exe.get_executor('local')

        self.assertIsInstance(executor, d_exe.DefaultExecutor)

    def test_get_remote_executor(self):
        executor = exe.get_executor('remote')

        self.assertIsInstance(executor, r_exe.RemoteExecutor)
