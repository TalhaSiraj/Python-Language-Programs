{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rooms In circular linked list: \n",
      "A\n",
      "B\n",
      "C\n",
      "D\n"
     ]
    }
   ],
   "source": [
    "class Node:    \n",
    "    def __init__(self,data):    \n",
    "        self.data = data;    \n",
    "        self.next = None;    \n",
    "\n",
    "class CreateList:    \n",
    "    def __init__(self):    \n",
    "        self.head = Node(None);    \n",
    "        self.tail = Node(None);    \n",
    "        self.head.next = self.tail;    \n",
    "        self.tail.next = self.head;           \n",
    "    def add(self,data):    \n",
    "        newNode = Node(data);        \n",
    "        if self.head.data is None:        \n",
    "            self.head = newNode;    \n",
    "            self.tail = newNode;    \n",
    "            newNode.next = self.head;    \n",
    "        else:        \n",
    "            self.tail.next = newNode;        \n",
    "            self.tail = newNode;        \n",
    "            self.tail.next = self.head;           \n",
    "    def display(self):    \n",
    "        current = self.head;    \n",
    "        if self.head is None:    \n",
    "            print(\"List is empty\");    \n",
    "            return;    \n",
    "        else:    \n",
    "            print(\"Rooms In circular linked list: \");        \n",
    "            print(current.data),    \n",
    "            while(current.next != self.head):    \n",
    "                current = current.next;    \n",
    "                print(current.data)   \n",
    "                \n",
    "class CircularLinkedList:    \n",
    "    cl = CreateList();       \n",
    "    cl.add(\"A\");    \n",
    "    cl.add(\"B\");    \n",
    "    cl.add(\"C\");    \n",
    "    cl.add(\"D\");    \n",
    "    cl.display();\n"
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
