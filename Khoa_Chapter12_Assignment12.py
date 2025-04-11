#Khoa Duong
#Assignment 12
#Write a program that analyzes student's grade.

import numpy as n
#Open, load, and return grade datas.
def load_grades(grades_file):
    return n.genfromtxt(grades_file, delimiter=',', skip_header=1, usecols=(2, 3, 4))

#Calculate and print exam's stats.
def exam_stats(data):
    num_exams = data.shape[1]
    print('Statistics per exam:')
    for i in range(num_exams):
        exam = data[:, i]
        print(f'\nExam {i + 1}:')
        print(f'Mean: {n.mean(exam):.2f}')
        print(f'Median: {n.median(exam):.2f}')
        print(f'Standard Deviation: {n.std(exam):.2f}')
        print(f'Min: {n.min(exam)}')
        print(f'Max: {n.max(exam)}')

        #Pass or fail count.
        passed = n.sum(exam >= 60)
        failed = n.sum(exam < 60)
        print(f'Passed: {passed}')
        print(f'Failed: {failed}')

#Main function to analysis date.
def main():
    grades_file = 'grades.csv'
    data = load_grades(grades_file)
    print('Grades:\n', data[:10])
    exam_stats(data)

    #Overall statistics.
    final_grades = data.flatten()
    print('\nOverall Statistics:')
    print(f'Mean: {n.mean(final_grades):.2f}')
    print(f'Median: {n.median(final_grades):.2f}')
    print(f'Std Dev: {n.std(final_grades):.2f}')
    print(f'Min: {n.min(final_grades)}')
    print(f'Max: {n.max(final_grades)}')

    total_grades = len(final_grades)
    total_passed = n.sum(final_grades >= 60)
    pass_percent = (total_passed / total_grades) * 100
    print(f'Overall Passing Percentage: {pass_percent:.2f}%')

if __name__ == '__main__':
    main()
