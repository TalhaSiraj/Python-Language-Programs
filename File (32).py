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
      "Enter Value Of X: 3\n",
      "Enter Value Of y: 5\n",
      "[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]\n"
     ]
    }
   ],
   "source": [
    "x = int(input(\"Enter Value Of X: \"))\n",
    "y = int(input(\"Enter Value Of y: \"))\n",
    "alist = [[0 for b in range(y)] for a in range(x)]\n",
    "for a in range(x):\n",
    "    for b in range(y):\n",
    "        alist[a][b]= a*b\n",
    "print(alist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter First Name: Talha\n",
      "Enter Last Name: Siraj\n",
      "Enter Age: 20\n",
      "Enter Roll Number: 74725\n",
      "Enter Score: 90\n",
      "Continue: No\n",
      "\n",
      " [('Talha', 'Siraj', '20', '74725', '90')]\n"
     ]
    }
   ],
   "source": [
    "student=[]\n",
    "while True:\n",
    "    fname = input(\"Enter First Name: \")\n",
    "    lname = input(\"Enter Last Name: \")\n",
    "    age = input(\"Enter Age: \")\n",
    "    roll = input(\"Enter Roll Number: \")\n",
    "    score = input(\"Enter Score: \")\n",
    "    student.append((fname, lname, age, roll, score))\n",
    "    cont =input(\"Continue: \")\n",
    "    if(cont!='Y'):\n",
    "        break   \n",
    "print(\"\\n\",student) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "initial_dictionary {'a': 1, 'b': 2, 'c': 3, 'd': 2}\n",
      "duplicate values [2]\n"
     ]
    }
   ],
   "source": [
    "ini_dict = {'a':1, 'b':2, 'c':3, 'd':2} \n",
    "print(\"initial_dictionary\", str(ini_dict)) \n",
    "rev_dict = {}  \n",
    "for key, value in ini_dict.items(): \n",
    "    rev_dict.setdefault(value, set()).add(key)       \n",
    "result = [key for key, values in rev_dict.items() \n",
    "                              if len(values) > 1] \n",
    "print(\"duplicate values\", str(result)) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 : 5\n",
      "2 : 8\n"
     ]
    }
   ],
   "source": [
    "values = \"1,1,1,1,1,2,2,2,2,2,2,2,2\"\n",
    "vlist = values.split(\",\")\n",
    "dct={}\n",
    "for v in vlist:\n",
    "    v=v.strip()\n",
    "    if v in dct:\n",
    "        dct[v] += 1\n",
    "    else:\n",
    "        dct[v] = 1\n",
    "for item, values in dct.items():\n",
    "    print(item,\":\",values)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Counter({'2': 8, '1': 5})\n",
      "1 5\n",
      "2 8\n"
     ]
    }
   ],
   "source": [
    "from collections import Counter\n",
    "xct = Counter(vlist)\n",
    "print(xct)\n",
    "for items, values in xct.items():\n",
    "    print(items,values)"
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
