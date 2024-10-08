#!/usr/bin/env python3

#    data          version        reason
#  2023/12/12        1.0          initial



import argparse
import collections
import re
import sys
from encdec8b10b import EncDec8B10B


enc_dec_8b10b_version_major = 0
enc_dec_8b10b_version_minor = 1


def encode_8b10b_print(input):
        en_hex = hex(int(input, 16))
        en_oct = int(input, 16)
        en_binary = format(en_oct, '08b')

        # print(type(en_hex))

        ctrl, decoded = EncDec8B10B.enc_8b10b(en_oct, 0, ctrl=0)
        # print("--")
        # print(decoded)
        enr0_oct_post = int(decoded)
        enr0_hex_post = hex(decoded)

        ctrl, decoded = EncDec8B10B.enc_8b10b(en_oct, 1, ctrl=0)
        enr1_oct_post = int(decoded)
        enr1_hex_post = hex(enr1_oct_post)

        ctrl, decoded = EncDec8B10B.enc_8b10b(en_oct, 0, ctrl=1)
        enr2_oct_post = int(decoded)
        enr2_hex_post = hex(enr2_oct_post)

        ctrl, decoded = EncDec8B10B.enc_8b10b(en_oct, 1, ctrl=1)
        enr3_oct_post = int(decoded)
        enr3_hex_post = hex(enr3_oct_post)
        # print(en_hex)
        # print(en_oct)
        # print(en_binary)

        found_key_code = None
        found_ctrl_code = None
        for key, value in EncDec8B10B.k_code_map.items():
            # print(value)
            if int(value, 16) == en_oct:
                found_key_code = key
                # print(key)
                break  # 找到值后可以提前退出循环
        for key, value in EncDec8B10B.k_code_ctrl.items():
            if int(value, 16) == en_oct:
                found_ctrl_code = key
                # print(key)
                break  # 找到值后可以提前退出循环

        found_key_code_HGF = None
        found_key_code_EDCBA = None
        enc_ctrl_symbol_5b6b = None
        enc_ctrl_symbol_3b4b = None
        enc_bin_EDCBA = en_binary[-5:]
        enc_bin_HGF = en_binary[:-5]

        # print("enc_bin_EDCBA="+enc_bin_EDCBA)
        # print(enc_bin_HGF)
        for key, sub_dict in EncDec8B10B.code_5b6b_abcdei.items():
            if enc_bin_EDCBA == key:
                for sub_key, sub_value in sub_dict.items():
                    enc_ctrl_symbol_5b6b = sub_value
                    break
                found_key_code_EDCBA = key
                # print("---" + sub_key)
                break  # 找到值后可以提前退出循环
        # print('++++'+found_key_code_EDCBA)
        # print('++++'+enc_ctrl_symbol_5b6b)

        for key, sub_dict in EncDec8B10B.code_3b_4b_fghj.items():
            # print(sub_dict)
            if enc_bin_HGF == key:
                for sub_key, sub_value in sub_dict.items():
                        enc_ctrl_symbol_3b4b = sub_value
                        # print("---" + sub_value)
                        # print('----' + sub_key)
                        break  # 找到值后可以提前退出循环
                found_key_code_HGF = key
                break
        # print('++++'+found_key_code_HGF)
        # print('++++'+enc_ctrl_symbol_3b4b)
        enc_ctrl_code_result = enc_ctrl_symbol_3b4b.replace('x', enc_ctrl_symbol_5b6b[2:])
        print(" ___________________________________________________________________________________________________________________________")
        print("|                                                    Little Endian                                                |         |")
        print("|---------------------------------------------------------------------------------|---------------------|---------|---------|")
        print("|               input           |         RD=-1          |      RD=+1             |                     |         |         |")
        print("|---------------------------------------------------------------------------------|---------------------|---------|---------|")
        print("|                                    012345 6789         |   012345 6789          |                     |         |         |")
        print("| id | dec | hex |  HGF EDCBA   |    abcdei fghj |  hex  |   abcdei fghj  |  hex  | Control Link Symbol |  K-code |   Code  |")
        pre = (0 << 0)
        print("   {}   {}   {}   {}         {}    {}     {}     {}        '{}'              '{}' '{}".format(pre, en_oct,en_hex, format(en_oct, '08b'), format(enr0_oct_post, '010b')[::-1],enr0_hex_post , format(enr1_oct_post, '010b')[::-1], enr1_hex_post, found_ctrl_code, found_key_code, enc_ctrl_code_result))
        pre = (1 << 0)
        print("   {}   {}   {}   {}         {}    {}     {}     {}        '{}'              '{}' '{}".format(pre, en_oct,en_hex, format(en_oct, '08b'), format(enr2_oct_post, '010b')[::-1], enr2_hex_post, format(enr3_oct_post, '010b')[::-1], enr3_hex_post, found_ctrl_code, found_key_code, enc_ctrl_code_result))
        print()
        print(" ___________________________________________________________________________________________________________________________")
        print("|                                                    Big Endian                                                   |         |")
        print("|---------------------------------------------------------------------------------|---------------------|---------|---------|")
        print("|               input           |         RD=-1          |      RD=+1             |                     |         |         |")
        print("|---------------------------------------------------------------------------------|---------------------|---------|---------|")
        print("|                                    0123 456789         |   0123 456789          |                     |         |         |")
        print("| id | dec | hex |  HGF EDCBA   |    jhgf iedcba |  hex  |   jhgf iedcba  |  hex  | Control Link Symbol |  K-code |   Code  |")
        pre = (0 << 0)
        print("   {}   {}   {}   {}          {}     {}     {}       {}        '{}'             '{}' '{}".format(pre, en_oct,en_hex, format(en_oct, '08b'), format(enr0_oct_post, '010b'), hex(int(format(enr0_oct_post, '010b')[::-1], 2)) , format(enr1_oct_post, '010b'), hex(int(format(enr1_oct_post, '010b')[::-1], 2)), found_ctrl_code, found_key_code, enc_ctrl_code_result) )
        pre = (1 << 0)
        print("   {}   {}   {}   {}          {}     {}     {}       {}        '{}'             '{}' '{}".format(pre, en_oct,en_hex, format(en_oct, '08b'), format(enr2_oct_post, '010b'), hex(int(format(enr2_oct_post, '010b')[::-1], 2)) , format(enr3_oct_post, '010b'), hex(int(format(enr3_oct_post, '010b')[::-1], 2)), found_ctrl_code, found_key_code, enc_ctrl_code_result) )
        print("------------------------------------------------------------------------------------------------------------------")
        print()
        print()

