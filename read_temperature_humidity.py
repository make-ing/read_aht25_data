from smbus2 import SMBus, i2c_msg


def main():
    write_msg = i2c_msg.write(0x38, [0xac, 0x33, 0x00])
    read_msg = i2c_msg.read(0x38, 7)

    with SMBus(1) as bus:
        bus.i2c_rdwr(write_msg, read_msg)

    data = bytes(read_msg)
    print(data)


if __name__ == "__main__":
    main()
