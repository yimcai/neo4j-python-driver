#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright (c) 2002-2019 "Neo4j,"
# Neo4j Sweden AB [http://neo4j.com]
#
# This file is part of Neo4j.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# tag::config-max-retry-time-import[]
from neo4j import GraphDatabase
# end::config-max-retry-time-import[]


class ConfigMaxRetryTimeExample:
    # tag::config-max-retry-time[]
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password), max_retry_time=15)
    # end::config-max-retry-time[]

    def close(self):
        self._driver.close()

    def can_connect(self):
        result = self._driver.session().run("RETURN 1")
        return result.single()[0] == 1
