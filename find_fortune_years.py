from lunardate import LunarDate

haircut_dict = {
    1: "受福", 2: "官事", 3: "欢喜", 4: "富贵", 5: "面黑",
    6: "神通", 7: "康宁", 8: "寿长", 9: "闻法", 10: "记别",
    11: "眼明", 12: "困苦", 13: "少白", 14: "神定", 15: "大吉",
    16: "利益", 17: "多病", 18: "犯盗", 19: "悟道", 20: "祸崇",
    21: "患难", 22: "受惧", 23: "多闻", 24: "证果", 25: "斗争",
    26: "祥瑞", 27: "疮癣", 28: "受冤", 29: "长慧", 30: "如意"
}

def find_years_for_fortune(fortune):
    jan_1_years = []
    dec_31_years = []
    for year in range(1999, 2200):
        jan_1_lunar_day = LunarDate.fromSolarDate(year, 1, 1).day
        dec_31_lunar_day = LunarDate.fromSolarDate(year, 12, 31).day

        jan_1_fortune = haircut_dict.get(jan_1_lunar_day, "无法确定")
        dec_31_fortune = haircut_dict.get(dec_31_lunar_day, "无法确定")

        if jan_1_fortune == fortune:
            jan_1_years.append(year)
        if dec_31_fortune == fortune:
            dec_31_years.append(year)

    return jan_1_years, dec_31_years

# 输入一个吉凶标记并查找匹配的年份
input_fortune = input("请输入一个吉凶标记: ")
jan_1_years, dec_31_years = find_years_for_fortune(input_fortune)

# 分别输出1月1日和12月31日对应的年份
print(f"从1999年到2199年间，1月1日对应‘{input_fortune}’的年份有：{', '.join(map(str, jan_1_years))}" if jan_1_years else "没有找到任何年份在1月1日对应该吉凶标记。")
print(f"从1999年到2199年间，12月31日对应‘{input_fortune}’的年份有：{', '.join(map(str, dec_31_years))}" if dec_31_years else "没有找到任何年份在12月31日对应该吉凶标记。")