def decode_8b10b_print(input):
        dec_hex = hex(int(input, 16))
        dec_oct = int(input, 16)
        dec_binary = format(dec_oct, '010b')
        # print(dec_binary)
        # dec_abcdei = dec_binary[:-4]
        # print(dec_abcdei)
        dec_hex_reverse = hex(int(format(dec_oct, '010b')[::-1], 2))
        dec_dec_reverse = int(dec_hex_reverse, 16)
        dec_bin_reverse = format(dec_dec_reverse, '010b')

        # print("dec_bin_reverse = "+dec_bin_reverse)
        dec_bin_abcdei = dec_bin_reverse[:-4]
        dec_bin_fghj = dec_bin_reverse[-4:]
        # print(dec_bin_abcdei)

        found_key_code_HGF = None
        found_key_code_EDCBA = None
        dec_ctrl_symbol_5b6b = None
        dec_ctrl_symbol_3b4b = None
        # print(dec_bin_fghj)
        for key, sub_dict in EncDec8B10B.code_5b6b_abcdei.items():
            for sub_key, sub_value in sub_dict.items():
                if str(dec_bin_abcdei) in sub_key:
                    found_key_code_EDCBA = sub_value
                    # print("---" + sub_value)
                    # print("---" + sub_key)
                    break  # 找到值后可以提前退出循环
            if found_key_code_EDCBA:
                break
        # print('++++'+key)
        dec_ctrl_symbol_5b6b = sub_value
        dec_EDCBA = key
        for key, sub_dict in EncDec8B10B.code_3b_4b_fghj.items():
            # print(sub_dict)
            for sub_key, sub_value in sub_dict.items():
                if str(dec_bin_fghj) in sub_key:
                    found_key_code_HGF = sub_value
                    # print("---" + sub_value)
                    # print('----' + sub_key)
                    break  # 找到值后可以提前退出循环
            if found_key_code_HGF:
                break
        # print('++++'+key)
        dec_ctrl_symbol_3b4b = sub_value
        dec_HGF = key

        dec_bin_result = dec_HGF + dec_EDCBA
        dec_hex_result = hex(int(dec_bin_result, 2))
        dec_dec_result = int(dec_bin_result, 2)

        # print(dec_bin_result)
        # print(dec_hex_result)

        dec_symbol_result = dec_ctrl_symbol_3b4b.replace('x', dec_ctrl_symbol_5b6b[2:])
        # print(dec_symbol_result)

        dec_hex_post = 0
        dec_oct_post = 0
        # ctrl, decoded = EncDec8B10B.dec_8b10b(dec_oct)
        # # print("--")
        # # print(decoded)
        # dec_oct_post = int(decoded)
        # dec_hex_post = hex(decoded)

        # ctrl, decoded = EncDec8B10B.dec_8b10b(dec_dec_reverse)
        # # print("--")
        # # print(decoded)
        # dec_reverse_oct_post = int(decoded)
        # dec_reverse_hex_post = hex(decoded)


        found_key_code = None
        found_ctrl_code = None
        for key, value in EncDec8B10B.k_code_map.items():
            # print(value)
            if int(value, 16) == int(dec_hex_result, 16):
                found_key_code = key
                # print(key)
                break  # 找到值后可以提前退出循环
        for key, value in EncDec8B10B.k_code_ctrl.items():
            if int(value, 16) == int(dec_hex_result, 16):
                found_ctrl_code = key
                # print(key)
                break  # 找到值后可以提前退出循环
        # print(found_ctrl_code)
        print(" ___________________________________________________________________________________________________________________________")
        print("|              input             |                     output                     |                     |         |         |")
        print("|---------------------------------------------------------------------------------|---------------------|---------|---------|")
        print("|                  012345 6789   |         |         |         765 43210          |                     |         |         |")
        print("|  hex  |  dec |   abcdei fghj   |   dec   |    hex  |         HGF EDCBA          | Control Link Symbol |  K-code |   Code  |")
        print("   {}    {}      {}        {}       {}            {}                    '{}'           '{}'  '{}".format(dec_hex, dec_oct, format(dec_oct, '010b')[::-1], dec_dec_result, dec_hex_result, dec_bin_result,found_ctrl_code, found_key_code, dec_symbol_result))
        print()
        print()
