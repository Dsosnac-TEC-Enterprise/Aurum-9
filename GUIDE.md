# 📖 Aurum-9 Operator's Manual

## 🛡️ C3MRS Operational Protocols

### 1. Kinetic Strike Execution
When the AI detects a high-confidence threat, it triggers **Sub-Second Micro-Segmentation**. 
* **Quarantine:** The asset is isolated via `iptables` or SDN API.
* **Investigation Pipe:** A controlled port (9999) remains open for forensic analysis. In terminal to perform forensics analysis for suspected IP address run `python3 -m c2_kinetic_engine.forensic_triage`

### 2. The Shadow-Clone Protocol
Instead of blocking an attacker, use `ShadowClonePivot` to reroute traffic.
* **Tactic:** The attacker interacts with a disposable container.
* **Goal:** Record 0-day methodologies without risking production data. To use ShadowClonePivot run `python3 -m c2_kinetic_engine.shadow_clone` in terminal.

### 3. The Nuclear Option (Dead Man's Switch)
In the event of a catastrophic breach:
1. Run `python -m c2_kinetic_engine.dead_man_switch`.
2. Provide your biometric hash signature.
3. The system will hard-sever all WAN interfaces and lock immutable backups.

---

## 🏢 Enterprise Deployment (AWS, Azure, K8s)

Aurum-9 is engineered for cloud-native environments. Follow these protocols for enterprise-grade deployment.

### 1. Containerization (Docker)
The framework is fully containerized to ensure an "Iron-Clad" runtime regardless of the host OS.

**Build the image:**
```bash
docker build -t aurum9-commander:v1.0
```
**Run the secure container:**
```bash
docker run -d -p 8443:8443 -p 9999:9999 --name aurum9 aurum9-commander:v1.0
```
**Orchestration (Kubernetes):**

For high-availability (HA) environments like AWS EKS or Azure AKS, use the provided Kubernetes manifest to deploy a self-healing cluster.

**Apply the deployment:**
```bash
kubectl apply -f k8s-deployment.yaml
```

**Security & Encryption**

All enterprise traffic is hardened via TLS 1.3.
HUD Access: Always use https:// on Port 8443.

Certificate Management: Replace the default cert.pem with your organization's CA-signed certificates for production use.

**Cloud Monitoring**

The LoadBalancer service in the K8s manifest will provide a public entry point.

Ensure your Cloud Security Groups (AWS) or Network Security Groups (Azure) only allow authorized IPs to access the Tactical HUD.




