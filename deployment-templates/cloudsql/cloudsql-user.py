# Copyright 2017 The Forseti Security Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Creates a Cloud SQL database template for forseti_inventory."""


def GenerateConfig(context):
    """Generate configuration."""

    resources = []

    resources.append({
        'name': context.env['name'],
        'type': 'sqladmin.v1beta4.user',
        'properties': {
            'project': context.env['project'],
            'instance': '$(ref.cloudsql-instance.name)',
            'kind': 'sql#user',
            'name': context.env['name']
        }
    })

    return {'resources': resources}
