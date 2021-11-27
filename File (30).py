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
      "David\n",
      "Elliott\n",
      "4803 Wellesley St.\n"
     ]
    }
   ],
   "source": [
    "customer_15 = {\"first name\": \"David\", \"last name\": \"Elliott\", \"address\": \"4803 Wellesley St.\"}\n",
    "print(customer_15[\"first name\"])\n",
    "print(customer_15[\"last name\"])\n",
    "print(customer_15[\"address\"])"
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
      "['abc']\n"
     ]
    }
   ],
   "source": [
    "x=[\"abc\",]\n",
    "print(x) #it neglectes comma"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'first name': 'David', 'last name': 'Elliott', 'address': '4803 Wellesley St.', 'Flana': \"dimkana's\"}\n"
     ]
    }
   ],
   "source": [
    "customer_15[\"Flana\"]=\"dimkana's\"\n",
    "print(customer_15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The customer's first name is David\n",
      "The customer's last name is Elliott\n",
      "The customer's address is 4803 Wellesley St.\n"
     ]
    }
   ],
   "source": [
    "customer_29876 = {\"first name\": \"David\", \"last name\": \"Elliott\", \"address\": \"4803 Wellesley St.\"}\n",
    "for each_key, each_value in customer_29876.items():\n",
    "    print(\"The customer's \" + each_key + \" is \" +each_value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'first name': 'David', 'last name': 'Elliott', 'address': '4803 Wellesley St.'}, {'first name': 'Robert', 'last name': 'James', 'address': '5734 Dublin St.'}]\n",
      "-----------------------\n",
      "[{'first name': 'David', 'last name': 'Elliott', 'address': '4803 Wellesley St.'}, {'first name': 'Robert', 'last name': 'James', 'address': '5734 Dublin St.'}]\n"
     ]
    }
   ],
   "source": [
    "customer_07 = {\"first name\": \"David\", \"last name\": \"Elliott\", \"address\": \"4803 Wellesley St.\"}\n",
    "customer_09 = {\"first name\": \"Robert\", \"last name\": \"James\", \"address\": \"5734 Dublin St.\"}\n",
    "#indirect\n",
    "\n",
    "customers=[]\n",
    "customers.append(customer_07)\n",
    "customers.append(customer_09)\n",
    "print(customers)\n",
    "\n",
    "print(\"-----------------------\")\n",
    "#Direct\n",
    "customers=[customer_07 ,customer_09]\n",
    "print(customers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'customer id': 0, 'first name': 'John', 'last name': 'Ogden', 'address': '301 Arbor Rd.'}, {'customer id': 1, 'first name': 'Ann', 'last name': 'Sattermyer', 'address': 'PO Box 1145'}, {'customer id': 2, 'first name': 'Jill', 'last name': 'Somers', 'address': '3 Main St.'}]\n",
      "\n",
      " {'customer id': 2, 'first name': 'Jill', 'last name': 'Somers', 'address': '3 Main St.'}\n",
      "\n",
      " 3 Main St.\n",
      "\n",
      " [{'customer id': 0, 'first name': 'John', 'last name': 'Ogden', 'address': '301 Arbor Rd.'}, {'customer id': 1, 'first name': 'Ann', 'last name': 'Sattermyer', 'address': 'PO Box 1145'}, {'customer id': 2, 'first name': 'Jill', 'last name': 'Somers', 'address': '3 Main St.'}, {'customer id': 'new_customer_id', 'first name': 'new_first_name', 'last name': 'new_last_name', 'address': 'new_address'}]\n",
      "\n",
      " 4\n"
     ]
    }
   ],
   "source": [
    " customers = [\n",
    " {\n",
    " \"customer id\": 0,\n",
    " \"first name\":\"John\",\n",
    " \"last name\": \"Ogden\",\n",
    " \"address\": \"301 Arbor Rd.\",\n",
    "  },\n",
    "  {\n",
    " \"customer id\": 1,\n",
    " \"first name\":\"Ann\",\n",
    " \"last name\": \"Sattermyer\",\n",
    " \"address\": \"PO Box 1145\",\n",
    "  },\n",
    "  {\n",
    " \"customer id\": 2,\n",
    " \"first name\":\"Jill\",\n",
    " \"last name\": \"Somers\",\n",
    " \"address\": \"3 Main St.\", \n",
    "  }\n",
    "]\n",
    "print(customers)\n",
    "print(\"\\n\",customers[2])\n",
    "print(\"\\n\",customers[2][\"address\"])\n",
    "new_dic={\n",
    "\"customer id\": \"new_customer_id\",\n",
    "\"first name\": \"new_first_name\",\n",
    "\"last name\": \"new_last_name\",\n",
    "\"address\": \"new_address\",\n",
    "}\n",
    "customers.append(new_dic)\n",
    "print(\"\\n\",customers)\n",
    "print(\"\\n\",len(customers))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'first name': 'Ann', 'last name': 'Sattermyer', 'address': 'PO Box 1145'}\n"
     ]
    }
   ],
   "source": [
    "#dics with in a dic\n",
    "customers = {\n",
    " 0: {\n",
    " \"first name\":\"John\",\n",
    " \"last name\": \"Ogden\",\n",
    " \"address\": \"301 Arbor Rd.\",\n",
    "  },\n",
    "1: {\n",
    " \"first name\":\"Ann\",\n",
    " \"last name\": \"Sattermyer\",\n",
    " \"address\": \"PO Box 1145\",\n",
    "  },\n",
    "2: {\n",
    " \"first name\":\"Jill\",\n",
    " \"last name\": \"Somers\",\n",
    " \"address\": \"3 Main St.\", \n",
    "  }\n",
    "}\n",
    "print(customers[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n",
      "2322\n",
      "1944\n"
     ]
    }
   ],
   "source": [
    "#functions\n",
    "#subprocess function\n",
    "def add_numbers(n1 ,n2):\n",
    "    first_number = n1\n",
    "    second_number = n2\n",
    "    total = first_number + second_number\n",
    "    print(total)\n",
    "#Functions with parameters       \n",
    "add_numbers(6,5)    \n",
    "\n",
    "#Functions with values already\n",
    "def calc_tax(sales_total=43, tax_rate=54):\n",
    "    print(sales_total * tax_rate)\n",
    "\n",
    "calc_tax()\n",
    "calc_tax(324,6)\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Somers\n"
     ]
    }
   ],
   "source": [
    "def find_something(dict, inner_dict, target):\n",
    "    print(dict[inner_dict][target])\n",
    "    \n",
    "customers = {\n",
    " 0: {\n",
    " \"first name\":\"John\",\n",
    " \"last name\": \"Ogden\",\n",
    " \"address\": \"301 Arbor Rd.\",\n",
    " },\n",
    " 1: {\n",
    " \"first name\":\"Ann\",\n",
    " \"last name\": \"Sattermyer\",\n",
    " \"address\": \"PO Box 1145\",\n",
    " },\n",
    " 2: {\n",
    " \"first name\":\"Jill\",\n",
    " \"last name\": \"Somers\",\n",
    " \"address\": \"3 Main St.\",\n",
    " }, \n",
    " }\n",
    "\n",
    "find_something(customers, 2, \"last name\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The winner was marcello\n",
      "The score was 56\n",
      "overtime: yes\n",
      "injuries: none\n",
      "replace: ramos\n",
      "replacewith: bale\n",
      "<function display_result at 0x00000139D86BD9D8>\n"
     ]
    }
   ],
   "source": [
    "def display_result(winner, score, **other_info):\n",
    "    print(\"The winner was \" + winner)\n",
    "    print(\"The score was \" + score)\n",
    "    for key, value in other_info.items():\n",
    "        print(key + \": \" + value)\n",
    "        \n",
    "display_result(winner=\"marcello\", score=\"56\", overtime=\"yes\", injuries=\"none\", replace=\"ramos\", replacewith=\"bale\")\n",
    "\n",
    "print(display_result)\n"
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
