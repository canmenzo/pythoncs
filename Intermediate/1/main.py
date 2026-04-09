import requests
import json
import os

API_KEY = "{{ INSERT YOUR VT API KEY HERE }}"
CACHE_FILE = "cache.json"

# Load previously cached results from disk
def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE) as f:
            return json.load(f)
    return {}

# Save results to disk so we don't repeat API calls for the same hash
def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)

# Query the VirusTotal API (or return cached result if already fetched)
def query_hash(hash_id):
    cache = load_cache()

    if hash_id in cache:
        print("[Cache hit - no API call made]\n")
        return cache[hash_id]

    url = f"https://www.virustotal.com/api/v3/files/{hash_id}"
    headers = {"x-apikey": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        print("Hash not found on VirusTotal.")
        return None
    if response.status_code != 200:
        print(f"API error: {response.status_code}")
        return None

    data = response.json()
    cache[hash_id] = data
    save_cache(cache)
    return data

# Display information based on the user's menu choice
def show_info(choice, attrs):
    results = attrs.get("last_analysis_results", {})
    stats = attrs.get("last_analysis_stats", {})

    if choice == "1":
        print(f"Total engines that scanned this file: {len(results)}")

    elif choice == "2":
        print("Engine list:")
        for name in sorted(results.keys()):
            print(f"  - {name}")

    elif choice == "3":
        print("Engine verdict summary:")
        for k, v in stats.items():
            print(f"  {k}: {v}")

    elif choice == "4":
        hits = stats.get("malicious", 0) + stats.get("suspicious", 0)
        print(f"Positive detections (malicious + suspicious): {hits}")

    elif choice == "5":
        keyword = "ransom"
        print(f"Engines with '{keyword}' in their result:")
        for engine, info in results.items():
            if keyword in json.dumps(info).lower():
                print(f"  [{engine}] {info.get('result')}")

    elif choice == "6":
        keyword = input("Enter keyword to search: ").strip()
        print(f"Engines matching '{keyword}':")
        for engine, info in results.items():
            if keyword.lower() in json.dumps(info).lower():
                print(f"  [{engine}] {info.get('result')}")

    else:
        print("Invalid choice.")

def main():
    hash_id = input("Enter hash (MD5 / SHA1 / SHA256): ").strip()
    data = query_hash(hash_id)
    if not data:
        return

    attrs = data.get("data", {}).get("attributes", {})

    while True:
        print("\n--- Menu ---")
        print("1. How many engines scanned this file")
        print("2. What engines scanned this")
        print("3. Conclusion from the different engines")
        print("4. How many positive hits")
        print("5. Look for keyword 'ransom'")
        print("6. Search for a custom keyword")
        print("0. Exit")

        choice = input("Choice: ").strip()
        if choice == "0":
            break
        show_info(choice, attrs)

if __name__ == "__main__":
    main()
