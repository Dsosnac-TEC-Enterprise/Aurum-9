import * as THREE from 'three';

// 1. Scene & Camera Setup
const scene = new THREE.Scene();
scene.fog = new THREE.FogExp2(0x000000, 0.04); // Cyberpunk fog effect

const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(0, 15, 25);
camera.lookAt(0, 0, 0);

// 2. Renderer Setup
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// 3. Create the Digital Battlefield (Grid)
const gridHelper = new THREE.GridHelper(60, 60, 0x005500, 0x002200);
scene.add(gridHelper);

// 4. Spawn Network Nodes (Servers/Endpoints)
const geometry = new THREE.SphereGeometry(1.2, 16, 16);
const nodes = [];
const nodeMaterial = new THREE.MeshBasicMaterial({ color: 0x00ff00, wireframe: true });

// Randomly place 8 nodes on the grid
for (let i = 0; i < 8; i++) {
    const node = new THREE.Mesh(geometry, nodeMaterial.clone());
    node.position.x = (Math.random() - 0.5) * 40;
    node.position.z = (Math.random() - 0.5) * 40;
    scene.add(node);
    nodes.push(node);
}

// 5. Animation Loop (The Core Renderer)
function animate() {
    requestAnimationFrame(animate);
    
    // Idle animation: Slowly rotate the nodes
    nodes.forEach(node => {
        node.rotation.y += 0.01;
        node.rotation.x += 0.005;
    });

    // Simulate HUD Alerts: Randomly flash a node RED (DDoS/Attack simulation)
    if (Math.random() > 0.99) {
        const targetNode = nodes[Math.floor(Math.random() * nodes.length)];
        targetNode.material.color.setHex(0xff0000); // Threat detected (Red)
        
        // Self-heal back to Green after 800ms
        setTimeout(() => {
            targetNode.material.color.setHex(0x00ff00); 
        }, 800);
    }

    renderer.render(scene, camera);
}

// Start the engine
animate();

// 6. Handle Window Resizing
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});
