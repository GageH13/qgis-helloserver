# -*- coding: utf-8 -*-
"""
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
  from HelloServer import HelloServer
  return HelloServer(iface)

