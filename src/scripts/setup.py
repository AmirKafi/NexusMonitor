import requests
from tqdm import tqdm
import zipfile
from configs import EXTRACT_DIR,DOWNLOAD_PATH,LHM_ZIP_URL, SDK_NAME
import os
import ctypes
import time

def download_file(url,dest_path):
    try:
        response = requests.get(url,stream=True,timeout=10)
        response.raise_for_status()
        total = int(response.headers.get('content-length',0) or 0)
        with open(dest_path,'wb') as f,tqdm(
            desc="Downloading",
            total=total,
            unit='B',
            unit_scale=True,
            unit_divisor=1024
        ) as bar:
            for data in response.iter_content(chunk_size=1024):
                if not data:
                    continue
                f.write(data)
                bar.update(len(data))
        print("Download completed!")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error Downloading file: {e}")
    
def extract_zip_from_path(zip_path):
    print(f"Extracting: {zip_path}")
    try:
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(EXTRACT_DIR)
        print("Extraction complete!")
    except zipfile.BadZipFile as e:
        raise RuntimeError(f"Error extracting ZIP: {e}")
    
def get_lhm_exe():
    for root, dirs, files in os.walk(EXTRACT_DIR):
        for fname in files:
            if fname.lower().endswith('.exe'):
                return os.path.join(root, fname)
    print("Executable not found in extracted folder")
    return None

def ready_files():
    if not os.path.isfile(DOWNLOAD_PATH):
        download_file(LHM_ZIP_URL, DOWNLOAD_PATH)

    if not os.path.isdir(EXTRACT_DIR):
        extract_zip_from_path(DOWNLOAD_PATH)

def run_as_admin_minimized(exe_path):
    try:
        SW_SHOWMINIMIZED = 2
        ctypes.windll.shell32.ShellExecuteW(None, 'runas', exe_path, None, None, SW_SHOWMINIMIZED)
        return True
    except Exception as exc:
        print(f"Failed to launch {exe_path} as admin: {exc}")
        return False
    
def initialize():
    print(f"Preparing {SDK_NAME}...")
    ready_files()    
    time.sleep(5)
    print("Setup Complete.")