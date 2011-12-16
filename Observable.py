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
import pickle
import logging

class Event(object):
    pass

class Observable(object):
    def __init__(self):
        self.serializedObject = []
        self.functionName = []
    def subscribe(self, functionName, subscriberObject = False):
      self.serializedObject.append(pickle.dumps(subscriberObject))
      self.functionName.append(functionName)
      logging.info('Subscribed')
    def fire(self, **attrs):
        e = Event()
        e.obj = self
        for k, v in attrs.iteritems():
            setattr(e, k, v)
        for i in range(len(self.functionName)):
            logging.info ('Cycle %d', i)
            if self.serializedObject != False:
              subscriberObject = pickle.loads(str(self.serializedObject[i]))
              functionName = self.functionName[i]
              eval("subscriberObject." + functionName + "(e)")
            else: eval(functionName + "(e)")