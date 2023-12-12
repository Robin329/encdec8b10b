from encdec8b10b import EncDec8B10B
# Encode Data Byte
running_disp = 0
byte_to_enc = 0xBC
running_disp, encoded = EncDec8B10B.enc_8b10b(byte_to_enc, running_disp)
print(hex(encoded))

# Encode Control Byte
byte_to_enc = 0xfb # comma
ctrl = 1
running_disp, encoded = EncDec8B10B.enc_8b10b(byte_to_enc, running_disp, ctrl)
print(hex(encoded))

# Decode Data Byte
byte_to_dec = 0x5b
ctrl, decoded = EncDec8B10B.dec_8b10b(byte_to_dec)
print(hex(decoded))
# ctrl variable confirm that it was a data byte
print(ctrl)

# Decode Control Byte
print("-----------------------------")
byte_to_dec = 0x17c # comma encoded
ctrl, decoded = EncDec8B10B.dec_8b10b(byte_to_dec)
print(hex(decoded))
print("-----------------------------")
# ctrl variable confirm that it was a control byte
print(ctrl)

# Verbosity
running_disp = 0
byte_to_enc = 0xA0
running_disp, encoded = EncDec8B10B.enc_8b10b(byte_to_enc, running_disp, verbose=True)
ctrl, decoded = EncDec8B10B.dec_8b10b(encoded, verbose=True)

print("-----------------------------")
# Decode Control Byte
byte_to_dec = 0x21b
ctrl, decoded = EncDec8B10B.dec_8b10b(byte_to_dec)
print(hex(decoded))
byte_to_dec = 0x2bc
ctrl, decoded = EncDec8B10B.dec_8b10b(byte_to_dec)
print(hex(decoded))
byte_to_dec = 0x346
ctrl, decoded = EncDec8B10B.dec_8b10b(byte_to_dec)
print(hex(decoded))

print("-----------------------------")