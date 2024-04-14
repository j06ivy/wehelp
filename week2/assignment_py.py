print("==task1==")

frdlocation = {
  "Leslie": "Xiaobitan",
  "Bob": "Ximen",
  "Mary": "Jingmei",
  "Copper": "Taipei Arena",
  "Vivian": "Xindian"
}

greenLine = [
  "Songshan", "Nanjing Sanmin", "Taipei Arena", "Nanjing Fuxing", "Songjiang Nanjing", "Zhongshan",
  "Beimen", "Ximen", "Xiaonanmen", "Chiang Kai-shek Memorial Hall", "Guting", "Taipower Building",
  "Gongguan", "Wanlong", "Jingmei", "Dapinglin", "Qizhang", "Xindian City Hall", "Xindian"
]

def findAndPrint(messages, currentStation):
    currentIndex = greenLine.index(currentStation)
    minDistance = float('inf')
    closestFriend = None

    for friend, station in frdlocation.items():
        stationIndex = None
        distance = None
        if station in greenLine:  # 檢查 station 是否在 greenLine 中
            if station == "Xiaobitan":
                stationIndex = greenLine.index(station)
                if currentStation == "Qizhang":
                    distance = 1
            else:
                stationIndex = greenLine.index(station)
                distance = abs(stationIndex - currentIndex)

            if distance is not None:
                if distance < minDistance:
                    minDistance = distance
                    closestFriend = friend

    if closestFriend is not None:
        print(f"{closestFriend}")

messages={
  "Bob": "I'm at Ximen MRT station.",
  "Mary": "I have a dㄋrink near Jingmei MRT station.",
  "Copper": "I just saw a concert at Taipei Arena.",
  "Leslie": "I'm at home near Xiaobitan station.",
  "Vivian": "I'm at Xindian station waiting for you."
}

findAndPrint(messages, "Wanlong") # print Mary
findAndPrint(messages, "Songshan") # print Copper
findAndPrint(messages, "Qizhang") # print Leslie
findAndPrint(messages, "Ximen") # print Bob
findAndPrint(messages, "Xindian City Hall") # print Vivian
findAndPrint(messages, "Dapinglin") # print Mary

print("==task2==")
def book(consultants, hour, duration, criteria):
    if criteria == "rate":
        consultants.sort(key=lambda x: x[criteria], reverse=True)
    elif criteria == "price":
        consultants.sort(key=lambda x: x[criteria])

    new_booking = {"hour": hour, "duration": duration}
    available = next((consultant for consultant in consultants if not consultant.get("bookings") or all(not (hour < booking["hour"] + booking["duration"] and hour + duration > booking["hour"]) for booking in consultant["bookings"])), None)

    if available:
        available.setdefault("bookings", []).append(new_booking)
        print(f"{available['name']}")
    else:
        print("No Service")

consultants = [
    {"name": "John", "rate": 4.5, "price": 1000},
    {"name": "Bob", "rate": 3, "price": 1200},
    {"name": "Jenny", "rate": 3.8, "price": 800}
]

book(consultants, 15, 1, "price")  # Jenny
book(consultants, 11, 2, "price")  # Jenny
book(consultants, 10, 2, "price")  # John
book(consultants, 20, 2, "rate")   # John
book(consultants, 11, 1, "rate")   # Bob
book(consultants, 11, 2, "rate")   # No Service
book(consultants, 14, 3, "price")  # John

print("==task3==")
def func(*data):
    name_data = list(data)
    middle_name_data = []

    for name in name_data:
        middle_name = ""
        if len(name) <= 3:
            middle_name = name[1]
        elif len(name) > 3:
            middle_name = name[2]
        middle_name_data.append(middle_name)
    unique_index = [i for i, char in enumerate(middle_name_data) if middle_name_data.count(char) == 1]

    if not unique_index:
        print("沒有")
    else:
        print(", ".join(name_data[i] for i in unique_index))

func("彭大牆", "陳王明雅", "吳明")  # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆")  # print 夏曼藍波安

print("==task4==")
def getNumber(index):
    number = 0
    arr = [0]
    for i in range(31):
        number += 4
        arr.append(number)
        number += 4
        arr.append(number)
        number -= 1
        arr.append(number)
    print(arr[index])

getNumber(1)  # print 4
getNumber(5)  # print 15
getNumber(10)  # print 25
getNumber(30)  # print 70


