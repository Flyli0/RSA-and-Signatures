import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from EncryptionDecryption.Decryption import decrypt
from EncryptionDecryption.Encryption import encrypt
from RSA_Key_Generation.KeysGenerator import generate_keys
from Signatures.Hash_and_sign import sign
from Signatures.Hash_and_sign_Verification import verify
from Padding.PKCS_Padding import pkcs_padding
from Padding.PKCS_Unpadding import pkcs_unpadding
from Padding.OAEP_Padding import oaep
from Padding.OAEP_Unpadding import oaep_unpad


class RSAApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RSA Toolkit")
        self.geometry("900x600")

        self.keys = None

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)
        self.signature = 0

        self.key_tab = ttk.Frame(self.notebook)
        self.rsa_tab = ttk.Frame(self.notebook)
        self.sig_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.key_tab, text="Generate Keys")
        self.notebook.add(self.rsa_tab, text="RSA Encrypt/Decrypt")
        self.notebook.add(self.sig_tab, text="Signature")

        self.build_key_tab()
        self.build_rsa_tab()
        self.build_sig_tab()

    # ================= KEY GENERATION =================
    def build_key_tab(self):
        ttk.Label(self.key_tab, text="Key Size:").pack(pady=10)

        self.key_size = tk.StringVar(value="1024")
        ttk.Combobox(self.key_tab, textvariable=self.key_size,
                      values=["1024", "2048", "4096"]).pack()

        ttk.Button(self.key_tab, text="Generate Keys",
                   command=self.on_generate_keys).pack(pady=10)

        self.key_output = tk.Text(self.key_tab, height=20)
        self.key_output.pack(fill="both", expand=True)

        ttk.Button(self.key_tab, text="Copy Keys",
                   command=self.copy_keys).pack(pady=5)

    def on_generate_keys(self):
        size = int(self.key_size.get())
        pub, priv = generate_keys(size)
        self.keys = (pub, priv)

        self.key_output.delete("1.0", tk.END)
        self.key_output.insert(tk.END, f"PUBLIC KEY:\n{pub}\n\nPRIVATE KEY:\n{priv}")

    def copy_keys(self):
        if self.keys:
            self.clipboard_clear()
            self.clipboard_append(str(self.keys))

    # ================= RSA TAB =================
    def build_rsa_tab(self):
        self.rsa_mode = tk.StringVar(value="encrypt")
        self.rsa_mode.trace_add("write", self.on_rsa_mode_change)
        self.padding = tk.StringVar(value="oaep")
        self.oaep_label = tk.StringVar(value="")

        ttk.Radiobutton(self.rsa_tab, text="Encrypt", variable=self.rsa_mode, value="encrypt").pack()
        ttk.Radiobutton(self.rsa_tab, text="Decrypt", variable=self.rsa_mode, value="decrypt").pack()

        ttk.Label(self.rsa_tab, text="Padding:").pack()
        self.padding_combo = ttk.Combobox(
            self.rsa_tab,
            textvariable=self.padding,
            values=["oaep", "pkcs"]
        )
        self.padding_combo.pack()

        # OAEP label input
        self.label_frame = ttk.Frame(self.rsa_tab)
        self.label_frame.pack(fill="x", pady=5)

        ttk.Label(self.label_frame, text="OAEP Label:").pack(side="left")
        self.label_entry = ttk.Entry(self.label_frame, textvariable=self.oaep_label)
        self.label_entry.pack(side="left", fill="x", expand=True)

        self.padding.trace_add("write", self.on_padding_change)
        self.on_padding_change()

        ttk.Button(self.rsa_tab, text="Load File",
                   command=self.load_file).pack(pady=5)

        ttk.Label(self.rsa_tab, text="Input Text:").pack()
        self.rsa_input = tk.Text(self.rsa_tab, height=10)
        self.rsa_input.pack(fill="both", expand=True)

        ttk.Label(self.rsa_tab, text="Key (paste tuple):").pack()
        self.rsa_key = tk.Entry(self.rsa_tab)
        self.rsa_key.pack(fill="x")

        ttk.Button(self.rsa_tab, text="Run",
                   command=self.run_rsa).pack(pady=10)

        self.rsa_output = tk.Text(self.rsa_tab, height=10)
        self.rsa_output.pack(fill="both", expand=True)

    def on_padding_change(self, *args):
        if self.padding.get() == "oaep":
            self.label_entry.config(state="normal")
        else:
            self.label_entry.config(state="disabled")

    def load_file(self):
        file = filedialog.askopenfilename()
        if file:
            with open(file, "rb") as f:
                self.rsa_input.delete("1.0", tk.END)
                self.rsa_input.insert(tk.END, f.read())

    def parse_key(self):
        try:
            return eval(self.rsa_key.get())
        except:
            messagebox.showerror("Error", "Invalid key format")
            return None

    def on_rsa_mode_change(self, *args):
        # clear key field when switching encrypt/decrypt mode
        self.rsa_key.delete(0, tk.END)

    def run_rsa(self):
        key = self.parse_key()
        if not key:
            return

        data = self.rsa_input.get("1.0", tk.END).strip()
        label = self.oaep_label.get()




        if self.rsa_mode.get() == "encrypt":
            data = data.encode()
            if self.padding.get() == "oaep":
                data = oaep(int(self.key_size.get()),data,label)
                data = int.from_bytes(data,'big')
            else:
                data = pkcs_padding(data, int(self.key_size.get())//8)
                data = int.from_bytes(data, 'big')
            result = encrypt(data, key)
        else:
            data = int(data)
            n = key[0]
            result = decrypt(data, key)
            result = result % n



            k = (n.bit_length() + 7) // 8

            result = result.to_bytes(k, 'big')
            print("EM HEX:", result.hex())
            print("FIRST BYTE:", result[0])
            print("SECOND BYTE:", result[1])
            if self.padding.get() == "oaep":
                result = oaep_unpad(result, int(self.key_size.get()), label)
            else:
                result = pkcs_unpadding(result)

            result = result.decode()

        self.rsa_output.delete("1.0", tk.END)
        self.rsa_output.insert("1.0", result)

    # ================= SIGNATURE TAB =================
    def build_sig_tab(self):
        self.sig_mode = tk.StringVar(value="sign")
        self.sig_mode.trace_add("write", self.on_sig_mode_change)
        self.sig_pad = tk.StringVar(value="pkcs")

        ttk.Radiobutton(self.sig_tab, text="Sign", variable=self.sig_mode, value="sign").pack()
        ttk.Radiobutton(self.sig_tab, text="Verify", variable=self.sig_mode, value="verify").pack()

        ttk.Label(self.sig_tab, text="Padding:").pack()
        ttk.Combobox(self.sig_tab, textvariable=self.sig_pad,
                      values=["pkcs", "pss"]).pack()

        ttk.Label(self.sig_tab, text="Message:").pack()
        self.sig_msg = tk.Text(self.sig_tab, height=6)
        self.sig_msg.pack(fill="both", expand=True)

        # Signature input (used in verify mode)
        self.sig_sig_frame = ttk.Frame(self.sig_tab)
        self.sig_sig_frame.pack(fill="both", expand=True, pady=5)

        ttk.Label(self.sig_sig_frame, text="Signature (int or bytes):").pack()
        self.sig_signature = tk.Text(self.sig_sig_frame, height=4)
        self.sig_signature.pack(fill="both", expand=True)

        ttk.Label(self.sig_tab, text="Key:").pack()
        self.sig_key = tk.Entry(self.sig_tab)
        self.sig_key.pack(fill="x")

        ttk.Button(self.sig_tab, text="Run",
                   command=self.run_sig).pack(pady=10)

        self.sig_out = tk.Text(self.sig_tab, height=8)
        self.sig_out.pack(fill="both", expand=True)

        self.on_sig_mode_change()

    def run_sig(self):
        key = self.parse_sig_key()
        if not key:
            return

        msg = self.sig_msg.get("1.0", tk.END).strip().encode()

        if self.sig_mode.get() == "sign":
            res = sign(msg, key, 1024)
        else:
            sig_text = self.sig_signature.get("1.0", tk.END).strip()
            try:
                # allow int or bytes (hex string)
                if sig_text.startswith("0x"):
                    self.signature = int(sig_text, 16).to_bytes((key[0].bit_length()+7)//8, 'big')
                elif sig_text.isdigit():
                    self.signature = int(sig_text).to_bytes((key[0].bit_length()+7)//8, 'big')
                else:
                    # assume hex without 0x
                    self.signature = bytes.fromhex(sig_text)
            except Exception:
                messagebox.showerror("Error", "Invalid signature format")
                return

            res = verify(msg, self.signature, key)

        self.sig_out.delete("1.0", tk.END)
        self.sig_out.insert(tk.END, str(res))
        key = self.parse_sig_key()
        if not key:
            return

        msg = self.sig_msg.get("1.0", tk.END).strip().encode()

        if self.sig_mode.get() == "sign":
            res = sign(msg, key, 1024)
        else:
            res = verify(msg, self.signature, key)

        self.sig_out.delete("1.0", tk.END)
        self.sig_out.insert(tk.END, str(res))

    def on_sig_mode_change(self, *args):
        self.sig_key.delete(0,tk.END)
        if self.sig_mode.get() == "sign":
            self.sig_signature.config(state="disabled")
        else:
            self.sig_signature.config(state="normal")
    def parse_sig_key(self):
        try:
            return eval(self.sig_key.get())
        except:
            messagebox.showerror("Error", "Invalid key format")
            return None


if __name__ == "__main__":
    app = RSAApp()
    app.mainloop()
