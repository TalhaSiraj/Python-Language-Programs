{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os.path\n",
    "import re\n",
    "import csv\n",
    "import json \n",
    "pizza = {} \n",
    "while True:\n",
    "    name = input(\"Enter The Pizza Type: \")\n",
    "    price = input(\"Enter The Prize of Pizza: \")\n",
    "    pizza.update([(name,price)])\n",
    "    quit =input(\"Wanna Quit Press Q: \")\n",
    "    if(quit=='Q'):\n",
    "        break\n",
    "\n",
    "if os.path.exists('Pizza Shop.json'):\n",
    "    print(\"The Jason File Exist\")\n",
    "    with open(\"Pizza Shop.json\", \"a+\") as f:\n",
    "        json.dump(pizza,f)\n",
    "else:\n",
    "    print(\"The Jason File Does Not Exist But We Created It New\")\n",
    "    with open(\"Pizza Shop.json\", \"w\") as f:\n",
    "        json.dump(pizza,f)\n",
    "    \n",
    "if os.path.exists('Pizza Shop.csv'):\n",
    "    print(\"The CSV File Exist\") \n",
    "    with open(\"Pizza Shop.csv\", \"a+\") as f:\n",
    "        for i in pizza:\n",
    "            f.write(\"%s,%s\\n\"%(i,pizza[i]))\n",
    "else:\n",
    "    print(\"The CSV File Does Not Exist But We Created It New\")\n",
    "    with open(\"Pizza Shop.csv\", \"w\") as f:\n",
    "        for i in pizza:\n",
    "            f.write(\"%s,%s\\n\"%(i,pizza[i]))"
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
