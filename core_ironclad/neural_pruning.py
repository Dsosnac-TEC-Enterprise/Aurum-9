import json
import os
from core_ironclad.explainable_ai import ExplainableAILogger

class NeuralPruning:
    """
    Iron-Clad Core Feature 3: Neural Pruning
    Implements a feedback loop to categorize false positives and 
    filter out noise, reducing system alert fatigue.
    """

    def __init__(self, registry_path="core_ironclad/pruning_registry.json"):
        self.registry_path = registry_path
        self.logger = ExplainableAILogger("IRONCLAD_NEURAL_PRUNING")
        self.noise_patterns = self._load_registry()

    def _load_registry(self):
        """Loads the registry of known false-positive patterns."""
        if os.path.exists(self.registry_path):
            with open(self.registry_path, 'r') as f:
                return json.load(f)
        return {"false_positives": []}

    def register_false_positive(self, pattern_signature, reasoning):
        """
        Records a specific event as a false positive to prevent future alerts.
        """
        if pattern_signature not in self.noise_patterns["false_positives"]:
            self.noise_patterns["false_positives"].append({
                "signature": pattern_signature,
                "reasoning": reasoning,
                "count": 1
            })
            print(f"[*] PRUNING: Pattern {pattern_signature} registered as noise.")
        else:
            for item in self.noise_patterns["false_positives"]:
                if item["signature"] == pattern_signature:
                    item["count"] += 1
        
        self._save_registry()
        self.logger.log_action(
            action_taken=f"Pruned Logic Branch: {pattern_signature}",
            trigger_condition="Manual operator feedback / False Positive verification",
            confidence_score=100.0
        )

    def is_noise(self, current_signature):
        """Checks if a current threat signature has been pruned."""
        for item in self.noise_patterns["false_positives"]:
            if item["signature"] == current_signature:
                return True
        return False

    def _save_registry(self):
        with open(self.registry_path, 'w') as f:
            json.dump(self.noise_patterns, f, indent=4)

# --- Testing Block ---
if __name__ == "__main__":
    pruner = NeuralPruning()
    # Simulate a false positive report
    pruner.register_false_positive("UDP_Flood_Internal_Backup_Sync", "Scheduled nightly backup")
    
    # Check if a new alert should be suppressed
    if pruner.is_noise("UDP_Flood_Internal_Backup_Sync"):
        print("[+] Alert suppressed: Known noise pattern detected.")
