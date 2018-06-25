"""
# Linux serial reader

## Usage

In Linux environment, run following.
```shell
python serial_reader.py
```

## Permission handling
If you have a permission error in accessing `PORT`, you need to add your user to `dialout` group (typically).

```shell
sudo usermod -a -G dialout "$USER"
```
"""
import serial

PORT = "/dev/ttyUSB0"
BAUD_RATE = 115200


def main():
    ser = serial.Serial(
        port=PORT,
        baudrate=BAUD_RATE,
        # parity=serial.PARITY_NONE,
        # stopbits=serial.STOPBITS_ONE,
        # bytesize=serial.EIGHTBITS,
        timeout=1,
    )
    while True:
        x = ser.readline()
        print(x)


if __name__ == "__main__":
    main()
