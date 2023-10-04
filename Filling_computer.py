import time
import socket
import os


s = socket.socket()
s.bind(('192.168.1.241', 2000))
s.listen(10)

os.system('start cmd /k python valve_1_2_3.py')
conn1, addr1 = s.accept()

os.system('start cmd /k python valve_4_5_6.py')
conn2, addr2 = s.accept()

os.system('start cmd /k python valve_7_8_9.py')
conn3, addr3 = s.accept()

os.system('start cmd /k python valve_10_11_12.py')
conn4, addr4 = s.accept()

os.system('start cmd /k python valve_13_14_15.py')
conn5, addr5 = s.accept()

os.system('start cmd /k python valve_16_17_18.py')
conn6, addr6 = s.accept()

os.system('start cmd /k python valve_19_20_21.py')
conn7, addr7 = s.accept()

os.system('start cmd /k python valve_22_23_24.py')
conn8, addr8 = s.accept()

os.system('start cmd /k python valve_25_26_27.py')
conn9, addr9 = s.accept()

os.system('start cmd /k python valve_28_29_30.py')
conn10, addr10 = s.accept()

os.system('start cmd /k python valve_31_32_33.py')
conn11, addr11 = s.accept()

os.system('start cmd /k python valve_34_35_36.py')
conn12, addr12 = s.accept()

os.system('start cmd /k python valve_37_38_39.py')
conn13, addr13 = s.accept()

os.system('start cmd /k python valve_40_41_42.py')
conn14, addr14 = s.accept()

os.system('start cmd /k python valve_43_44_45.py')
conn15, addr15 = s.accept()

os.system('start cmd /k python valve_46_47_48.py')
conn16, addr16 = s.accept()

os.system('start cmd /k python valve_49_50_51.py')
conn17, addr17 = s.accept()

os.system('start cmd /k python valve_52_53_54.py')
conn18, addr18 = s.accept()

os.system('start cmd /k python valve_55_56_57.py')
conn19, addr19 = s.accept()

os.system('start cmd /k python valve_58_59_60.py')
conn20, addr20 = s.accept()

os.system('start cmd /k python valve_61_62_63.py')
conn21, addr21 = s.accept()

os.system('start cmd /k python valve_64_65_66.py')
conn22, addr22 = s.accept()

os.system('start cmd /k python valve_67_68_69.py')
conn23, addr23 = s.accept()

os.system('start cmd /k python valve_70_71_72.py')
conn24, addr24= s.accept()

os.system('start cmd /k python valve_73_74_75.py')
conn25, addr25 = s.accept()

os.system('start cmd /k python valve_76_77_78.py')
conn26, addr26 = s.accept()

os.system('start cmd /k python valve_79_80_81.py')
conn27, addr27 = s.accept()

os.system('start cmd /k python valve_82_83_84.py')
conn28, addr28 = s.accept()

os.system('start cmd /k python valve_85_86_87.py')
conn29, addr29 = s.accept()

os.system('start cmd /k python encoder.py')
conn30, addr30 = s.accept()

i = 0

sectors = {0: 'start_pos',
           10: 'CO2',
           60: 'slow_filling',
           120: 'fast_filling',
           310: 'press_reset',
           340: 'start_pos'}

valves = [[0, conn1, 'valve_1'],
          [2, conn1, 'valve_2'],
          [4, conn1, 'valve_3'],
          [6, conn2, 'valve_1'],
          [8, conn2, 'valve_2'],
          [10, conn2, 'valve_3'],
          [12, conn3, 'valve_1'],
          [14, conn3, 'valve_2'],
          [16, conn3, 'valve_3'],
          [18, conn4, 'valve_1'],
          [20, conn4, 'valve_2'],
          [22, conn4, 'valve_3'],
          [24, conn5, 'valve_1'],
          [26, conn5, 'valve_2'],
          [28, conn5, 'valve_3'],
          [30, conn6, 'valve_1'],
          [32, conn6, 'valve_2'],
          [34, conn6, 'valve_3'],
          [36, conn7, 'valve_1'],
          [38, conn7, 'valve_2'],
          [40, conn7, 'valve_3'],
          [42, conn8, 'valve_1'],
          [44, conn8, 'valve_2'],
          [46, conn8, 'valve_3'],
          [48, conn9, 'valve_1'],
          [50, conn9, 'valve_2'],
          [52, conn9, 'valve_3'],
          [54, conn10, 'valve_1'],
          [56, conn10, 'valve_2'],
          [58, conn10, 'valve_3'],
          [60, conn11, 'valve_1'],
          [62, conn11, 'valve_2'],
          [64, conn11, 'valve_3'],
          [66, conn12, 'valve_1'],
          [68, conn12, 'valve_2'],
          [70, conn12, 'valve_3'],
          [72, conn13, 'valve_1'],
          [74, conn13, 'valve_2'],
          [76, conn13, 'valve_3'],
          [78, conn14, 'valve_1'],
          [80, conn14, 'valve_2'],
          [82, conn14, 'valve_3'],
          [84, conn15, 'valve_1'],
          [86, conn15, 'valve_2'],
          [88, conn15, 'valve_3'],
          [90, conn16, 'valve_1'],
          [92, conn16, 'valve_2'],
          [94, conn16, 'valve_3'],
          [96, conn17, 'valve_1'],
          [98, conn17, 'valve_2'],
          [100, conn17, 'valve_3'],
          [102, conn18, 'valve_1'],
          [104, conn18, 'valve_2'],
          [106, conn18, 'valve_3'],
          [108, conn19, 'valve_1'],
          [110, conn19, 'valve_2'],
          [112, conn19, 'valve_3'],
          [114, conn20, 'valve_1'],
          [116, conn20, 'valve_2'],
          [118, conn20, 'valve_3'],
          [120, conn21, 'valve_1'],
          [122, conn21, 'valve_2'],
          [124, conn21, 'valve_3'],
          [126, conn22, 'valve_1'],
          [128, conn22, 'valve_2'],
          [130, conn22, 'valve_3'],
          [132, conn23, 'valve_1'],
          [134, conn23, 'valve_2'],
          [136, conn23, 'valve_3'],
          [138, conn24, 'valve_1'],
          [140, conn24, 'valve_2'],
          [142, conn24, 'valve_3'],
          [144, conn25, 'valve_1'],
          [146, conn25, 'valve_2'],
          [148, conn25, 'valve_3'],
          [150, conn26, 'valve_1'],
          [152, conn26, 'valve_2'],
          [154, conn26, 'valve_3'],
          [156, conn27, 'valve_1'],
          [158, conn27, 'valve_2'],
          [160, conn27, 'valve_3'],
          [162, conn28, 'valve_1'],
          [164, conn28, 'valve_2'],
          [166, conn28, 'valve_3'],
          [168, conn29, 'valve_1'],
          [170, conn29, 'valve_2'],
          [172, conn29, 'valve_3']]


def send_data(i, conn, valve):
    if i in sectors.keys():
        conn.send(str.encode(f'{valve}'+'_'+f'{sectors[i]}'))


while True:
    data = conn30.recv(70)
    i = int(data.decode('cp1251'))
        
    for j in valves:
        send_data(i+j[0], j[1], j[2])
