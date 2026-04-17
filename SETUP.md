## 🛠️ Installation & Setup

Deploy the Aurum-9 framework using the automated setup script. This will configure your virtual environment, install dependencies, and launch the Neural Commander.

### Prerequisites
* **Python 3.11+**
* **Git**
* **Docker** (Optional, for Shadow-Clone containerization)

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sosnac/Aurum-9.git
   cd Aurum-9
```
2. **Run the deployment script:**
   ```bash
   chmod +x setup.sh
./setup.sh
```
3. 🖥️ **Accessing the Tactical HUD:**
Once the backend is running, navigate to the 3D HUD directory:
   ```bash
cd tactical_hud/frontend_3d
python3 -m http.server 8000
```
**Then open your browser to**
 http://localhost:8000.
