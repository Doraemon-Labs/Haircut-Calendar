from lunardate import LunarDate

haircut_dict = {
    1: "受福", 2: "官事", 3: "欢喜", 4: "富贵", 5: "面黑",
    6: "神通", 7: "康宁", 8: "寿长", 9: "闻法", 10: "记别",
    11: "眼明", 12: "困苦", 13: "少白", 14: "神定", 15: "大吉",
    16: "利益", 17: "多病", 18: "犯盗", 19: "悟道", 20: "祸崇",
    21: "患难", 22: "受惧", 23: "多闻", 24: "证果", 25: "斗争",
    26: "祥瑞", 27: "疮癣", 28: "受冤", 29: "长慧", 30: "如意"
}

def get_fortune_by_date(year, month, day):
    lunar_date = LunarDate.fromSolarDate(year, month, day)
    lunar_day = lunar_date.day
    fortune = haircut_dict.get(lunar_day, "无法确定")
    return fortune

# 获取用户输入的日期
input_date = input("请输入一个日期（格式为YYYY-MM-DD）: ")
year, month, day = map(int, input_date.split('-'))

# 根据输入的日期获取吉凶标记
fortune = get_fortune_by_date(year, month, day)
print(f"{year}年{month}月{day}日的吉凶标记是：{fortune}")
