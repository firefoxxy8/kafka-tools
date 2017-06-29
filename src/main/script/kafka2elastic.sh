#!/bin/sh

# Copyright KOLIBERO under one or more contributor license agreements.
# KOLIBERO licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

src/main/python/kafka2elastic.py --kafka_bootstrap_srvs=ip-172-31-11-245.eu-west-2.compute.internal:9092 --kafka_source_topic=enriched-good-json-ce


