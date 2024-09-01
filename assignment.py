#!/usr/bin/python3

class CourseInformationLookup:
    def __init__(ctx):
        ctx.course_rooms = {
            'CSC101': '3004',
            'CSC102': '4501',
            'CSC103': '6755',
            'NET110': '1244',
            'COM241': '1411'
        }
        ctx.course_instructors = {
            'CSC101': 'Haynes',
            'CSC102': 'Alvarado',
            'CSC103': 'Rich',
            'NET110': 'Burke',
            'COM241': 'Lee'
        }
        ctx.course_times = {
            'CSC101': '8:00 a.m.',
            'CSC102': '9:00 a.m.',
            'CSC103': '10:00 a.m.',
            'NET110': '11:00 a.m.',
            'COM241': '1:00 p.m.'
        }

    def lookup_course(ctx, course_number):
        """Displays the course details for a given course number."""
        if course_number in ctx.course_rooms:
            print(f"Room Number: {ctx.course_rooms[course_number]}")
            print(f"Instructor: {ctx.course_instructors[course_number]}")
            print(f"Meeting Time: {ctx.course_times[course_number]}")
        else:
            print("Course number not found.")

def main():
    lookup = CourseInformationLookup()
    course_number = input("Enter a course number (e.g., CSC101): ")
    lookup.lookup_course(course_number)

if __name__ == "__main__":
    main()
