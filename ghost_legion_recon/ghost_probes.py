import os
import time
import platform
import psutil
from core_ironclad import ExplainableAILogger

class GhostProbe:
    """
    Recon Module: Ephemeral Ghost Probes
    Self-destructing scripts deployed to map the network edge and 
    report health metrics back to the C2 core.
    """

    def __init__(self, probe_id=None):
        self.probe_id = probe_id or f"probe-{os.getpid()}"
        self.logger = ExplainableAILogger("GHOST_LEGION_PROBE")

    def audit_environment(self):
        """Gathers system and network metadata."""
        print(f"[*] PROBE {self.probe_id}: Initiating stealth audit...")
        
        metrics = {
            "os": platform.system(),
            "cpu_usage": psutil.cpu_percent(),
            "active_connections": len(psutil.net_connections()),
            "timestamp": time.time()
        }
        
        # In a real scenario, this would be encrypted and sent to the C2 API
        print(f"[+] PROBE {self.probe_id}: Audit complete. Connections found: {metrics['active_connections']}")
        
        self.logger.log_action(
            action_taken=f"Probe {self.probe_id} completed environment audit",
            trigger_condition="Autonomous recon cycle triggered",
            confidence_score=100.0
        )
        return metrics

    def self_destruct(self):
        """Simulates the probe wiping its presence from the system."""
        print(f"[!] PROBE {self.probe_id}: Mission complete. Initiating self-destruct...")
        
        # Log the exit
        self.logger.log_action(
            action_taken=f"Probe {self.probe_id} self-terminated",
            trigger_condition="End of recon lifecycle",
            confidence_score=100.0
        )
        
        # Simulated 'cleanup' logic
        time.sleep(0.5)
        print("[X] PROBE DATA WIPED FROM MEMORY. EXITING.")
        # In a standalone script, os.remove(__file__) could be used to delete the script itself.

if __name__ == "__main__":
    probe = GhostProbe()
    probe.audit_environment()
    probe.self_destruct()
