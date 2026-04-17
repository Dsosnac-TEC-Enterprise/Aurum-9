# 🤝 Contributing to Aurum-9

Thank you for helping build the future of autonomous defense! To keep Aurum-9 "Iron-Clad," please follow these rules:

### 1. The Logic Receipt Rule
Every new function that performs an autonomous action **MUST** call the `ExplainableAILogger`. No "black box" decisions are allowed.

### 2. Integrity Management
If you modify core logic, you must update the `hash_registry.json` by running:
`python -m core_ironclad.self_healing` 
(Ensure you are authorized before updating baselines!)

### 3. Code Quality
* Follow PEP 8 for Python.
* All network actions must be simulated in the base logic before being connected to production APIs.
* Use Docker for all environment-specific testing.
