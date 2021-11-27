{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "from PIL import Image\n",
    "import glob\n",
    "images = []\n",
    "resized = []\n",
    "resized_array = []\n",
    "for file in glob.glob(r'\\Users\\Muhammad Faizan\\Desktop\\python\\picutres\\*.jpg'):\n",
    "    img = Image.open(file)\n",
    "    images.append(img)\n",
    "for image in images:\n",
    "    res = image.resize([200,200])\n",
    "    resized.append(res)\n",
    "for i in resized:\n",
    "    numpy = np.array(i,dtype=\"uint8\")\n",
    "    resized_array.append(numpy)\n",
    "    print(resized_array,'\\n',np.shape(resized_array))"
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
