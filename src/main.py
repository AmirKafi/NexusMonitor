from domain.cpu import CPU
from domain.gpu import GPU
import app
import os
import time

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def format_components_table(data: dict) -> str:
    headers = ["Component", "Name", "Temp", "Usage", "Detail"]
    rows = []
    for comp, attrs in data.items():
        if comp == "cpu":
            detail = f"Cores: {attrs.get('cores', '')}"
        elif comp == "gpu":
            detail = f"Clock: {attrs.get('clock', '')}"
        else:
            detail = ""
        rows.append([
            comp.upper(),
            str(attrs.get("name", "")),
            str(attrs.get("temp", "")),
            str(attrs.get("usage", "")),
            detail
        ])

    # compute column widths
    col_widths = [
        max(len(headers[i]), max((len(row[i]) for row in rows), default=0))
        for i in range(len(headers))
    ]

    sep = " | "
    header_line = sep.join(headers[i].ljust(col_widths[i]) for i in range(len(headers)))
    divider = "-+-".join("-" * col_widths[i] for i in range(len(headers)))

    lines = [header_line, divider]
    for row in rows:
        lines.append(sep.join(row[i].ljust(col_widths[i]) for i in range(len(headers))))

    return "\n".join(lines)

def recursive_update(cpu: CPU, gpu: GPU, interval=1):
    while True:
        try:
            app.read_sensors(cpu, gpu)

            data = {
                "cpu": {
                    "name": cpu.name,
                    "temp": f"{cpu.temp} °C",
                    "usage": f"{int(cpu.usage)} %",
                    "cores": cpu.cores_count
                },
                "gpu": {
                    "name": gpu.name,
                    "temp": f"{gpu.temp} °C",
                    "usage": f"{int(gpu.usage)} %",
                    "clock": gpu.gpu_clock
                }
            }

            clear_console()
            table = format_components_table(data)
            print(table)

            time.sleep(interval)
        except KeyboardInterrupt:
            print("Exiting monitoring...")
            break

def main():
    cpu,gpu = app.discover_components()
    recursive_update(cpu, gpu, interval=1)



if __name__ == "__main__":
    main()
