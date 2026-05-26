import os
import time
from PIL import Image, ImageEnhance

# --- FOLDER SETTINGS ---
# Aksar phones me yehi path hota hai camera photos ke liye
CAMERA_PATH = "/sdcard/DCIM/Camera/"
OUTPUT_PATH = "/sdcard/DCIM/Camera/aura_result.jpg"

def get_smart_selection():
    print("\n--- 📸 AURA LIGHT: CAMERA SCANNER ---")
    
    if not os.path.exists(CAMERA_PATH):
        print(f"❌ Camera folder nahi mila: {CAMERA_PATH}")
        print("Tip: Pydroid settings me jaakar 'All Files Access' allow karein.")
        return None

    # Camera folder se latest 10 photos uthana
    try:
        files = [f for f in os.listdir(CAMERA_PATH) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        # Time ke hisaab se sort (Latest upar)
        files.sort(key=lambda x: os.path.getmtime(os.path.join(CAMERA_PATH, x)), reverse=True)
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

    if not files:
        print("❌ Camera folder khali hai bhai!")
        return None

    print("\nSelect karein (Latest photos upar hain):")
    print("-" * 50)
    for i, file in enumerate(files[:10]):
        full_path = os.path.join(CAMERA_PATH, file)
        # Size aur Time nikalna pehchan ke liye
        size_mb = os.path.getsize(full_path) / (1024 * 1024)
        mod_time = time.strftime('%I:%M %p', time.localtime(os.path.getmtime(full_path)))
        
        print(f"[{i}] {file} | {size_mb:.1f} MB | Time: {mod_time}")
    print("-" * 50)

    try:
        idx = int(input("\nKaunsi photo (Number)? "))
        return os.path.join(CAMERA_PATH, files[idx])
    except:
        print("❌ Galat input!")
        return None

def apply_aura_filter(input_path):
    try:
        img = Image.open(input_path).convert("RGB")
        print(f"\n✨ Processing: {os.path.basename(input_path)}...")

        # 1. Vivo V40e level Sharpness
        img = ImageEnhance.Sharpness(img).enhance(2.8)

        # 2. Aura Warmth (Golden-Orange Glow)
        # Red: 255, Green: 165, Blue: 80
        aura_layer = Image.new("RGB", img.size, (255, 165, 80))
        img = Image.blend(img, aura_layer, 0.12)

        # 3. Aesthetic Contrast & Color
        img = ImageEnhance.Contrast(img).enhance(1.2)
        img = ImageEnhance.Color(img).enhance(1.3)

        # 4. Save to Downloads (Taaki aasani se mil jaye)
        img.save(OUTPUT_PATH, quality=100)
        print(f"\n✅ DHAMAKA TAIYAR!")
        print(f"📂 Check karo: {OUTPUT_PATH}")

    except Exception as e:
        print(f"❌ Error: {e}")

# --- EXECUTION ---
selected = get_smart_selection()
if selected:
    apply_aura_filter(selected)
