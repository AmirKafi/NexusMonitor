from typing import Tuple
import clr
import os
import time
from configs import EXTRACT_DIR

from domain.cpu import CPU
from domain.gpu import GPU
import scripts.setup as setup
import wmi

DLL_PATH = os.path.join(EXTRACT_DIR,r"LibreHardwareMonitorLib.dll")
if not os.path.isfile(DLL_PATH):
    setup.initialize()

clr.AddReference(DLL_PATH)

from LibreHardwareMonitor.Hardware import Computer  # type: ignore # noqa: E402

def discover_components():
    cpu_name = None
    gpu_name = None

    c = wmi.WMI()

    # CPU name
    for cpu in c.Win32_Processor():
        cpu_name = cpu.Name
        break 

    # GPU name
    for gpu in c.Win32_VideoController():
        gpu_name = gpu.Name
        break 

    return CPU(cpu_name), GPU(gpu_name)

def read_sensors(cpu: CPU, gpu: GPU):
    c = Computer()
    c.IsCpuEnabled = True
    c.IsGpuEnabled = True
    c.IsMotherboardEnabled = True
    c.Open()

    for hw in c.Hardware:
        hw.Update()
        for shw in hw.SubHardware:
            shw.Update()

    time.sleep(0.2)
    for h in c.Hardware:
        h.Update()
        for shw in h.SubHardware:
            shw.Update()

        if "cpu" in h.HardwareType.ToString().lower():
                cores = 0
                for sensor in h.Sensors:
                    stype = str(sensor.SensorType).lower()
                    if stype == "temperature" and "package" in sensor.Name.lower() and sensor.Value is not None:
                        cpu.update_temp(sensor.Value)
                    elif stype == "load":
                        if "total" in sensor.Name.lower() and sensor.Value is not None:
                            cpu.update_usage(sensor.Value)
                        if sensor.Name.lower().startswith("cpu core #") and not sensor.Name.lower().endswith("#2"):
                            cores += 1

                if cores > 0:
                    cpu.update_cores_count(cores)

        elif "gpu" in h.HardwareType.ToString().lower():
            for sensor in h.Sensors:
                stype = str(sensor.SensorType).lower()
                if stype == "temperature" and "core" in sensor.Name.lower() and sensor.Value is not None:
                    gpu.update_temp(sensor.Value)
                elif stype == "load" and "core" in sensor.Name.lower():
                    gpu.update_usage(sensor.Value)
                elif stype == "clock" and "core" in sensor.Name.lower():
                    gpu.update_clock(float(sensor.Value))

    c.Close()