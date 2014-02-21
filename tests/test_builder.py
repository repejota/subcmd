#
## BEGIN LICENSE BLOCK
#
# Copyright (c) <2012-2014>, Raul Perez <repejota@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the <organization> nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
## END LICENSE BLOCK
#

import context
import unittest

from subcmd.app import App


class BuilderTestSuite(unittest.TestCase):
    """Builder test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True

    def test_instanciate_app(self):
        app = App()
        # Once instanciated is not None
        self.assertIsNotNone(app)

    def test_instanciate_app_properties(self):
        app = App()
        # We got a default name
        self.assertIsNotNone(app.name)
        # Default name is __class__.__name__
        self.assertEquals("App", app.name)
        # We got a default description
        self.assertIsNotNone(app.description)
        # Default description is "__class__.__name__ description"
        self.assertEquals("App's description", app.description)
        # We got a default epilog
        self.assertIsNotNone(app.epilog)
        # Default epilog is "__class__.__name__ epilog"
        self.assertEquals("App's epilog", app.epilog)
        # We got a default version
        self.assertIsNotNone(app.version)
        # Default version is 0
        self.assertEquals(0, app.version)

    def test_instanciate_app_constructor(self):
        app = App(name="AppName",
                  description="Description",
                  epilog="Epilog",
                  version=2.5)
        # We got a default name
        self.assertIsNotNone(app.name)
        # Default name is initialized
        self.assertEquals("AppName", app.name)
        # We got a default description
        self.assertIsNotNone(app.description)
        # Default description is initialized
        self.assertEquals("Description", app.description)
        # We got a default epilog
        self.assertIsNotNone(app.epilog)
        # Default epilog is initialized
        self.assertEquals("Epilog", app.epilog)
        # We got a default version
        self.assertIsNotNone(app.version)
        # Default version is 2.5
        self.assertEquals(2.5, app.version)


if __name__ == '__main__':
    unittest.main()
