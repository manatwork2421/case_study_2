def count_passed(enrollments, course_name, pass_threshold=40):
    count=0
    for record in enrollments:
        if record['course'] == course_name and record['marks'] >= pass_threshold:
            count += 1
    return count
        