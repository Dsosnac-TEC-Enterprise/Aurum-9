import time
import json
import socket
from core_ironclad import ExplainableAILogger

class ForensicInvestigator:
    """
    Operator Tool: Connects to a quarantined asset via the designated 
    Investigation Pipe (Port 9999) to safely pull memory and process logs.
    """
    
    def __init__(self, target_ip):
        self.target_ip = target_ip
        self.port = 9999
        self.logger = ExplainableAILogger("FORENSIC_TRIAGE")

    def simulate_data_extraction(self):
        """Simulates pulling a JSON log file from the isolated machine."""
        print(f"\n[*] Establishing secure encrypted tunnel to {self.target_ip}:{self.port}...")
        time.sleep(1.5) # Simulating connection latency
        print("[+] Connection established. Bypassing network quarantine via authorized port.")
        
        print("[*] Extracting running processes and memory dumps...")
        time.sleep(2)
        
        # This is the mock data we "pulled" from the infected machine
        mock_forensic_data = {
            "infected_process_id": 4092,
            "malware_signature": "Trojan.Linux.Ransom.X",
            "files_encrypted": 142,
            "origin_hacker_ip": "198.51.100.44",
            "system_status": "CRITICAL_BUT_CONTAINED"
        }
        return mock_forensic_data

    def execute_triage(self):
        try:
            data = self.simulate_data_extraction()
            
            print("\n" + "="*40)
            print(" 🚨 FORENSIC TRIAGE REPORT 🚨 ")
            print("="*40)
            for key, value in data.items():
                print(f" >> {key.upper()}: {value}")
            print("="*40)
            
            print(f"\n[+] Data successfully saved to secure vault.")
            print(f"[*] The asset {self.target_ip} is now safe for complete termination/wiping.")
            
            self.logger.log_action(
                action_taken=f"Extracted forensic data via Port {self.port}",
                trigger_condition=f"Operator initiated manual triage on {self.target_ip}",
                confidence_score=100.0
            )
            
        except Exception as e:
            print(f"[-] Triage Failed. The asset may be completely offline. Error: {e}")

# --- Operator CLI ---
if __name__ == "__main__":
    print("--- AURUM-9 FORENSIC TRIAGE TERMINAL ---")
    target = input("Enter the IP address of the quarantined node: ")
    
    investigator = ForensicInvestigator(target)
    investigator.execute_triage()
