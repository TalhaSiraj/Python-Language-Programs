{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def myname(name):\n",
    "    return name.lower(), name.upper(), name.capitalize() \n",
    "\n",
    "Name= input(\"Enter The Name: \")\n",
    "upper,lower,capital= myname(Name)\n",
    "print(upper,lower,capital)\n",
    "\n",
    "Name2= input(\"Enter The Name: \")\n",
    "print(Name2)\n",
    "print(type(Name2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def whatever():\n",
    "    y=20\n",
    "    print(y)\n",
    "    \n",
    "y=50    \n",
    "whatever()\n",
    "print(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "cleanest_cities = [\"Cheyenne\", \"Santa Fe\", \"Tucson\", \"Great Falls\", \"Honolulu\"]\n",
    "user_input = \"\"\n",
    "while user_input != \"q\":\n",
    "    user_input = input(\"Enter a city, or q to quit:\")\n",
    "    if user_input != \"q\":\n",
    "        if user_input in cleanest_cities:\n",
    "            print(\"It's one of the cleanest cities\")\n",
    "        else:\n",
    "            print(\"It's not the cleanest cities\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
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
