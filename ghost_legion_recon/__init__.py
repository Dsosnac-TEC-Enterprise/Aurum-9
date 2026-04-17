# ghost_legion_recon/__init__.py

"""
Aurum-9 Reconnaissance Package: The Ghost Legion
Handles ephemeral probes, agentic honeypots, and active deception tactics.
"""

from .ghost_probes import GhostProbe
from .honeypot_manager import HoneypotManager

__all__ = ["GhostProbe", "HoneypotManager"]
