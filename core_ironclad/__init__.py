# core_ironclad/__init__.py

"""
Aurum-9 Core Package: Iron-Clad Features
This package contains the foundational security, logging, and integrity 
mechanisms required by all other Aurum-9 modules.
"""

# By importing these here, other files can import them directly from 'core_ironclad'
from .explainable_ai import ExplainableAILogger
from .self_healing import SelfHealingLogic

__all__ = ["ExplainableAILogger", "SelfHealingLogic"]
