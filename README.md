# 💀 AuraEngine v1.0
### *Extreme 6-Core Video & Photo Processing on Android*
**AuraEngine** is a high-performance media enhancement tool built for developers and creators who want professional-grade color grading and sharpness directly on their mobile devices. Forget Cloud processing—we squeeze every single drop of juice from your phone's multi-core processor.
---
## 🔥 The "Aura" Difference
Unlike basic filters that just overlay a color, AuraEngine deconstructs your video into individual frames, processes them in **Parallel** using **6 CPU Cores**, and re-stitches them with zero audio-lag.
* **⚡ V40e Level Sharpness:** Advanced `ImageEnhance` algorithms for that "Crisp" look.
* **✨ Golden Aura Glow:** Signature warmth blending for a divine, aesthetic look.
* **🏎️ True Multiprocessing:** Utilizing `ProcessPoolExecutor` to make your mobile CPU fly.
* **🐧 Termux Optimized:** Built to thrive in the "Ultimate Mobile Linux" environment.
---
## 🛠️ The Tech Stack (Open Source)
I built this because most mobile apps are too slow, compress your quality, or hide features behind paywalls. AuraEngine is raw, open, and incredibly fast.
* **Engine:** `FFmpeg` (The Swiss Army Knife of Video)
* **Heart:** `Python 3.x`
* **Lungs:** `Pillow (PIL)` for precise frame-by-frame manipulation.
* **Nitrous:** `concurrent.futures` for dedicated 6-core parallelism.
---
## 📸 Dual-Mode Engine
AuraEngine brings high-end aesthetics to both your videos and your photography:
* **Photo Mode:** Single-frame processing with 100% quality retention. It scans your `DCIM/Camera` folder for an instant Aura upgrade.
* **Video Mode (Beast Mode):** Extracts video at 30 FPS, processes frames in parallel batches, and merges them back with the original audio.
---
## 📽️ Proof of Concept (See it to believe it)

| Mode | Original (Before) | AuraEngine Result |
| :--- | :--- | :--- |
| **Photo** | ![Original Photo](assets/photo_before.jpg) | ![Aura Photo](assets/photo_after.jpg) |
| **Video** | [🔗 View Original Video](assets/video_before.mp4) | [🔗 View Aura Video](assets/video_after.mp4) |

## 🚀 Installation & Usage (Termux)

1. **Grant Storage Access:**
   ```bash
   termux-setup-storage
2. **Install System Dependencies**
   ```bash
   pkg update && pkg upgrade
   pkg install python ffmpeg
3. **Install libraries**
   ```bash
   pip install pillow
4. **Create Script**
   ```bash
   (Copy script from main.py)
   nano main.py
5. **Make script executable ans run it**
  ```bash
  chmod +x main.py
  python main.py

##Thanks. Devloper -- Darsh Ameta😎
