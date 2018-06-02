"""
# Linux serial reader

## Usage

In Linux environment, run following.
```shell
$ python serial_reader.py
```

"""
import serial

BAUD_RATE = 115200


def main():
    ser = serial.Serial(
        port="/dev/ttyUSB0",
        baudrate=BAUD_RATE,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1,
    )

    while True:
        x = ser.readline()
        print(x)


if __name__ == "__main__":
    main()
