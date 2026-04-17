### Installation & Setup🚀
Deploy the Aurum-9 framework using the automated setup script. This will configure your virtual environment, install dependencies, and launch the Neural Commander.

### Prerequisites
* **Python 3.11+**
* **Git**
* **Docker** (Optional, for Shadow-Clone containerization)

### Quick Start

**Clone the repository:**
   ```bash
   git clone https://github.com/Dsosnac-TEC-Enterprise/Aurum-9.git
   cd Aurum-9
   ```
**Run the deployment script:**

   ```bash
chmod +x setup.sh
./setup.sh
   ```
**Viewing Autonomous XAI feed:**
   ```bash
python3 main.py
   ```
**🖥️ Accessing the Tactical HUD:**

Once the backend is running,navigate to the 3D HUD directory:
   ```bash
cd tactical_hud/frontend_3d
python3 -m http.server 8000
   ```
**Then open your browser to:**
 http://localhost:8000

