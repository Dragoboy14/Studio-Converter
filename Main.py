import os
import time
import subprocess
import shutil
from concurrent.futures import ProcessPoolExecutor
from PIL import Image, ImageEnhance

# --- PATH SETTINGS ---
BASE_PATH = "/sdcard/DCIM/Camera/"
DOWNLOAD_PATH = "/sdcard/Download/"
TMP_FRAMES = os.path.join(DOWNLOAD_PATH, "tmp_frames")
TMP_AUDIO = os.path.join(DOWNLOAD_PATH, "tmp_audio.mp3")

# --- CORE MAGIC: THE FILTER ---
def apply_aura_core(img):
    """Tera signature filter logic jo Photo/Video dono mein chalega"""
    # 1. Sharpness
    img = ImageEnhance.Sharpness(img).enhance(2.8)
    # 2. Aura Warmth
    aura_layer = Image.new("RGB", img.size, (255, 165, 80))
    img = Image.blend(img, aura_layer, 0.12)
    # 3. Contrast & Color
    img = ImageEnhance.Contrast(img).enhance(1.2)
    img = ImageEnhance.Color(img).enhance(1.3)
    return img

# --- STEP 3: MULTI-CORE WORKER ---
def process_single_frame(frame_name):
    frame_path = os.path.join(TMP_FRAMES, frame_name)
    try:
        img = Image.open(frame_path).convert("RGB")
        img = apply_aura_core(img)
        img.save(frame_path, quality=95) # Video ke liye 95 optimized hai
        return True
    except:
        return False

# --- VIDEO ENGINE ---
def run_video_pipeline(video_path):
    print("🎬 Step 1 & 2: Extracting Audio & Frames (30 FPS)...")
    if os.path.exists(TMP_FRAMES): shutil.rmtree(TMP_FRAMES)
    os.makedirs(TMP_FRAMES)
    
    # Audio extract karna
    subprocess.run(f"ffmpeg -i '{video_path}' -q:a 0 -map a '{TMP_AUDIO}' -y", shell=True)
    # Frames extract karna
    subprocess.run(f"ffmpeg -i '{video_path}' -vf fps=30 '{TMP_FRAMES}/f_%05d.jpg' -y", shell=True)

    frames = sorted(os.listdir(TMP_FRAMES))
    print(f"🚀 Step 3: Firing 6 Cores for {len(frames)} frames...")
    
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=6) as executor:
        list(executor.map(process_single_frame, frames))
    
    print(f"⚡ Processing Time: {time.time() - start_time:.2f} sec")

    print("🧵 Step 4 & 5: Rebuilding Video & Syncing Audio...")
    output_video = os.path.join(DOWNLOAD_PATH, "aura_video_result.mp4")
    # Video stitching + Audio merging
    cmd = (f"ffmpeg -y -framerate 30 -i '{TMP_FRAMES}/f_%05d.jpg' -i '{TMP_AUDIO}' "
           f"-c:v libx264 -pix_fmt yuv420p -c:a aac -shortest '{output_video}'")
    subprocess.run(cmd, shell=True)

    print("🧹 Step 6: Cleaning up temp folders...")
    shutil.rmtree(TMP_FRAMES)
    if os.path.exists(TMP_AUDIO): os.remove(TMP_AUDIO)
    print(f"✅ MISSION SUCCESS! Saved to: {output_video}")

# --- PHOTO ENGINE (Tera Code Sync kiya hai) ---
def run_photo_pipeline():
    print("\n--- 📸 AURA LIGHT: PHOTO SCANNER ---")
    files = [f for f in os.listdir(BASE_PATH) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    files.sort(key=lambda x: os.path.getmtime(os.path.join(BASE_PATH, x)), reverse=True)

    for i, file in enumerate(files[:10]):
        size_mb = os.path.getsize(os.path.join(BASE_PATH, file)) / (1024*1024)
        print(f"[{i}] {file} | {size_mb:.1f} MB")
    
    idx = int(input("\nPhoto Number? "))
    img_path = os.path.join(BASE_PATH, files[idx])
    
    img = Image.open(img_path).convert("RGB")
    img = apply_aura_core(img)
    
    out = os.path.join(DOWNLOAD_PATH, "aura_photo_result.jpg")
    img.save(out, quality=100)
    print(f"✅ Photo Saved: {out}")

# --- MAIN MENU ---
if __name__ == "__main__":
    print("--- 💀 AURA BAAP MULTI-CORE V1 ---")
    print("[1] Photo Edit")
    print("[2] Video Edit (6 Cores / 30 FPS)")
    
    mode = input("Select Mode: ")
    if mode == '1':
        run_photo_pipeline()
    elif mode == '2':
        # Video selection logic (Latest video uthayega)
        vids = [f for f in os.listdir(BASE_PATH) if f.lower().endswith(('.mp4', '.mkv', '.mov'))]
        vids.sort(key=lambda x: os.path.getmtime(os.path.join(BASE_PATH, x)), reverse=True)
        
        for i, v in enumerate(vids[:5]):
            print(f"[{i}] {v}")
        
        v_idx = int(input("Video Number? "))
        run_video_pipeline(os.path.join(BASE_PATH, vids[v_idx]))
