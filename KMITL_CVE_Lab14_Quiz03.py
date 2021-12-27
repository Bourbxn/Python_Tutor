postcodes = (
    (("Nonthaburi", "MueangNonthaburi"), "11000"),
    (("Nonthaburi", "BangKruai"), "11130"),
    (("Nonthaburi", "BangYai"), "11140"),
    (("Nonthaburi", "BangBuaThong"), "11110"),
    (("Nonthaburi", "SaiNoi"), "11150"),
    (("Nonthaburi", "PakKret"), "11120"),
    (("SamutPrakan", "MuengSamutPrakan"), ("10270", "10280")),
    (("SamutPrakan", "BangBo"), ("10550", "10560")),
    (("SamutPrakan", "BangPhli"), "10540"),
    (("SamutPrakan", "PhraPradaeng"), "10130"),
    (("SamutPrakan", "PhraSamutChedi"), "10290"),
    (("SamutPrakan", "BangSaoThong"), "10540"),
    (("Chachoengsao", "MueangChachoengsao"), "24000"),
    (("Chachoengsao", "BangKhla"), "24110"),
    (("Chachoengsao", "BangNamPriao"), ("24000", "24150", "24170")),
    (("Chachoengsao", "BangPakong"), ("24130", "24180")),
    (("Chachoengsao", "BanPho"), "24140"),
    (("Chachoengsao", "PhanomSarakham"), "24120"),
    (("Chachoengsao", "Ratchasan"), "24120"),
    (("Chachoengsao", "SanamChaiKhet"), "24160"),
    (("Chachoengsao", "PlaengYao"), "24190"),
    (("Chachoengsao", "ThaTakiap"), "24160"),
    (("Chachoengsao", "KhlongKhuean"), ("24000", "24110")),
)

text = input("Please enter a district name: ")
checkData = False
for i in range(len(postcodes)):
    if text == postcodes[i][0][1]:
        checkData = True
        print("Code(s): ", end="")
        print(postcodes[i][1])

if checkData == False:
    print("Information not found")
