{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this : 3\n",
      "is : 3\n",
      "the : 1\n",
      "new : 1\n",
      "way : 1\n",
      "of : 1\n",
      "teaching : 1\n",
      "good : 1\n",
      "option : 1\n",
      "great : 1\n"
     ]
    }
   ],
   "source": [
    "#Bismillahirrahmanirrahim\n",
    "\n",
    "file = open(\"My File.txt\",\"r\") \n",
    "dic  = dict() \n",
    "for i in file: \n",
    "    i     = i.strip() \n",
    "    i     = i.lower()\n",
    "    i = i.translate(i.maketrans(\"\", \"\", string.punctuation)) \n",
    "    words = i.split(\" \") \n",
    "    for j in words:  \n",
    "        if j in dic: \n",
    "            dic[j] = dic[j]+1\n",
    "        else: \n",
    "            dic[j]=1\n",
    "    for key in list(dic.keys()): \n",
    "        print(key,\":\",dic[key]) "
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
