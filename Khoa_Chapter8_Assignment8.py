#Khoa Duong
#Assignment 8
#Write a program for a teacher to inout how many sudent, their name and grades then display it in table format.

import csv

#Write the input in csv file.
def write_grades():
    num_student = int(input("Enter the number of students: "))

    
    #Open csv file to writing.
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['First name', 'Last name', 'Exam 1', 'Exam 2', 'Exam 3', 'Average'])


        #Collect student's data.
        for _ in range(num_student):
            
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")
            Exam_1 = int(input("Enter the first exam's grade: "))
            Exam_2 = int(input("Enter the second exam's grade: "))
            Exam_3 = int(input("Enter the third exam's grade: "))
            Average = round((Exam_1 + Exam_2 + Exam_3)/3, 2)


            #Write student data.
            writer.writerow([first_name, last_name, Exam_1, Exam_2, Exam_3, Average])
            
    print("Grade has been saved successfully to grades.csv.")


#Read and print out the data.
def main():
    write_grades()
    with open("grades.csv", "r") as file:
        reader = csv.reader(file)


        #Convert to list formatting.
        data = list(reader)


        #print table with format.
        print("\n{:<12} {:<12} {:<7} {:<7} {:<7} {:<7}".format(*data[0]))
        print("_"*50)


        #Print student records.
        for row in data[1:]:
            print("{:<12} {:<12} {:<7} {:<7} {:<7} {:<7}".format(*row))


if __name__ == "__main__":
    main()
