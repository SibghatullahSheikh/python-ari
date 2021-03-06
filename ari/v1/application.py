# -*- coding: utf-8 -*-
# Copyright (c) 2013 PolyBeacon, Inc.

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from ari.common import base


class Application(base.Resource):
    def __repr__(self):
        return '<Application %s>' % self._info


class ApplicationManager(base.Manager):

    resource_class = Application

    @staticmethod
    def _path(id=None):
        return '/applications/%s' % id if id else '/applications'

    def get(self, application_name):
        try:
            return self._list(self._path(application_name))[0]
        except IndexError:
            return None

    def list(self):
        return self._list(self._path())
