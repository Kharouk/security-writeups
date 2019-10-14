from sys import argv
import codecs
string = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"

ary = argv[1:]

stringified = "".join(ary)
answer = codecs.encode(stringified, 'rot_13')

print("".join(answer))
