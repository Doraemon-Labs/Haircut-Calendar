from lunardate import LunarDate
import datetime

haircut_dict = {
    1: "受福", 2: "官事", 3: "欢喜", 4: "富贵", 5: "面黑",
    6: "神通", 7: "康宁", 8: "寿长", 9: "闻法", 10: "记别",
    11: "眼明", 12: "困苦", 13: "少白", 14: "神定", 15: "大吉",
    16: "利益", 17: "多病", 18: "犯盗", 19: "悟道", 20: "祸崇",
    21: "患难", 22: "受惧", 23: "多闻", 24: "证果", 25: "斗争",
    26: "祥瑞", 27: "疮癣", 28: "受冤", 29: "长慧", 30: "如意"
}

def convert_solar_to_lunar(year, month, day):
    lunar_date = LunarDate.fromSolarDate(year, month, day)
    return lunar_date.day

def generate_ics_for_range(start_year, end_year):
    ics_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//YourOrg//Haircut Calendar//EN\n"
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            start_date = datetime.date(year, month, 1)
            one_day = datetime.timedelta(days=1)
            current_date = start_date
            while current_date.month == month:
                lunar_day = convert_solar_to_lunar(current_date.year, current_date.month, current_date.day)
                fortune = haircut_dict.get(lunar_day, "无法确定")
                event_date = current_date.strftime('%Y%m%d')
                ics_content += f"BEGIN:VEVENT\nUID:{event_date}@yourdomain.com\nDTSTAMP:{event_date}T000000Z\nDTSTART;VALUE=DATE:{event_date}\nSUMMARY:{fortune}\nDESCRIPTION:\nEND:VEVENT\n"
                current_date += one_day
    ics_content += "END:VCALENDAR"
    return ics_content

# 从这里开始手动输入起止年份
start_year = int(input("请输入起始年份: "))
end_year = int(input("请输入结束年份: "))

# 生成ICS文件
ics_data = generate_ics_for_range(start_year, end_year)

# 将ICS数据写入文件
file_name = f"haircut_calendar_{start_year}_to_{end_year}.ics"
with open(file_name, "w") as file:
    file.write(ics_data)

print(f"ICS日历文件 {file_name} 已生成。")
