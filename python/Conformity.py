def main():
    n = int(input())
    
    course_combination = {}
    for i in range(n):
        courses = tuple(sorted(tuple(int(x) for x in input().split())))
        course_combination[courses] = course_combination.get(courses, 0) + 1
    
    most_popular = max(course_combination.values())
    count = 0
    for num_of_students in course_combination.values():
        if num_of_students == most_popular:
            count += num_of_students 

    print(count) 


if __name__ == '__main__':
    main()
