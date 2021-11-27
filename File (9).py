{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "print(\"Welcome To Marksheet Program\")\n",
    "print()\n",
    "name = input(\"Enter Name: \")\n",
    "roll = input(\"Enter Roll Number: \")\n",
    "semester = input(\"Enter Semester: \")\n",
    "\n",
    "programing  = float(input(\"Enter Programing Marks        = \"))\n",
    "calculus    = float(input(\"Enter Calculus Marks          = \"))\n",
    "english     = float(input(\"Enter English Marks           = \"))\n",
    "computer    = float(input(\"Enter Computer Marks          = \"))\n",
    "pst         = float(input(\"Enter Pakistan Studies Marks  = \"))\n",
    "electronics = float(input(\"Enter Electronics Marks       = \"))\n",
    "\n",
    "total       = 600\n",
    "print(\"\\n\\nYour Result Has Been Saved In The My Marksheet File.\" )\n",
    "obtained    = programing + calculus + english + computer + pst + electronics\n",
    "grade       = ''\n",
    "userGrade = ''\n",
    "percentage = float((obtained / total) * 100)\n",
    "\n",
    "if(percentage>=88):\n",
    "    grade='A+'\n",
    "elif(percentage>=80 and percentage<88):\n",
    "    grade='A'\n",
    "elif(percentage>=74 and percentage<80):\n",
    "    grade='B'\n",
    "elif(percentage>=60 and percentage<74):\n",
    "    grade='C'\n",
    "else:\n",
    "    grade='F'\n",
    "\n",
    "data_set = [name, roll, semester, programing, calculus, english, computer, pst, electronics, obtained, total, round(float(percentage),2), grade]\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
