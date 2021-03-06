# Copyright 2014 Infoblox
#
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

import logging

from designate.backend.impl_infoblox.records import base
from designate.i18n import _LI

LOG = logging.getLogger(__name__)


class SOARecord(base.DNSRecord):
    def create(self, recordset):
        LOG.warning(_LI("Create SOA record not implemented"))
        pass

    def _update_infoblox_record(self, recordset):
        LOG.warning(_LI("Update SOA record not implemented"))
        pass

    def _update_infoblox_recordset(self, recordset):
        LOG.warning(_LI("Update SOA recordset not implemented"))
        pass

    def delete(self, recordset):
        LOG.warning(_LI("Delete SOA record not implemented"))
        pass
