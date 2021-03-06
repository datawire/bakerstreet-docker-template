#!/usr/bin/env python

# Copyright 2015 The Baker Street Authors. All rights reserved.
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

import sys
import threading
import uuid

from flask import Flask, jsonify
app = Flask(__name__)

index = 0
service_id = uuid.uuid4()
version = "1"

def synchronized(func):
    func.__lock__ = threading.Lock()

    def synchronized_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)

    return synchronized_func

@synchronized
def increment_index():
    global index
    index += 1

@app.route("/")
def hello():
    increment_index()
    return jsonify(service_id=str(service_id), index=index, message="Hello, world!", version=version)

@app.route("/health")
def health_check():
    increment_index()
    return jsonify(service_id=str(service_id), index=index, status='OK')

if __name__ == "__main__":
    passed_args = sys.argv
    version = passed_args[2]
    app.run(port=int(passed_args[1]), host="0.0.0.0")
