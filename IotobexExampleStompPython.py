# IotobexExampleStompPython.py
#
# Example of a Python program to demonstrate a STOMP client interface for Iotobex. This program
# publishes a single message then waits momentarily for reception of that message before terminating.
#
#
# Copyright 2020 Arid Systems Pty Ltd
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#
# Utilizes the Python STOMP client by Jason R Briggs. Has been tested using version
# 5.0.1. Add the stomp.py package to project.

import time
import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('Received an error "%s"' % message)
    def on_message(self, headers, message):
        print('Received a message "%s"' % message)

# Configure the following as per the Credentials and STOMP specifics as detailed
# in the Iotobex Client Console.
url = 'STOMP-URL'   # refer Iotobex Client Console
port = 61613        # confirm - refer Iotobex Client Console
username = 'client-username'    # refer Iotobex Client Console
password = 'client-password'    # refer Iotobex Client Console

# The stream name below must be configured for the user whose credentials are
# entered above. By means of the Iotobex Client Console, configure the stream
# name as both a publishable and subscribed stream. Note that when using the
# Stomp library as per this example, the destination must be specified as the
# topic prefixed by the string '/topic'. So for example, the destination for a
# stream named com.example.sample.topic would be '/topic/com.example.sample.topic'.
sample_stream_name = 'com.example.sample.topic'
message_text = 'Sample message'

print('======= ClientExampleStompPython =======')
conn = stomp.Connection([(url, port)])
conn.set_listener('', MyListener())
print('Connecting to ' + url + ' via port ' + str(port) + ' with username: ' + username + ' and password: ' + password)
conn.connect(username, password, wait=True)
print('Subscribing to stream ' + sample_stream_name)
conn.subscribe(destination='/topic/' + sample_stream_name, id='1', ack='auto')
print('Sending message to stream ' + sample_stream_name + ' - message: ' + message_text)
conn.send(destination='/topic/' + sample_stream_name, body=message_text)
print('Waiting for two seconds')
time.sleep(2)
print('Disconnecting')
conn.disconnect()
print('================= End =================')
