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
      "************************************\n",
      "Values Of Nodes : \n",
      "[[10, [100, 8]], [[1, 2], [20, 4]]]\n",
      "[[10, 10], [[1, 2], [20, 4]]]\n",
      "[10, [[1, 2], [20, 4]]]\n",
      "[10, [10, [20, 4]]]\n",
      "[10, [10, 10]]\n",
      "[10, 10]\n",
      "********\n",
      "************************************\n",
      "Min Max With Alpha Beta Prunning : \n",
      "Resultant Value : 10\n",
      "No Of Times Pruned : 2\n",
      "Value Of Alpha : 10\n",
      "Value Of Beta : 100\n",
      "************************************\n"
     ]
    }
   ],
   "source": [
    "Graph = [[[10, 6], [100, 8]],[[1, 2], [20, 4]]]\n",
    "Root = 0\n",
    "PrunedNodes = 0\n",
    "print(\"************************************\")\n",
    "print (\"Values Of Nodes : \")\n",
    "def ChildNodes(branch, depth, Alpha, Beta):\n",
    "    global Graph\n",
    "    global Root\n",
    "    global PrunedNodes\n",
    "    i = 0\n",
    "\n",
    "    for child in branch:\n",
    "        if type(child) is list:\n",
    "            (NewAlpha, NewBeta) = ChildNodes(child, depth + 1, Alpha, Beta)\n",
    "            if depth % 2 == 1:\n",
    "                Beta = NewAlpha if NewAlpha < Beta else Beta\n",
    "            else:\n",
    "                Alpha = NewBeta if NewBeta > Alpha else Alpha\n",
    "            branch[i] = Alpha if depth % 2 == 0 else Beta\n",
    "            i += 1\n",
    "            print (Graph)\n",
    "        else:\n",
    "            if depth % 2 == 0 and Alpha < child:\n",
    "                Alpha = child\n",
    "            if depth % 2 == 1 and Beta > child:\n",
    "                Beta = child\n",
    "            if Alpha >= Beta:\n",
    "                PrunedNodes += 1\n",
    "                break\n",
    "    if depth == Root:\n",
    "        Graph = Alpha if Root == 0 else Beta\n",
    "    return (Alpha, Beta)\n",
    "def AlphaBetaPrune(in_Graph=Graph, start=Root, upper=-100, lower=100):\n",
    "    global Graph\n",
    "    global PrunedNodes\n",
    "    global Root\n",
    "\n",
    "    (Alpha, Beta) = ChildNodes(Graph, start, upper, lower)\n",
    "    \n",
    "    if __name__ == \"__main__\":\n",
    "        print(\"********\")\n",
    "        print(\"************************************\")\n",
    "        print (\"Min Max With Alpha Beta Prunning : \")\n",
    "        print (\"Resultant Value :\", Graph)\n",
    "        print (\"No Of Times Pruned :\", PrunedNodes)\n",
    "        print (\"Value Of Alpha :\", Alpha)\n",
    "        print (\"Value Of Beta :\", Beta)\n",
    "        print(\"************************************\")\n",
    "        \n",
    "        \n",
    "\n",
    "    return (Alpha, Beta, Graph, PrunedNodes)\n",
    "if __name__ == \"__main__\":\n",
    "    AlphaBetaPrune(None)"
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
