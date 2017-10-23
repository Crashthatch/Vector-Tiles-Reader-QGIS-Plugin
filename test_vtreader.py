# -*- coding: utf-8 -*-
#
# This code is licensed under the GPL 2.0 license.
#
import pytest
import os
import sys
from qgis.core import *
from qgis.utils import iface
from PyQt4.QtCore import *


def testIfaceisNotNote():
    global iface
    assert iface is not None


# def testMbtilesSourceCreation():
#     path = os.path.join(os.path.dirname(__file__), 'sample_data', 'uster_zh.mbtiles')
#     src = MBTilesSource(path)
#     assert src is not None
#     assert path == src.source()

def run_all():
    pytest.main()


if __name__ == "__main__":
    run_all()
