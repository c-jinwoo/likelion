information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
foods = ["된장찌개", "피자", "제육볶음"]

print(information.get("취미"))

information["특기"] = "피아노"
information["사는곳"] = "서울"

# dict 요소 제거
del information["좋아하는 음식"]

print(information)

# dict 길이
print(len(information))

# dict 제거
information.clear()
print(information)

# 역순
print(foods[-1])

# list 추가
foods.append("김밥")
print(foods)

# list 제거
del foods[1]
print(foods)
