from smbus2 import SMBus, i2c_msg
import struct

def main():
    write_msg = i2c_msg.write(0x38, [0xac, 0x33, 0x00])
    read_msg = i2c_msg.read(0x38, 7)

    with SMBus(1) as bus:
        bus.i2c_rdwr(write_msg, read_msg)

    data = bytes(read_msg)
    raw_humidity = (
        (data[1] << 12) |
        (data[2] << 4) |
        ((data[3] & 0xF0) >> 4)
    )
    humidity = (raw_humidity / (1 << 20)) * 100
    print(f"Humidity: {humidity:.2f} %")

    raw_temp = (
        ((data[3] & 0x0F) << 16) |  # lower 4 bits of byte 3
        (data[4] << 8) |
        data[5]
    )
    temperature = (raw_temp / (1 << 20)) * 200 - 50
    print(f"Temperature: {temperature:.2f} °C")


if __name__ == "__main__":
    main()
