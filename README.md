<p align="center">
  <img src="https://img.shields.io/badge/🏛️_OOP-Practical_Exam-10B981?style=for-the-badge&logoColor=white" alt="OOP Exam Badge" />
</p>

<h1 align="center">🧩 Python OOP Practice</h1>

<p align="center">
  <strong>Classes • One <code>run()</code> • Timed-exam friendly solutions</strong>
</p>

<p align="center">
  Short OOP scripts written in a consistent pattern—fast to reproduce during a timed practical exam.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Style_Rules-Snake_Case-2DD4BF?style=flat-square" alt="Style rules" />
  <img src="https://img.shields.io/badge/Exam_Pattern-stdin(open(0))-60A5FA?style=flat-square" alt="Exam pattern" />
  <img src="https://img.shields.io/badge/OOP-Exactly_1_run()-F59E0B?style=flat-square" alt="OOP" />
</p>

<p align="center">
  <a href="#-introduction">Introduction</a> •
  <a href="#-style-rules">Style Rules</a> •
  <a href="#-how-to-run">How to run</a> •
  <a href="#-exam-pattern">Exam pattern</a> •
  <a href="#-input-patterns">Input patterns</a> •
  <a href="#-educational-note">Educational note</a>
</p>

---

## 📌 Introduction

This repository contains short **Python OOP practice** scripts following a consistent structure—ideal for quick repetition during a practical exam.

---

## 🎨 Style rules

- Use a **class** (OOP style).
- Implement **exactly one** `run()` method.
- Use **snake_case** variable names.
- Avoid **single-letter** variable names.
- Keep comments short (only when needed).
- When working with file resources, call `.close()`.

---

## 🚀 How to run

From the repository root (`.`):

```bash
python final_exam/arithmetic_and_loops/add_two_numbers_and_display.py
```

---

## 🎯 Exam pattern (used by all scripts)

1. Create a class for the exercise.
2. Put all logic inside `run()`.
3. Read input from `open(0)` (stdin):
   - create `self.input_file = open(0)` (or equivalent)
4. Solve the problem (often by collecting values into a list).
5. Print the final answer.
6. Close input at the end of `run()`.
7. Instantiate the class at the bottom and call `.run()`.

---

### ⌨️ Input patterns

**Collect 10 numbers**
- Use `for count in range(10)`
- Read each number with: `int(self.input_file.readline())`
- Append into `self.numbers`

---

**Collect until the user stops**
- Use `while True`
- Read one line with `self.input_file.readline()`
- Break when the line is empty
- Use `try` / `except ValueError` to stop when the input is not a number

---

## ⚠️ Educational note

<div align="center">

*For educational purposes only. Created for the PUP Object-Oriented Programming course.*

</div>

