#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Tutum API
# Copyright (c) 2008-2024 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2024 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier

from . import base


class TututmApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(self, name="tutum", *args, **kwargs)

    @appier.route("/", "GET")
    def index(self):
        return self.services()

    @appier.route("/services", "GET")
    def services(self):
        api = self.get_api()
        services = api.list_services()
        return services

    @appier.route("/services/<str:uuid>", "GET")
    def _service(self, uuid):
        api = self.get_api()
        service = api.get_service(uuid)
        return service

    @appier.route("/nodes", "GET")
    def nodes(self):
        api = self.get_api()
        nodes = api.list_nodes()
        return nodes

    @appier.route("/nodes/<str:uuid>", "GET")
    def node(self, uuid):
        api = self.get_api()
        node = api.get_node(uuid)
        return node

    @appier.route("/nodes/<str:uuid>/check", "GET")
    def check_node(self, uuid):
        api = self.get_api()
        node = api.check_node(uuid)
        return node

    @appier.route("/containers", "GET")
    def containers(self):
        api = self.get_api()
        containers = api.list_containers()
        return containers

    @appier.route("/containers/<str:uuid>", "GET")
    def container(self, uuid):
        api = self.get_api()
        container = api.get_container(uuid)
        return container

    @appier.route("/actions", "GET")
    def actions(self):
        api = self.get_api()
        actions = api.list_actions()
        return actions

    @appier.route("/actions/<str:uuid>", "GET")
    def action(self, uuid):
        api = self.get_api()
        action = api.get_action(uuid)
        return action

    def get_api(self):
        api = base.get_api()
        return api


if __name__ == "__main__":
    app = TututmApp()
    app.serve()
else:
    __path__ = []
