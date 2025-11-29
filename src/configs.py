import os
from pathlib import Path

SDK_NAME = "LibreHardwareMonitor"


LHM_ZIP_URL = "https://github.com/LibreHardwareMonitor/LibreHardwareMonitor/releases/download/v0.9.4/LibreHardwareMonitor-net472.zip"

# Project root is one level above this `src` package directory.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
TEMP_DIR = PROJECT_ROOT / SDK_NAME
os.makedirs(TEMP_DIR, exist_ok=True)

DOWNLOAD_PATH = os.path.join(str(TEMP_DIR), f"{SDK_NAME}.zip")
EXTRACT_DIR = os.path.join(str(TEMP_DIR), "extracted")