def main():
    arg_parser = argparse.ArgumentParser(description='Parse 8b10b')
    arg_parser.add_argument(
        '-v', "--version", help='encode 8b10b version check. [enc_dec_8b10b.py -v]', action='store_true', default=None)
    arg_parser.add_argument(
        '-e', "--encode", help='encode 8b10b. [enc_dec_8b10b.py -e 0xFB]', default=None)
    arg_parser.add_argument(
        '-d', "--decode", help='decode 8b10b. [enc_dec_8b10b.py -d 0x368]', default=None)
    arg_parser.add_argument(
        '-r', "--run", help='8b10b running Disparity. [enc_dec_8b10b.py -d 0x368 -r 0/1]', default=None)
    arg_parser.add_argument('-c', "--ctrl", help='Control symbol. [enc_dec_8b10b.py -c SS]', default=None)
    arg_parser.add_argument('-p', "--print", help='print usage info. [enc_dec_8b10b.py -p]', action='store_true', default=False)
    args = arg_parser.parse_args()

    if args.version:
        print("Version " + str(enc_dec_8b10b_version_major) + "." + str(enc_dec_8b10b_version_minor))

    if args.print:
        # for key, value0 in EncDec8B10B.k_code_map.items():
        #     print(key)
        # for key, value1 in EncDec8B10B.k_code_ctrl.items():
        #     print(key)
        print("          Input                          RD = −1            RD = +1")
        print(" Symbol  DEC    HEX   HGF EDCBA        abcdei fghj        abcdei fghj")
        print(" K.28.0  28     1C    000 11100        001111 0100        110000 1011")
        print(" K.28.1  60     3C    001 11100        001111 1001        110000 0110")
        print(" K.28.2  92     5C    010 11100        001111 0101        110000 1010")
        print(" K.28.3  124    7C    011 11100        001111 0011        110000 1100")
        print(" K.28.4  156    9C    100 11100        001111 0010        110000 1101")
        print(" K.28.5  188    BC    101 11100        001111 1010        110000 0101")
        print(" K.28.6  220    DC    110 11100        001111 0110        110000 1001")
        print(" K.28.7  252    FC    111 11100        001111 1000        110000 0111")
        print(" K.23.7  247    F7    111 10111        111010 1000        000101 0111")
        print(" K.27.7  251    FB    111 11011        110110 1000        001001 0111")
        print(" K.29.7  253    FD    111 11101        101110 1000        010001 0111")
        print(" K.30.7  254    FE    111 11110        011110 1000        100001 0111")

    run_disp = 0
    if args.run:
        run_disp = int(args.run)
    if args.encode:
        # print(args.encode)
        # print(hex(int(args.encode, 16)))
        encode_8b10b_print(args.encode)

    if args.decode:
        decode_8b10b_print(args.decode)

    if args.ctrl:
        input_key = args.ctrl
        found_key_code = None
        found_ctrl_code = None
        # for key, value in EncDec8B10B.k_code_map.items():
        #     print(value)
        #     if key == input_key:
        #         found_key_code = key
        #         # print(key)
        #         break  # 找到值后可以提前退出循环
        for key, value in EncDec8B10B.k_code_ctrl.items():
            if key == input_key:
                found_ctrl_code = key
                # print(key)
                # print(value)
                encode_8b10b_print(value)
                break  # 找到值后可以提前退出循环

if __name__ == '__main__':
    main()
