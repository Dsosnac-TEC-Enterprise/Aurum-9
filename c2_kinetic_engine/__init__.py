# c2_kinetic_engine/__init__.py

"""
Aurum-9 C2 Package: The Kinetic Strike Engine
This package handles all autonomous, sub-second defensive actions and 
network infrastructure reconfigurations.
"""

from .micro_segmentation import KineticMicroSegmentation
from .shadow_clone import ShadowClonePivot
from .dead_man_switch import DeadManSwitch

__all__ = [
    "KineticMicroSegmentation", 
    "ShadowClonePivot", 
    "DeadManSwitch"
]
