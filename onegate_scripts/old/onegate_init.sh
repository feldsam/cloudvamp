#!/bin/bash
# -------------------------------------------------------------------------- #
# Copyright 2015, Universitat Politecnica de Valencia                        #
#                                                                            #
# Licensed under the Apache License, Version 2.0 (the "License"); you may    #
# not use this file except in compliance with the License. You may obtain    #
# a copy of the License at                                                   #
#                                                                            #
# http://www.apache.org/licenses/LICENSE-2.0                                 #
#                                                                            #
# Unless required by applicable law or agreed to in writing, software        #
# distributed under the License is distributed on an "AS IS" BASIS,          #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   #
# See the License for the specific language governing permissions and        #
# limitations under the License.                                             #
#--------------------------------------------------------------------------- #

DELAY=5

source /mnt/context.sh 

cp -f /mnt/onegate_publisher.sh /root/onegate_publisher.sh
chmod +x /root/onegate_publisher.sh
cd /root
nohup /root/onegate_publisher.sh $ONEGATE_ENDPOINT/vm/$VMID `cat /mnt/token.txt` $DELAY > /dev/null 2> /dev/null &
