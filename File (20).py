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
      "5\n",
      "7\n",
      "12\n"
     ]
    }
   ],
   "source": [
    "a=int(input())\n",
    "b=int(input())\n",
    "c=a+b\n",
    "print(c)"
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
      "7\n",
      "true\n",
      "8\n"
     ]
    }
   ],
   "source": [
    "a=int(input())\n",
    "b=bool(input())\n",
    "c=a+b\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "5\n",
      "8\n",
      "11\n"
     ]
    }
   ],
   "source": [
    "i=2\n",
    "Data=['IU','Iqra','Karachi','pk']\n",
    "for a in Data :\n",
    "    print(i)\n",
    "    i+=3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "for x in range (6):\n",
    "    print (x)"
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
      "5\n",
      "7\n",
      "(12+0j)\n"
     ]
    }
   ],
   "source": [
    "a=int(input())\n",
    "b=complex(input())\n",
    "c=a+b\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "5\n",
      "7\n"
     ]
    }
   ],
   "source": [
    "#third number is the difference\n",
    "for x in range(3,9,2):\n",
    "    print (x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15\n",
      "13\n",
      "11\n",
      "9\n",
      "7\n",
      "5\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "for x in range(15,1,-2):\n",
    "    print (x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "for x in range(5):\n",
    "    continue"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "loop ends\n"
     ]
    }
   ],
   "source": [
    "for i in range(10):\n",
    "    print(i)\n",
    "else:\n",
    "    print('loop ends')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#+\n",
    "#-\n",
    "#*\n",
    "#** power\n",
    "#%\n",
    "#/\n",
    "#// ceiling ya floor k lie\n",
    "\n",
    "x=int(input())\n",
    "y=int(input())\n",
    "a=x+y; print(a)\n",
    "b=x-y; print(b)\n",
    "c=x*y; print(c)\n",
    "d=x/y; print(d)\n",
    "e=x**y; print(e)\n",
    "f=x//y; print(f)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "data= ['A','B','','D']\n",
    "for d in data:\n",
    "    if d=='A':\n",
    "        print('1st')\n",
    "    elif d=='B':\n",
    "        print('2nd')\n",
    "    elif d=='C':\n",
    "        print('3rd')\n",
    "    else:\n",
    "        print('no data')\n",
    "\n"
   ]
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
