#!/usr/bin/env python
#
# Title: observer pattern implementation for App Engine
# Author: Domenico Pontari
# Email: fairsayan@gmail.com
# Website: http://it.linkedin.com/in/pontari/
#
# Rif about observer design pattern: http://it.wikipedia.org/wiki/Observer_pattern
# Basic idea: http://stackoverflow.com/questions/1904351/python-observer-pattern-examples-tips?answertab=votes#tab-top
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
#
import logging
import Called

class Caller():
  def resume(self, event):
    logging.info ('Resumed caller...')

  def __init__(self):
    called = Called.Called()
    called.subscribe('resume', __name__, self)
    logging.info ('Running called object method...')
    called.run()

