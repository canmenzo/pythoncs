import tkinter as tk
from tkinter import messagebox
import requests
import json
import os

API_KEY = "{{ INSERT YOUR VT API KEY HERE }}"
CACHE_FILE = "cache.json"

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE) as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)

def query_hash(hash_id):
    cache = load_cache()
    if hash_id in cache:
        return cache[hash_id]

    url = f"https://www.virustotal.com/api/v3/files/{hash_id}"
    headers = {"x-apikey": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        return None
    if response.status_code != 200:
        raise Exception(f"API error: {response.status_code}")

    data = response.json()
    cache[hash_id] = data
    save_cache(cache)
    return data

# Main GUI application class
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("VirusTotal Hash Checker")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        # Top section: hash input and query button
        frame_top = tk.Frame(root, pady=10)
        frame_top.pack(fill="x", padx=20)

        tk.Label(frame_top, text="Hash (MD5/SHA1/SHA256):").pack(side="left")
        self.entry = tk.Entry(frame_top, width=40)
        self.entry.pack(side="left", padx=5)
        tk.Button(frame_top, text="Query", command=self.run_query).pack(side="left")

        # Scrollable text area for results
        self.result_text = tk.Text(root, height=20, state="disabled", bg="#f5f5f5")
        self.result_text.pack(fill="both", padx=20, pady=5)

        # Stats summary label at the bottom
        self.stats_label = tk.Label(root, text="", font=("Arial", 10), justify="left")
        self.stats_label.pack(padx=20, anchor="w")

    def run_query(self):
        hash_id = self.entry.get().strip()
        if not hash_id:
            messagebox.showwarning("Warning", "Please enter a hash.")
            return

        try:
            data = query_hash(hash_id)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        if data is None:
            messagebox.showinfo("Result", "Hash not found on VirusTotal.")
            return

        self.display_results(data)

    def display_results(self, data):
        attrs = data.get("data", {}).get("attributes", {})
        results = attrs.get("last_analysis_results", {})
        stats = attrs.get("last_analysis_stats", {})

        # Clear previous results
        self.result_text.config(state="normal")
        self.result_text.delete("1.0", "end")

        # Build summary line
        malicious = stats.get("malicious", 0)
        suspicious = stats.get("suspicious", 0)
        undetected = stats.get("undetected", 0)
        total = len(results)

        summary = (
            f"Total engines: {total}  |  "
            f"Malicious: {malicious}  |  "
            f"Suspicious: {suspicious}  |  "
            f"Clean: {undetected}"
        )
        self.stats_label.config(text=summary)

        # List each engine and its verdict
        self.result_text.insert("end", "ENGINE RESULTS:\n")
        self.result_text.insert("end", "-" * 50 + "\n")

        for engine, info in sorted(results.items()):
            category = info.get("category", "unknown")
            result = info.get("result") or "-"
            line = f"{engine:<30} [{category}]  {result}\n"
            # Highlight malicious detections in red
            tag = "malicious" if category == "malicious" else "normal"
            self.result_text.insert("end", line, tag)

        self.result_text.tag_config("malicious", foreground="red")
        self.result_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
