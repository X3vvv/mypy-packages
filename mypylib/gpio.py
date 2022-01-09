"""
My GPIO library.
"""


def get_channel(default: int = 21):
    """
    Get a channel number from user input.
    Accept `GPIO0` ~ `GPIO27`.

    ### Raspberry Pi 4B GPIO Interface (BCM scheme)
    ```
       3V3  (1) (2)  5V
     GPIO2  (3) (4)  5V
     GPIO3  (5) (6)  GND
     GPIO4  (7) (8)  GPIO14
       GND  (9) (10) GPIO15
    GPIO17 (11) (12) GPIO18
    GPIO27 (13) (14) GND
    GPIO22 (15) (16) GPIO23
       3V3 (17) (18) GPIO24
    GPIO10 (19) (20) GND
     GPIO9 (21) (22) GPIO25
    GPIO11 (23) (24) GPIO8
       GND (25) (26) GPIO7
     GPIO0 (27) (28) GPIO1
     GPIO5 (29) (30) GND
     GPIO6 (31) (32) GPIO12
    GPIO13 (33) (34) GND
    GPIO19 (35) (36) GPIO16
    GPIO26 (37) (38) GPIO20
       GND (39) (40) GPIO21
    ```
    """
    legal_pin_raspi4b_BCM = [i for i in range(0, 28)]  # GPIO0~GPIO27
    channel = default if default in legal_pin_raspi4b_BCM else legal_pin_raspi4b_BCM[0]

    new = input(f"Enter a channel [default:{channel}]: ")
    while True:
        if new.strip() == "":  # empty input
            break  # using default channel
        elif not new.isnumeric:  # non numeric
            new = input("Error! Channel must be integer: ")
        else:  # numeric
            if int(new) not in legal_pin_raspi4b_BCM:
                new = input("Error! Invalid channel: ")
            else:  # accept the new channel
                break

    return int(channel)
