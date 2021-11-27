{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#1. Parsing Of The Sir's Given Text File:\n",
    "\n",
    "from os import path\n",
    "\n",
    "def filecheak(e):\n",
    "    f         = open(e, encoding=\"utf8\")\n",
    "    line      = 0\n",
    "    paragraph = 0\n",
    "    cheak     = True\n",
    "    for i in f:\n",
    "        if '\\n' in i:\n",
    "            line += 1\n",
    "            if len(i) < 2:\n",
    "                cheak = True\n",
    "            elif len(i) > 2 and cheak is True:\n",
    "                paragraph = paragraph + 1\n",
    "                cheak     = False\n",
    "    f.close()\n",
    "    print(\"Number Of Paragraphs:            {}\".format(paragraph))\n",
    "\n",
    "def file(path):\n",
    "    g                = open(path, encoding=\"utf8\")\n",
    "    spaces           = tabs = words = num_lines = totalchars = specialchracters = 0\n",
    "    lines_in_file    = g.read()\n",
    "    totalchars       = len(lines_in_file)\n",
    "    words            = len(lines_in_file.split())\n",
    "    num_lines        = lines_in_file.count('\\n') +1\n",
    "    tabs             = len(lines_in_file.split('\\t')) -1\n",
    "    spaces           = len(lines_in_file.split(' ')) -1\n",
    "    specialchracters = totalchars - spaces - tabs\n",
    "    g.close()\n",
    "    return spaces , tabs, num_lines, words, specialchracters\n",
    "    \n",
    "name = input(\"Enter Your Text Filename: \")\n",
    "\n",
    "if path.isfile(name) is True:        \n",
    "    spaces, tabs, lines, words, specialchracters = file(name)\n",
    "    print(\"\\nYour Requested Information: \".format(name))\n",
    "    print(\"\\nNumber Of Words:                 {}\".format(words))\n",
    "    print(\"Number Of Lines:                 {}\".format(lines))\n",
    "    print(\"Number Of Non-Space Characters:  {}\".format(specialchracters))\n",
    "    print(\"Number Of Spaces:                {}\".format(spaces))\n",
    "    print(\"Number Of Tabs:                  {}\".format(tabs))\n",
    "    filecheak(name)    \n",
    "else :\n",
    "    print(\"\\nThe File (\", name, \") Does Not Exist.\")   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Your HTML Filename: example_html_file.html\n",
      "\n",
      "Your Requested Information: \n",
      "\n",
      "The Opening Tags: {'html': 1, 'head': 1, 'title': 1, 'style': 1, 'body': 1, 'h1': 1, 'p': 3, 'a': 1}\n",
      "The Closing Tags: {'title': 1, 'style': 1, 'head': 1, 'h1': 1, 'p': 3, 'a': 1, 'body': 1, 'html': 1}\n"
     ]
    }
   ],
   "source": [
    "#2. Parsing Of The Sir's Given HTML File:\n",
    "\n",
    "from os import path\n",
    "from html.parser import HTMLParser\n",
    "\n",
    "opentags  ={}\n",
    "closetags ={}\n",
    "class hparser(HTMLParser):\n",
    "    def handle_starttag(a, tag, attrs):\n",
    "        if tag not in opentags:\n",
    "            opentags[tag] = 1\n",
    "        else:\n",
    "            opentags[tag] +=1\n",
    "            \n",
    "    def display(a):  \n",
    "        print(\"\\nThe Opening Tags: {}\".format(opentags))\n",
    "        print(\"The Closing Tags: {}\".format(closetags))\n",
    "        \n",
    "    def handle_endtag(a, tag):\n",
    "        if tag not in closetags:\n",
    "            closetags[tag] = 1\n",
    "        else:\n",
    "            closetags[tag]  +=1 \n",
    "\n",
    "htmlname = input(\"Enter Your HTML Filename: \")\n",
    "\n",
    "if path.isfile(htmlname) is True:\n",
    "    parser = hparser()\n",
    "    f      = open(htmlname, 'r')\n",
    "    data   = f.read()\n",
    "    print(\"\\nYour Requested Information: \".format(htmlname))\n",
    "    parser.feed(data)\n",
    "    parser.display() \n",
    "    opentags = {}\n",
    "else :\n",
    "    print(\"\\nThe File (\", htmlname, \") Does Not Exist.\")  "
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
