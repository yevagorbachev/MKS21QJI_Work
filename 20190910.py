from random import choice

krewes = {
    'crew1':['0x00','0x01','0x02','0x03','0x04','0x05',],
    'crew2':['0x10','0x11','0x12','0x13','0x14','0x15',],
    'crew3':['0x20','0x21','0x22','0x23','0x24','0x25',],
    'crew4':['0x30','0x31','0x32','0x33','0x34','0x35',],
}
print(choice(krewes[choice([key for key in krewes.keys()])]))