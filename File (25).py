{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bayesian Network With Conditoional Probability :\n",
      "********************************************************\n",
      "Probability of Grass Being Wet     : 0.4503600000000001\n",
      "Probability of Grass Not Being Wet : 0.07164000000000002\n",
      "Final Joint Probability            : 0.5220000000000001\n"
     ]
    }
   ],
   "source": [
    "def Sprinkler(S,R):\n",
    "    if((S=='T') & (R=='F')):\n",
    "        Probability = 0.4\n",
    "    elif((S== 'T') & (R=='T')):\n",
    "        Probability = 0.01       \n",
    "    elif((S=='F') & (R=='F')):\n",
    "        Probability = 0.6\n",
    "    elif((S=='F') & (R=='T')):\n",
    "        Probability = 0.99\n",
    "    else:\n",
    "        print(\"The Values Are Invalid.\")\n",
    "    return Probability\n",
    "\n",
    "def Rain(R):\n",
    "    if(R=='T'):\n",
    "        Probability = 0.2\n",
    "    elif(R =='F'):\n",
    "        Probability = 0.8\n",
    "    else:\n",
    "        print(\"The Values Are Invalid.\")\n",
    "    return Probability \n",
    "\n",
    "def GrassWet(G,S,R):\n",
    "    if((G =='T') & (S =='F') & (R =='F')):\n",
    "        Probability = 0\n",
    "    elif((G =='T') & (S =='F') & (R =='T')):\n",
    "        Probability = 0.8\n",
    "    elif((G =='T') & (S =='T') & (R =='F')):\n",
    "        Probability = 0.9\n",
    "    elif((G =='T') & (S =='T') & (R =='T')):\n",
    "        Probability = 0.99\n",
    "    elif((G =='F') & (S =='F') & (R =='F')):\n",
    "        Probability = 1\n",
    "    elif((G =='F') & (S =='F') & (R =='T')):\n",
    "        Probability = 0.2\n",
    "    elif((G =='F') & (S =='T') & (R =='F')):\n",
    "        Probability = 0.1\n",
    "    elif((G =='F') & (S =='T') & (R =='T')):\n",
    "        Probability = 0.01\n",
    "    else:\n",
    "        print(\"The Values Are Invalid.\")\n",
    "    return Probability               \n",
    "\n",
    "def TheProbablitiy(G,S,R,L):\n",
    "    RainProbability      = Rain(R)\n",
    "    SprinklerProbability = Sprinkler(S,R)\n",
    "    GrassWetProbability  = GrassWet(G,S,R)   \n",
    "    Probability = RainProbability * SprinklerProbability * GrassWetProbability\n",
    "    L.append(Probability)\n",
    "\n",
    "L=[]\n",
    "TheProbablitiy('T', 'T', 'T',L)\n",
    "TheProbablitiy('T', 'T', 'F',L)\n",
    "TheProbablitiy('T', 'F', 'T',L)\n",
    "TheProbablitiy('T', 'T', 'T',L)\n",
    "L=sum(L)\n",
    "print(\"Bayesian Network With Conditoional Probability :\")\n",
    "print(\"********************************************************\")\n",
    "print(\"Probability of Grass Being Wet     :\",L)\n",
    "Finalprobabilty=L\n",
    "del L\n",
    "L=[]\n",
    "TheProbablitiy('F', 'T', 'T',L)\n",
    "TheProbablitiy('F', 'T', 'F',L)\n",
    "TheProbablitiy('F', 'F', 'T',L)\n",
    "TheProbablitiy('F', 'T', 'T',L)\n",
    "L=sum(L)\n",
    "Finalprobabilty=Finalprobabilty+L\n",
    "print(\"Probability of Grass Not Being Wet :\",L)\n",
    "print(\"Final Joint Probability            :\",Finalprobabilty) "
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
 "nbformat_minor": 4
}
