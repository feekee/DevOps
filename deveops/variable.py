# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-6-29
# Author Yo
# Email YoLoveLife@outlook.com

#OPS
OPS_PUSH_MISSION_LACK_OF_KEY_OR_JUMPER = -3
OPS_PUSH_MISSION_UNREACHABLE = -2
OPS_PUSH_MISSION_FAILED = -1
OPS_PUSH_MISSION_WAIT_EXAM = 1
OPS_PUSH_MISSION_WAIT_UPLOAD = 2
OPS_PUSH_MISSION_WAIT_RUN = 3
OPS_PUSH_MISSION_RUNNING = 4
OPS_PUSH_MISSION_SUCCESS = 5
OPS_PUSH_MISSION_IMPORT_VAR = 6
OPS_PUSH_MISSION_IMPORT_TASKS = 7

#HOST
HOST_CLOSE = -2
# 此状态机器将不会参与到所有运维操作中
HOST_PAUSE = -1
HOST_CAN_BE_USE = 1

#GROUP
GROUP_PAUSE = -2
GROUP_UNREACHABLE = -1
GROUP_CAN_BE_USE = 1