# NexusMonitor

A real-time system hardware monitoring application for Windows that displays CPU and GPU metrics including temperature, usage, and performance details.

## Overview

NexusMonitor is a Python-based system monitoring tool that provides live tracking of your computer's hardware components. It uses **LibreHardwareMonitor** for hardware sensor data collection and displays real-time metrics in a formatted console interface.

## Features

- **CPU Monitoring**: Real-time temperature, usage percentage, and core count
- **GPU Monitoring**: Real-time temperature, usage percentage, and clock speed
- **Live Updates**: Continuously refreshes hardware metrics at configurable intervals
- **Formatted Display**: Clean console table interface for easy readability
- **Cross-Component Tracking**: Tracks multiple hardware components simultaneously

## System Requirements

- **Python**: 3.13 or higher
- **OS**: Windows (uses WMI and LibreHardwareMonitor)
- **Dependencies**:
  - `pythonnet` (3.0.5+) - .NET interoperability for Python
  - `requests` (2.32.5+) - HTTP library
  - `tqdm` (4.67.1+) - Progress bars
  - `wmi` (1.5.1+) - Windows Management Instrumentation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AmirKafi/NexusMonitor.git
cd NexusMonitor
```

2. Install dependencies using `uv` (recommended) or `pip`:
```bash
# Using uv
uv pip install -r src/requirements.txt

# Or using pip
pip install pythonnet requests tqdm wmi
```

3. The application automatically extracts LibreHardwareMonitor on first run if needed.

## Usage

Run the application from the `src` directory:

```bash
cd src
python main.py
```

The application will:
1. Initialize LibreHardwareMonitor
2. Discover your CPU and GPU components
3. Display a formatted table with real-time metrics
4. Continuously update the metrics at 1-second intervals (configurable)

### Console Output Example

```
Component | Name              | Temp  | Usage | Detail
----------+-------------------+-------+-------+-------------------
CPU       | Intel Core i7     | 45°C  | 25%   | Cores: 8
GPU       | NVIDIA GeForce RTX| 62°C  | 60%   | Clock: 1850 MHz
```

## Project Structure

```
NexusMonitor/
├── src/
│   ├── app.py              # Hardware discovery and monitoring logic
│   ├── main.py             # Entry point and CLI interface
│   ├── configs.py          # Configuration settings
│   ├── requirements.txt    # Python dependencies
│   └── domain/
│       ├── component.py    # Base hardware component class
│       ├── cpu.py          # CPU-specific implementation
│       └── gpu.py          # GPU-specific implementation
├── LibreHardwareMonitor/   # LibreHardwareMonitor binaries
├── pyproject.toml          # Project metadata and dependencies
└── README.md               # This file
```

## Configuration

Configuration settings can be modified in `src/configs.py`:
- `EXTRACT_DIR`: Directory for LibreHardwareMonitor extraction
- Monitor update interval and other settings

## Technical Details

- **LibreHardwareMonitor**: Uses the .NET library for comprehensive hardware sensor access
- **WMI Integration**: Windows Management Instrumentation for CPU/GPU discovery
- **pythonnet**: Bridges Python and .NET for seamless library integration

## License

This project is maintained by [AmirKafi](https://github.com/AmirKafi).

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

---

**Note**: Requires administrator privileges to access certain hardware sensors on Windows.