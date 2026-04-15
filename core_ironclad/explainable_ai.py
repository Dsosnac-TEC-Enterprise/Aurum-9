import logging
from datetime import datetime

# Configure standard logging
logging.basicConfig(
    filename='aurum_logic_receipts.log', 
    level=logging.INFO,
    format='%(asctime)s - XAI-RECEIPT - %(message)s'
)

class ExplainableAILogger:
    """
    Iron-Clad Core Feature 1: Explainable AI (XAI)
    Generates plain-English 'Logic Receipts' for all autonomous actions.
    """
    
    def __init__(self, module_name):
        self.module_name = module_name

    def log_action(self, action_taken, trigger_condition, confidence_score):
        """
        Logs a detailed receipt of why the AI took a specific action.
        
        :param action_taken: The kinetic action executed (e.g., "Isolated IP 192.168.1.5")
        :param trigger_condition: What caused it (e.g., "High entropy in database queries")
        :param confidence_score: AI's certainty percentage (e.g., 98.5)
        """
        receipt = (
            f"Module: [{self.module_name}] | "
            f"Action: {action_taken} | "
            f"Reasoning: {trigger_condition} | "
            f"AI Confidence: {confidence_score}%"
        )
        
        # Log to file
        logging.info(receipt)
        
        # Print to console for our debugging
        print(f"[+] XAI LOG GENERATED: {receipt}")

# Example Usage:
# if __name__ == "__main__":
#     logger = ExplainableAILogger("C2_KINETIC_ENGINE")
#     logger.log_action("Triggered Shadow-Clone Pivot", "Lateral movement detected on port 445", 99.2)
