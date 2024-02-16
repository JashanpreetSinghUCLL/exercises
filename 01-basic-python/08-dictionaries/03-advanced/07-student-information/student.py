
def process_data(string_data):
    students = {}
    for item in string_data:
        name, age, *courses = item.split(",")
        students[name] = {"age": int(age), "courses": courses}
    return students
# print(process_data(['John Smith,20,Math,Physics', 'Jane Doe,21,Biology,Chemistry,Math']))

def average_age(data):
    sum = 0
    num_of_students = 0 
    for student in data.values():
        sum += student["age"]
        num_of_students += 1
    return sum / num_of_students

# print(average_age(process_data(['John Smith,20,Math,Physics', 'Jane Doe,21,Biology,Chemistry,Math'])))

def courses(data):
    courses = set()
    for student in data.values():
        courses.update(student["courses"])
    return courses

# print(courses(process_data(['John Smith,20,Math,Physics', 'Jane Doe,21,Biology,Chemistry,Math'])))

def most_common_courses(data):
    courses_with_count = {}
    for student in data.values():
        for course in student["courses"]:
            if course not in courses_with_count:
                courses_with_count[course] = 0
            courses_with_count[course] += 1
    max_count = max(courses_with_count.values())
    return {course for course in courses_with_count.keys() if courses_with_count[course] == max_count}

print(most_common_courses(process_data(['John Smith,20,Math,Physics', 'Jane Doe,21,Biology,Chemistry,Math'])))
