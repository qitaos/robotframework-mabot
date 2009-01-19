#  Copyright 2008 Nokia Siemens Networks Oyj
#  
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#  
#      http://www.apache.org/licenses/LICENSE-2.0
#  
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


try:
    from robot.running import TestSuite
    from robot.conf import RobotSettings
except ImportError, error:
    print """All needed Robot modules could not be imported. 
Check your Robot installation."""
    print "Error was: %s" % (error[0])
    sys.exit(1)

import logger


def load_data(source, settings):
    robot_settings = RobotSettings()
    robot_settings['Include'] = settings['include']
    robot_settings['Exclude'] = settings['exclude']
    return TestSuite([source], robot_settings, logger.LOGGER)
    