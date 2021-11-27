{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Given array is\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "IOPub data rate exceeded.\n",
      "The notebook server will temporarily stop sending output\n",
      "to the client in order to avoid crashing it.\n",
      "To change this limit, set the config variable\n",
      "`--NotebookApp.iopub_data_rate_limit`.\n",
      "\n",
      "Current values:\n",
      "NotebookApp.iopub_data_rate_limit=1000000.0 (bytes/sec)\n",
      "NotebookApp.rate_limit_window=3.0 (secs)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "import time\n",
    "start = time.time()\n",
    "def insertionSort(arr): \n",
    "    for i in range(1, len(arr)):\n",
    "        key = arr[i]\n",
    "        j = i-1\n",
    "        while j >= 0 and key < arr[j] : \n",
    "                arr[j + 1] = arr[j] \n",
    "                j -= 1\n",
    "        arr[j + 1] = key \n",
    "         \n",
    "arr = [random.random() for _ in range(100)]\n",
    "print(\"Given array is\", end=\"\\n\")\n",
    "print(arr)\n",
    "insertionSort(arr) \n",
    "print(\"Sorted array is: \", end=\"\\n\")\n",
    "print(arr) \n",
    "end = time.time()\n",
    "print(\"\\nTime Taken:\")\n",
    "print(end - start)"
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
