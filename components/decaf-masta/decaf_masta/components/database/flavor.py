##
# Copyright 2016 DECaF Project Group, University of Paderborn
# This file is part of the decaf orchestration framework
# All Rights Reserved.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
##

__author__ = 'Kristian Hinnenthal'
__date__ = '$13-okt-2015 14:15:27$'
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .mastadatabase import Base
from .datacenter import Datacenter

class Flavor(Base):
    __tablename__ = 'flavors'
    flavor_id = Column(String(250), primary_key=True)
    datacenter_id = Column(Integer, ForeignKey('datacenters.datacenter_id'), nullable=False)
    flavor_os_id = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)