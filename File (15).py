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
      "Depth First Search :\n",
      "*********************\n",
      "Eforie\n",
      "Hirsova\n",
      "Urziceni\n",
      "Vaslui\n",
      "Iasi\n",
      "Neamt\n",
      "Bucharest\n",
      "Giurgiu\n",
      "Pitesti\n",
      "RimnicuVilcea\n",
      "Sibiu\n",
      "Fagaras\n",
      "Craiova\n",
      "Dobreta\n",
      "Mehadia\n",
      "Lugoj\n",
      "Timisoara\n",
      "Arad\n",
      "Zerind\n",
      "Oradea\n"
     ]
    }
   ],
   "source": [
    "VisitedCities = set()\n",
    "def DepthFirstSearch(City,VisitedCities,RomaniaMap):\n",
    "    if City not in VisitedCities:\n",
    "        print (City)\n",
    "        VisitedCities.add(City)\n",
    "        for NextCity in RomaniaMap[City]:  \n",
    "            DepthFirstSearch(NextCity,VisitedCities, RomaniaMap)          \n",
    "\n",
    "RomaniaMap = {\n",
    "\"Arad\" : [\"Zerind\",\"Timisoara\",\"Sibiu\"],\n",
    "\"Zerind\" : [\"Oradea\",\"Arad\"],\n",
    "\"Timisoara\" : [\"Lugoj\",\"Arad\"],\n",
    "\"Oradea\" : [\"Sibiu\",\"Zerind\"],    \n",
    "\"Lugoj\" : [\"Mehadia\",\"Timisoara\"],\n",
    "\"Mehadia\" : [\"Dobreta\",\"Lugoj\"],\n",
    "\"Dobreta\" : [\"Craiova\",\"Mehadia\"],\n",
    "\"Craiova\" : [\"RimnicuVilcea\",\"Dobreta\",\"Pitesti\"],\n",
    "\"RimnicuVilcea\" : [\"Sibiu\",\"Pitesti\",\"Craiova\"],\n",
    "\"Sibiu\" : [\"RimnicuVilcea\",\"Fagaras\"],\n",
    "\"Pitesti\" : [\"Bucharest\",\"RimnicuVilcea\",\"Craiova\"],\n",
    "\"Fagaras\" : [\"Bucharest\",\"Sibiu\"],\n",
    "\"Bucharest\" : [\"Giurgiu\",\"Urziceni\",\"Pitesti\",\"Fagaras\"],\n",
    "\"Urziceni\" : [\"Hirsova\",\"Vaslui\",\"Bucharest\"],\n",
    "\"Hirsova\" : [\"Eforie\",\"Urziceni\"],\n",
    "\"Vaslui\" : [\"Iasi\",\"Urziceni\"],\n",
    "\"Iasi\" : [\"Neamt\",\"Vaslui\"],\n",
    "\"Eforie\" : [\"Hirsova\"],\n",
    "\"Neamt\" : [\"Iasi\"],\n",
    "\"Giurgiu\" : [\"Bucharest\"]\n",
    "}\n",
    "\n",
    "print(\"Depth First Search :\")\n",
    "print(\"*********************\")\n",
    "DepthFirstSearch(\"Eforie\",VisitedCities, RomaniaMap)"
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
 "nbformat_minor": 4
}
