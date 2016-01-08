#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Tutum API
# Copyright (c) 2008-2015 Hive Solutions Lda.
#
# This file is part of Hive Tutum API.
#
# Hive Tutum API is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Tutum API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Tutum API. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2015 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import base64

import appier

from . import service

BASE_URL = "https://dashboard.tutum.co/api/v1/"
""" The default base url to be used when no other
base url value is provided to the constructor """

class Api(
    appier.Api,
    service.ServiceApi
):

    def __init__(self, *args, **kwargs):
        appier.Api.__init__(self, *args, **kwargs)
        self.username = appier.conf("TT_USERNAME", None)
        self.password = appier.conf("TT_PASSWORD", None)
        self.base_url = kwargs.get("base_url", BASE_URL)
        self.username = kwargs.get("username", self.username)
        self.password = kwargs.get("password", self.password)

    def build(
        self,
        method,
        url,
        data = None,
        data_j = None,
        data_m = None,
        headers = None,
        params = None,
        mime = None,
        kwargs = None
    ):
        auth = kwargs.pop("auth", True)
        if auth: headers["Authorization"] = self.get_authorization()

    def get_authorization(self):
        if not self.username or not self.password: None
        payload = "%s:%s" % (self.username, self.password)
        payload = appier.legacy.bytes(payload)
        authorization = base64.b64encode(payload)
        authorization = appier.legacy.str(authorization)
        return "Basic %s" % authorization
