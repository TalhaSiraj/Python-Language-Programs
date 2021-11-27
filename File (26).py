{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape=  (3, 3, 3)\n",
      "\n",
      "Change=\n",
      " 400\n",
      "\n",
      "Slicing=\n",
      " [[[ 21  22 400]]\n",
      "\n",
      " [[ 51  52 400]]]\n",
      "\n",
      "Less Then 50=\n",
      " [11 12 13 21 22 31 32 41 42 43]\n",
      "\n",
      "Array=\n",
      " [[[ 11  12  13]\n",
      "  [ 21  22 400]\n",
      "  [ 31  32 400]]\n",
      "\n",
      " [[ 41  42  43]\n",
      "  [ 51  52 400]\n",
      "  [ 61  62 400]]\n",
      "\n",
      " [[ 71  72  73]\n",
      "  [ 81  82 400]\n",
      "  [ 91  92 400]]]\n"
     ]
    }
   ],
   "source": [
    "Apgt= np.array(\n",
    "              [\n",
    "               [\n",
    "                [11,12,13],\n",
    "                [21,22,23],\n",
    "                [31,32,33]\n",
    "               ],\n",
    "               [   \n",
    "                [41,42,43],\n",
    "                [51,52,53],\n",
    "                [61,62,63]\n",
    "               ],\n",
    "               [\n",
    "                [71,72,73],\n",
    "                [81,82,83],\n",
    "                [91,92,93]\n",
    "               ]\n",
    "              ]\n",
    "             )\n",
    "print(\"Shape= \", Arr.shape)\n",
    "bps=Apgt[:,1:,2]= 400\n",
    "print(\"\\nChange=\\n\", bps)\n",
    "print(\"\\nSlicing=\\n\", Apgt[:2, 1:2])\n",
    "print(\"\\nLess Then 50=\\n\", Apgt[Apgt<50])\n",
    "print(\"\\nArray=\\n\", Apgt)"
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
      "(4, 4, 3, 2, 4)\n",
      "0.0\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "Ars= np.zeros([4,4,3,2,4])\n",
    "print(Ars.shape)\n",
    "print(Ars[3,3,0,1,2])"
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
