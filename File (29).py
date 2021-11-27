{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Atlanta', 'Baltimore', 'Chicago', 'Denver', 'Los Angeles', 'Seattle']\n"
     ]
    }
   ],
   "source": [
    "cities = [\"Atlanta\", \"Baltimore\", \"Chicago\", \"Denver\", \"Los Angeles\", \"Seattle\"]\n",
    "print(cities)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your Marksheet:-\n",
      "\n",
      "English     = 78\n",
      "Math        = 89\n",
      "Computer    = 54\n",
      "Pst         = 82\n",
      "Programing  = 98\n",
      "\n",
      "Total       = 401\n",
      "Precetage   = 80.2\n",
      "Grade       = A\n"
     ]
    }
   ],
   "source": [
    "Sub = (\"English\", \"Math\", \"Computer\", \"Pst\", \"Programing\")\n",
    "Marks = (78,89,54,82,98)\n",
    "print(\"Your Marksheet:-\\n\")\n",
    "print(Sub[0], \"    =\", Marks[0])\n",
    "print(Sub[1], \"       =\", Marks[1])\n",
    "print(Sub[2], \"   =\", Marks[2])\n",
    "print(Sub[3], \"        =\", Marks[3])\n",
    "print(Sub[4], \" =\", Marks[4])\n",
    "Total= Marks[0]+Marks[1]+Marks[2]+Marks[3]+Marks[4]\n",
    "print(\"\\nTotal       =\",Total)\n",
    "Per = Total/5\n",
    "print(\"Precetage   =\",Per)\n",
    "if Per >=88:\n",
    "    print(\"Grade       = A+\") \n",
    "elif Per >=80:\n",
    "    print(\"Grade       = A\")\n",
    "elif Per >=74:\n",
    "    print(\"Grade       = B\") \n",
    "elif Per >=60:\n",
    "    print(\"Grade       = C\") \n",
    "elif Per <60:\n",
    "    print(\"You Failed\")    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
