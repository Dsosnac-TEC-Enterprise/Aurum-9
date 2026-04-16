import hashlib
import os
import json
import sys
from core_ironclad.explainable_ai import ExplainableAILogger

class SelfHealingLogic:
    """
    Iron-Clad Core Feature 2: Self-Healing Logic
    Monitors source code hashes against an immutable registry to detect tampering or code drift.
    """

    def __init__(self, target_directory=".", registry_file="core_ironclad/hash_registry.json"):
        self.target_directory = target_directory
        self.registry_file = registry_file
        self.logger = ExplainableAILogger("IRONCLAD_SELF_HEALING")
        self.baseline_hashes = {}

    def _calculate_file_hash(self, filepath):
        """Generates a SHA-256 hash for a given file."""
        sha256_hash = hashlib.sha256()
        try:
            with open(filepath, "rb") as f:
                # Read and update hash string value in blocks of 4K
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except FileNotFoundError:
            return None

    def generate_baseline(self):
        """Scans the directory and saves the initial 'clean' state of the code."""
        print("[*] Generating baseline code hashes...")
        for root, _, files in os.walk(self.target_directory):
            for file in files:
                if file.endswith(".py"): # Only monitor Python scripts
                    filepath = os.path.join(root, file)
                    self.baseline_hashes[filepath] = self._calculate_file_hash(filepath)
        
        # Save the baseline to a JSON file (our immutable registry)
        with open(self.registry_file, 'w') as f:
            json.dump(self.baseline_hashes, f, indent=4)
        
        self.logger.log_action(
            action_taken="Generated Hash Baseline",
            trigger_condition="Initial setup or authorized system update",
            confidence_score=100.0
        )
        print(f"[+] Baseline saved to {self.registry_file}")

    def verify_integrity(self):
        """Compares current file hashes against the saved baseline."""
        print("[*] Verifying system integrity...")
        
        if not os.path.exists(self.registry_file):
            print("[-] No registry found! Run generate_baseline() first.")
            return False

        with open(self.registry_file, 'r') as f:
            saved_hashes = json.load(f)

        tampered_files = []

        for filepath, saved_hash in saved_hashes.items():
            current_hash = self._calculate_file_hash(filepath)
            
            if current_hash is None:
                tampered_files.append((filepath, "FILE MISSING"))
            elif current_hash != saved_hash:
                tampered_files.append((filepath, "HASH MISMATCH (MODIFIED)"))

        if tampered_files:
            for file, issue in tampered_files:
                self.logger.log_action(
                    action_taken=f"CRITICAL: Integrity failure on {file}",
                    trigger_condition=issue,
                    confidence_score=100.0
                )
            self._trigger_kill_switch()
            return False
            
        print("[+] All core files verified. System integrity is 100%.")
        return True

    def _trigger_kill_switch(self):
        """Simulates shutting down the instance to prevent compromised execution."""
        print("\n[!!!] KINETIC RESPONSE TRIGGERED: COMPROMISE DETECTED [!!!]")
        print("[!!!] Initiating self-termination to protect the network...")
        self.logger.log_action("System Halt", "Self-Healing trigger: Unverified code drift", 100.0)
        # In a real production environment, this would tear down the Docker container.
        sys.exit(1)

# --- Execution Block ---
if __name__ == "__main__":
    healer = SelfHealingLogic()
    
    # Check if a registry exists. If not, build it. If it does, verify it.
    if not os.path.exists(healer.registry_file):
        healer.generate_baseline()
    else:
        healer.verify_integrity()
  
