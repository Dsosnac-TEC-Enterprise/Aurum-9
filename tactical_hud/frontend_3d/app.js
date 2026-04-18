import * as THREE from 'three';

// --- NEW: Logging System Logic ---
const consoleLog = document.getElementById('console-log');

function addLog(message, type = 'info') {
    const entry = document.createElement('div');
    entry.className = `log-entry log-${type}`;
    
    // Create a timestamp (e.g., 14:05:22)
    const time = new Date().toLocaleTimeString('en-US', { hour12: false });
    entry.innerText = `[${time}] ${message}`;
    
    consoleLog.appendChild(entry);
    
    // Auto-scroll to the bottom so newest logs are always visible
    consoleLog.scrollTop = consoleLog.scrollHeight;
}

// Initial Boot Sequence Logs
addLog("NEURAL COMMANDER: Interface connected.", "info");
addLog("GHOST LEGION: Ephemeral probes deployed.", "info");
addLog("ORACLE: Threat intel polling active.", "warning");
addLog("AWAITING ANOMALIES...", "info");

// --- 1. Scene & Camera Setup ---
const scene = new THREE.Scene();
scene.fog = new THREE.FogExp2(0x000000, 0.04); 

const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(0, 15, 25);
camera.lookAt(0, 0, 0);

// --- 2. Renderer Setup ---
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// --- 3. Create the Digital Battlefield (Grid) ---
const gridHelper = new THREE.GridHelper(60, 60, 0x005500, 0x002200);
scene.add(gridHelper);

// --- 4. Spawn Network Nodes ---
const geometry = new THREE.SphereGeometry(1.2, 16, 16);
const nodes = [];
const nodeMaterial = new THREE.MeshBasicMaterial({ color: 0x00ff00, wireframe: true });

for (let i = 0; i < 8; i++) {
    const node = new THREE.Mesh(geometry, nodeMaterial.clone());
    node.position.x = (Math.random() - 0.5) * 40;
    node.position.z = (Math.random() - 0.5) * 40;
    
    // Give each node a fake IP address for the logs
    node.userData = { 
        ip: `10.0.0.${Math.floor(Math.random() * 255)}`,
        isUnderAttack: false 
    };
    
    scene.add(node);
    nodes.push(node);
}

// --- 5. Animation Loop (The Core Renderer) ---
function animate() {
    requestAnimationFrame(animate);
    
    // Idle animation: Slowly rotate the nodes
    nodes.forEach(node => {
        node.rotation.y += 0.01;
        node.rotation.x += 0.005;
    });

    // Simulate HUD Alerts & Logs
    if (Math.random() > 0.995) { // Trigger roughly every few seconds
        const targetNode = nodes[Math.floor(Math.random() * nodes.length)];
        
        if (!targetNode.userData.isUnderAttack) {
            targetNode.userData.isUnderAttack = true;
            targetNode.material.color.setHex(0xff0000); // Turn Red
            
            // Log the Attack
            addLog(`ENTROPY SPIKE: Anomalous traffic on ${targetNode.userData.ip}`, "critical");
            addLog(`KINETIC C2: Micro-segmentation initiated for ${targetNode.userData.ip}`, "warning");
            
            // Self-heal back to Green after 2 seconds
            setTimeout(() => {
                targetNode.material.color.setHex(0x00ff00); 
                targetNode.userData.isUnderAttack = false;
                
                // Log the Resolution
                addLog(`IRON-CLAD: Traffic normalized. ${targetNode.userData.ip} restored to grid.`, "info");
            }, 2000);
        }
    }

    renderer.render(scene, camera);
}

// Start the engine
animate();

// --- 6. Handle Window Resizing ---
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});
