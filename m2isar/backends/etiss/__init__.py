# SPDX-License-Identifier: Apache-2.0

# This file is part of the M2-ISA-R project: https://github.com/tum-ei-eda/M2-ISA-R
#
# Copyright (c) 2022
# Chair of Electrical Design Automation
# Technical University of Munich

from enum import Enum, auto

class BlockEndType(Enum):
	NONE = auto()
	UNCOND = auto()
	ALL = auto()