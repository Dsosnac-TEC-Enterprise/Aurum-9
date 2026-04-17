import math
import collections
from core_ironclad import ExplainableAILogger

class EntropyAnalyzer:
    """
    HUD Module: Entropy-Based Behavior Analysis
    Monitors the 'vibe' of data flow. High-entropy deviations trigger alerts.
    """

    def __init__(self):
        self.logger = ExplainableAILogger("HUD_ENTROPY_ANALYZER")

    def calculate_entropy(self, data_packet):
        """
        Calculates the Shannon Entropy of a data string.
        Higher entropy = more randomness (potential encrypted exfiltration).
        """
        if not data_packet:
            return 0
        
        # Count frequency of each character
        frequencies = collections.Counter(data_packet)
        length = len(data_packet)
        
        # Shannon Entropy Formula
        entropy = -sum((count / length) * math.log2(count / length) for count in frequencies.values())
        return entropy

    def analyze_flow(self, source_ip, data_stream):
        """Analyzes a stream and flags it if it exceeds the chaos threshold."""
        entropy_score = self.calculate_entropy(data_stream)
        threshold = 4.5  # Example threshold for structured data
        
        print(f"[*] HUD: Analyzing flow from {source_ip} | Entropy: {entropy_score:.2f}")

        if entropy_score > threshold:
            print(f"[!] ALERT: High-entropy flow detected on {source_ip}! Possible encrypted tunnel.")
            self.logger.log_action(
                action_taken=f"Flagged {source_ip} for HUD Visualization",
                trigger_condition=f"Entropy score {entropy_score:.2f} exceeded threshold {threshold}",
                confidence_score=89.0
            )
            return "CRITICAL"
        return "NORMAL"

# --- Testing Block ---
if __name__ == "__main__":
    analyzer = EntropyAnalyzer()
    # Normal looking data
    analyzer.analyze_flow("10.0.0.5", "user_login,timestamp,status=success")
    # Highly random/encrypted looking data
    analyzer.analyze_flow("10.0.0.99", "af83h9283u4h9f823h9f82h39f8h239f8h23f")
