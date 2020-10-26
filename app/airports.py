# Copyright 2017 Google Inc. All Rights Reserved.
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

# Airport data provided by David Megginson (http://ourairports.com/data/).

import io
import math
import array
import csv
import io

class Airports(object):
    print("Test")

    def __init__(self):
        with open('third_party/airports.csv', 'r') as f:
            self.airport_file = io.StringIO(f.read())
            self.airport_reader = csv.DictReader(self.airport_file)

    def get_airport_by_iata(self, iata_code):
        if iata_code.isdigit():
            size = int(iata_code)
        else:
            return("Not valid number.")
        table = [[2.4,1.05,2.5],[0.38,3.0,1.12],[2.5,0.35,3.6],[1.20,2.5,0.32]]
        effort = None
        time = None
        staff = None
        model = None
        newSize = int(size)
        if newSize >= 2 and size <=50:
            model=0 
        
        elif newSize > 50 and size <= 300:
            model=1
        
        elif newSize > 300:
            model=2
        
        effort = table[0][model]*pow(newSize,table[1][model])
        time = table[2][model]*pow(effort,table[3][model]) 
        staff = math.ceil(effort/time)
        return ('The number of staff needed to complete your project is... %d' % staff)
