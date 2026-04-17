# tactical_hud/backend_analytics/__init__.py

"""
Aurum-9 HUD Package: Backend Analytics
Handles the data ingestion and entropy-based behavioral analysis before 
passing threat metrics to the 3D frontend.
"""

from .behavior_entropy import EntropyAnalyzer

__all__ = ["EntropyAnalyzer"]
