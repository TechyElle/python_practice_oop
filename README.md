# Python OOP Practice (Final Exam)

Quick programs written in a style you can reproduce on paper in under a minute.

## Style rules used here
- Class-based (OOP integrated)
- Short, direct code
- Snake_case variable names
- No single-letter variables
- Short human comments when needed
- For file resources: call `.close()` (when applicable)

## How to run
Example:
```bash
python final_exam/arithmetic_and_loops/add_two_numbers_and_display.py
```

# To Study

These files are short OOP practice programs for the close-notes practical exam.

Keep the current working directory as `.` when running them.

Use snake case for variables.

Use all lowercase variable names.

Do not use single-letter variable names.

Close the input file with `.close()`.

Each program follows the same fast pattern:

Make a class for the program.

Write one `run()` method.

Create the needed variables inside `run()`.

Open input with `open(0)`.

Collect numbers.

Solve the problem.

Print the answer.

Close the input file at the end of `run()`.

Create the object at the bottom.

Call `.run()` on the object.

For programs that collect ten numbers:

Use `for count in range(10)`.

Read the number with `int(self.input_file.readline())`.

Append each number to `self.numbers`.

For programs that collect until the user stops:

Use `while True`.

Read one line from `self.input_file.readline()`.

Break if the line is empty.

Use `try` and `except ValueError`.

Break when the input is not a number.

Study target:

Write the class.

Write `run()`.

Write the variables.

Write the loop.

Write the condition.

Print the answer.

Close the input file.

Make the object and run it.

