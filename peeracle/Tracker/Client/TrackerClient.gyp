#
# Copyright (c) 2015 peeracle contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

{
  'includes': [
    '../../../build/common.gypi'
  ],
  'conditions': [
    ['OS!="android" and OS!="ios"', {
      'targets': [
        {
          'target_name': 'peeracle_websockets_client',
          'type': 'static_library',
          'standalone_static_library': 1,
          'dependencies': [
            '<(webrtc_depth)/third_party/boringssl/boringssl.gyp:boringssl',
            '<(DEPTH)/third_party/libwebsockets/libwebsockets.gyp:*',
          ],
          'sources': [
            'WebSocketsClient.cc',
            'WebSocketsClient.h',
            'WebSocketsClientInterface.h',
            'WebSocketsClientObserver.h',
          ],
        },
        {
          'target_name': 'peeracle_websockets_client_unittest',
          'type': 'executable',
          'dependencies': [
            'peeracle_websockets_client',
            '<(DEPTH)/test/test.gyp:peeracle_tests_utils',
          ],
          'sources': [
            'WebSocketsClient_unittest.cc',
          ],
        },
      ],
    }],
  ],
  'targets': [
    {
      'target_name': 'peeracle_tracker_client',
      'type': 'static_library',
      'standalone_static_library': 1,
      'conditions': [
        ['OS!="android" and OS!="ios"', {
          'dependencies': [
            'peeracle_websockets_client',
          ],
        }],
      ],
      'dependencies': [
        '../Message/TrackerMessage.gyp:peeracle_tracker_message',
      ],
      'sources': [
        #'TrackerClient.cc',
        #'TrackerClient.h',
        #'TrackerClientInterface.h',
        #'TrackerClientObserver.h',
      ],
    },
    {
      'target_name': 'peeracle_tracker_client_unittest',
      'type': 'executable',
      'dependencies': [
        'peeracle_tracker_client',
        '<(DEPTH)/test/test.gyp:peeracle_tests_utils',
      ],
      'sources': [
        'TrackerClient_unittest.cc',
      ],
    },
  ],
}
