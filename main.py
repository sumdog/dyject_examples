#!/usr/bin/env python
"""
Copyright [2013] [dyject.com]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from dyject import Context

if __name__ == '__main__':

   ctx = Context()
   ctx.load_config('example.config')

   client = ctx.get_class('ClientConfig')
   config = ctx.get_class('ConfigurationHandler')

   print('Client arch is {0}'.format(client.arch))
   print('Configuration Handler config objects: {0}'.format(config.configs))

   other_a = ctx.get_class('OtherConfig',prototype=True)
   other_b = ctx.get_class('OtherConfig',prototype=True)

   if id(other_a) != id(other_b):
     print('Other objects are distinct instances')
