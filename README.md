# Assignment 7
## Course Information Lookup

This simple Python program allows users to retrieve details about specific courses, including room numbers, instructors, and meeting times, using a console-based interface.

### Usage Instructions

1. **Prepare the Script**:
   - Ensure that the first line of the script points to the correct path for Python 3 on your system. If `/usr/bin/python3` is not the correct path, change it to the path where Python 3 is installed, which might be `/usr/local/bin/python3` or another location depending on your setup.

2. **Make the Script Executable**:
   - Before running the script, you need to make it executable. Open a terminal and navigate to the directory containing `assignment.py`.
   - Run the following command to make the script executable:
     ```
     chmod +x assignment.py
     ```

3. **Running the Script**:
   - Once the script is executable, you can run it directly from the terminal by typing:
     ```
     ./assignment.py
     ```
   - Follow the on-screen prompts to enter a course number and retrieve course information.

### How to Use the `CourseInformationLookup` Class

If you wish to use the `CourseInformationLookup` class in another Python script:

- Import the class from `assignment.py`:
  ```python
  from assignment import CourseInformationLookup
  ```
- Create an instance of `CourseInformationLookup`:
  ```python
  course_lookup = CourseInformationLookup()
  ```
- Use the `lookup_course` method to get details about a course:
  ```python
  course_number = 'CSC101'
  course_lookup.lookup_course(course_number)
  ```

This approach allows you to incorporate course information lookup functionalities into broader Python applications or scripts.

### Concept

The program leverages Python dictionaries to map course numbers to their respective room numbers, instructors, and meeting times. This data structure allows for efficient lookups of course details, making it an ideal choice for applications where quick retrieval of information based on a key (in this case, the course number) is necessary.

### Features

- **Lookup Room Numbers:** Find out where each course is held.
- **Find Instructors:** Get the name of the instructor teaching each course.
- **Check Meeting Times:** Know the schedule for each course to plan your day accordingly.

### How It Works

The program defines three dictionaries:
1. `course_rooms`: Maps course numbers to room numbers.
2. `course_instructors`: Maps course numbers to instructor names.
3. `course_times`: Maps course numbers to meeting times.

When a user inputs a course number, the program checks if this number exists in the dictionaries. If it does, the program prints the relevant room number, instructor, and meeting time. If not, it notifies the user that the course number was not found.

### Usage

To use the program, run it in a Python environment, input a course number when prompted, and view the displayed information.

Example:
```
Enter a course number (e.g., CSC101): CSC101
Room Number: 3004
Instructor: Haynes
Meeting Time: 8:00 a.m.
```

### Algorithm Considerations

The program utilizes basic operations of Python dictionaries, highlighting the efficiency of lookups, which are generally O(1) on average. This means that regardless of how many items are in the dictionary, looking up a key takes a constant amount of time. The decision to use dictionaries stems from the need for mapping unique identifiers (course numbers) to various attributes in a way that is quick and easy to maintain.

### Next Steps

#### Step 1: Persistence (Optional)
We need to convert the `dict` structures to persistent and retrievable data with a key:value store or database, consider Redis for this.

#### Step 2: User Input Interface
Provide a user-friendly interface for entering new course information. This interface should prompt the user for the course number, room number, instructor name, and meeting time. Ensure input validation is in place to check for correct formats and prevent erroneous data entry.

#### Step 3: Verification
Before adding a new course, verify whether the course already exists in the system to avoid duplicates. If the course is already present, inform the user and possibly offer to update the existing entry instead.

#### Step 4: Adding the Course
If the course does not exist, proceed to add the new course information to the respective dictionaries. This process involves appending new key-value pairs to each related dictionary:

- **Course-Room Dictionary:** Add the course number and its corresponding room number.
- **Course-Instructor Dictionary:** Add the course number and the assigned instructor's name.
- **Course-Time Dictionary:** Add the course number and its meeting time.

#### Step 5: Confirmation
After successfully adding the course, provide a confirmation message to the user. This reassures the user that the data has been correctly entered into the system.

