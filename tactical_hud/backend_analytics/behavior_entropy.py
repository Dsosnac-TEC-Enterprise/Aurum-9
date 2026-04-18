import math
import collections
from core_ironclad import ExplainableAILogger

class EntropyAnalyzer:
    """
    HUD Module: Machine Learning Behavior Analysis (Z-Score Anomaly Detection)
    Learns the baseline 'vibe' of network traffic and dynamically flags 
    statistical anomalies without relying on static thresholds.
    """

    def __init__(self):
        self.logger = ExplainableAILogger("HUD_ML_ENTROPY")
        self.history = []  # Stores historical entropy scores to learn from
        self.learning_period = 10  # Needs 10 packets to establish a baseline

    def calculate_entropy(self, data_packet):
        """Calculates the Shannon Entropy of a string."""
        if not data_packet: return 0
        frequencies = collections.Counter(data_packet)
        length = len(data_packet)
        return -sum((count / length) * math.log2(count / length) for count in frequencies.values())

    def analyze_flow(self, source_ip, data_stream):
        """Analyzes flow using dynamic statistical Machine Learning."""
        current_score = self.calculate_entropy(data_stream)
        
        # 1. Add to history to keep learning (Rolling window of 50 packets)
        self.history.append(current_score)
        if len(self.history) > 50:
            self.history.pop(0)

        # 2. Check if the model is still training
        if len(self.history) < self.learning_period:
            print(f"[*] ML Engine Training on {source_ip}... ({len(self.history)}/{self.learning_period} samples)")
            return "LEARNING"

        # 3. Calculate baseline metrics
        mean = sum(self.history) / len(self.history)
        variance = sum((x - mean) ** 2 for x in self.history) / len(self.history)
        std_dev = math.sqrt(variance) if variance > 0 else 0.001

        # 4. Calculate Z-Score (How many standard deviations away from normal is this?)
        z_score = abs(current_score - mean) / std_dev

        print(f"[*] HUD ML Analysis | IP: {source_ip} | Entropy: {current_score:.2f} | Z-Score: {z_score:.2f}")

        # 5. Anomaly Threshold: If Z-Score is greater than 2.5, it's highly anomalous
        if z_score > 2.5:
            print(f"[!] ML ALERT: Dynamic anomaly detected on {source_ip}! Data flow violates learned baseline.")
            self.logger.log_action(
                action_taken=f"Flagged {source_ip} for HUD Visualization",
                trigger_condition=f"ML Z-Score {z_score:.2f} exceeded dynamic threshold",
                confidence_score=92.5
            )
            return "CRITICAL"
            
        return "NORMAL"

# --- Testing Block ---
if __name__ == "__main__":
    analyzer = EntropyAnalyzer()
    
    # Simulate normal traffic to train the ML model
    print("--- TRAINING PHASE ---")
    for _ in range(10):
        analyzer.analyze_flow("10.0.0.5", "user_login,status=success,timestamp=12345")
    
    # Simulate an encrypted data exfiltration attack
    print("\n--- ATTACK PHASE ---")
    analyzer.analyze_flow("10.0.0.99", "a8f3h9283u4h9f823h9f82h39f8h239f8h23fa8f3h")
