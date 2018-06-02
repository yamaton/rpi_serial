"""
# Raspberry Pi serial producer

Loads a local text file and keeps write it out to serial port repeatedly.

## Usage
$ python serial_producer.py <local_text_file> --with_header

With `--with_header` the stream shows the header line only once.

"""
import time
import argparse
import itertools
import serial

DEFAULT_FPS = 30
BAUD_RATE = 115200


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="""Path to text file (assuming csv)""")
    parser.add_argument(
        "--with_header", action="store_true", help="""Handle the first line as header"""
    )
    parser.add_argument(
        "--fps", default=DEFAULT_FPS, type=int, help="""FPS of serial write"""
    )
    args = parser.parse_args()
    return args


def gen_lines(filepath, with_header=True):
    with open(filepath, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    if with_header:
        yield lines[0]
        lines = lines[1:]

    for line in itertools.cycle(lines):
        yield line


def main():

    ser = serial.Serial(
        port="/dev/ttyAMA0",
        baudrate=BAUD_RATE,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1,
    )

    args = parse_args()
    lines = gen_lines(args.filepath, with_header=args.with_header)
    interval_sec = 1 / args.fps

    for line in lines:
        ser.write(line)
        time.sleep(interval_sec)


if __name__ == "__main__":
    main()
