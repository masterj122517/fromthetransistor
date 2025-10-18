#!/usr/bin/env python3
import sys
import re

def parse_vcd(filename):
    with open(filename) as f:
        lines = f.readlines()

    times = []
    signals = {}
    id_to_name = {}
    current_time = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # 信号定义，例如：$var wire 1 ! a $end
        if line.startswith("$var"):
            parts = line.split()
            id_to_name[parts[3]] = parts[4]
            signals[parts[4]] = []
        # 时间标记，例如：#100
        elif line.startswith("#"):
            current_time = int(line[1:])
            times.append(current_time)
            for name in signals:
                if len(signals[name]) < len(times):
                    signals[name].append(signals[name][-1] if signals[name] else 0)
        # 值变化，例如：1! 或 0"
        elif line[0] in ("0", "1"):
            value = int(line[0])
            sig_id = line[1:]
            if sig_id in id_to_name:
                name = id_to_name[sig_id]
                signals[name][-1] = value

    return times, signals


def draw_waveform(times, signals, width=8):
    # 打印时间标尺
    print("Time: ", end="")
    for t in times:
        print(f"{t:<{width}}", end="")
    print("\n       " + "—" * (width * len(times)))

    # 打印每个信号波形
    for name, values in signals.items():
        line = f"{name:<5}: "
        for v in values:
            line += ("█" * width) if v else ("─" * width)
        print(line)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 vcd_ascii_viewer.py <file.vcd>")
        sys.exit(1)

    filename = sys.argv[1]
    times, signals = parse_vcd(filename)
    draw_waveform(times, signals)


if __name__ == "__main__":
    main()
