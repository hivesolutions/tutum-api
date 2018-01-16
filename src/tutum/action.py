#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Tutum API
# Copyright (c) 2008-2018 Hive Solutions Lda.
#
# This file is part of Hive Tutum API.
#
# Hive Tutum API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Tutum API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Tutum API. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2018 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

class ActionAPI(object):

    def list_actions(self):
        url = self.base_url + "action/"
        contents = self.get(url)
        actions = contents["objects"]
        return actions

    def get_action(self, uuid):
        url = self.base_url + "action/%s/" % uuid
        contents = self.get(url)
        return contents
