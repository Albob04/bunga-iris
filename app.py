{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "da467d0d",
   "metadata": {},
   "source": [
    "## <div align=\"center\"> TUGAS LAB IS388 Data Analysis </div>\n",
    "## <div align=\"center\"> WEEK [XX]: [Topic]</div>\n",
    "#### <div align=\"center\"> Semester Ganjil 2024/2025 </div>\n",
    "---"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1529afb1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime\n",
    "import uuid\n",
    "\n",
    "studentName = \"Nama\"\n",
    "studentNIM = \"NIM\"\n",
    "studentClass = \"Class\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "c0fdf3fd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name: \t\tNama\n",
      "NIM: \t\tNIM\n",
      "NIM: \t\tClass\n",
      "Start: \t\t2025-12-04 13:44:39.826391\n",
      "Device ID: \tb51a3e6f-d0dc-11f0-908e-f09e4a101f8e\n"
     ]
    }
   ],
   "source": [
    "myDate = datetime.datetime.now()\n",
    "myDevice = str(uuid.uuid1())\n",
    "\n",
    "print(\"Name: \\t\\t{}\".format(studentName))\n",
    "print(\"NIM: \\t\\t{}\".format(studentNIM))\n",
    "print(\"NIM: \\t\\t{}\".format(studentClass))\n",
    "print(\"Start: \\t\\t{}\".format(myDate))\n",
    "print(\"Device ID: \\t{}\".format(myDevice))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "247cf3e5",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "67531a34",
   "metadata": {},
   "source": [
    "## <div align=\"center\"> Guided Lab </div>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2b4f49c6",
   "metadata": {},
   "source": [
    "### Enter Guided Lab Code Here:"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "809f9851-aaf0-4700-95c1-b72aaafbe9e3",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "aac1948c-4261-49e1-afde-c5063ae3f758",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'prediction'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[14], line 4\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mpandas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mpd\u001b[39;00m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mnumpy\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mnp\u001b[39;00m\n\u001b[1;32m----> 4\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;21;01mprediction\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m predict\n\u001b[0;32m      6\u001b[0m st\u001b[38;5;241m.\u001b[39mtitle(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mClassifying Iris Flowers\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m      7\u001b[0m st\u001b[38;5;241m.\u001b[39mmarkdown(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mToy model to play to classify iris flowers into \u001b[39m\u001b[38;5;130;01m\\\u001b[39;00m\n\u001b[0;32m      8\u001b[0m \u001b[38;5;124m    (setosa, versicolor, virginica) based on their sepal/petal \u001b[39m\u001b[38;5;124m\\\u001b[39m\u001b[38;5;124m and length/width.\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'prediction'"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "from prediction import predict\n",
    "\n",
    "st.title('Classifying Iris Flowers')\n",
    "st.markdown('Toy model to play to classify iris flowers into \\\n",
    "    (setosa, versicolor, virginica) based on their sepal/petal \\ and length/width.')\n",
    "    \n",
    "st.header(\"Plant Features\")\n",
    "coll, col2 = st.columns(2)\n",
    "         \n",
    "with coll:\n",
    "    st.text(\"Sepal characteristics\")\n",
    "    sepal_1 = st.slider('Sepal lenght (cm)', 1.0, 8.0, 0.5)\n",
    "    sepal_w = st.slider('Sepal width (cm)', 2.0, 4.4, 0.5)\n",
    "    \n",
    "with col2:\n",
    "    st.text(\"Pepal characteristics\")\n",
    "    petal_1 = st.slider('Petal lenght (cm)', 1.0, 7.0, 0.5)\n",
    "    petal_w = st.slider('Petal width (cm)', 0.1, 2.5, 0.5)\n",
    "    \n",
    "st.text('')\n",
    "if st.button(\"Predict type of Iris\"):\n",
    "    result = predict(\n",
    "        np.array([[sepal_1, sepal_w, petal_1, petal_w]]))\n",
    "    st.text(result[0])\n",
    "\n",
    "    \n",
    "st.text('')\n",
    "st.text('')\n",
    "st.markdown()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d2127cb0",
   "metadata": {},
   "source": [
    "----"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "69b7f628",
   "metadata": {},
   "source": [
    "## <div align=\"center\"> Conclusion </div>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b7ecf70d",
   "metadata": {},
   "source": [
    "### Enter Your Conclusion Here:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df392fe6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "b765bf3f",
   "metadata": {},
   "source": [
    "----"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "650b115b",
   "metadata": {},
   "outputs": [],
   "source": [
    "studentName2 = \"Nama2\"\n",
    "studentNIM2 = \"NIM2\"\n",
    "studentClass2 = \"Class2\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "40f84526",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name: \t\tNama2\n",
      "NIM: \t\tNIM2\n",
      "NIM: \t\tClass2\n",
      "End: \t\t2025-12-04 13:44:39.826391\n",
      "Device ID: \tb51a3e6f-d0dc-11f0-908e-f09e4a101f8e\n"
     ]
    }
   ],
   "source": [
    "print(\"Name: \\t\\t{}\".format(studentName2))\n",
    "print(\"NIM: \\t\\t{}\".format(studentNIM2))\n",
    "print(\"NIM: \\t\\t{}\".format(studentClass2))\n",
    "print(\"End: \\t\\t{}\".format(myDate))\n",
    "print(\"Device ID: \\t{}\".format(myDevice))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "14310678",
   "metadata": {},
   "source": [
    "----"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "88210d09",
   "metadata": {},
   "source": [
    "## <div align=\"center\"> Reference </div>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "20664996",
   "metadata": {},
   "source": [
    "### Input Your Reference Here  (Jika ada):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ba2ed2b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "29050624",
   "metadata": {},
   "source": [
    "----"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af937f5f-2617-4067-a899-19f7ef5d01a7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c33a50ce-cc92-413b-b994-0745f9e7e7fa",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b84dbbe-6013-47f2-b021-11ea682a32ef",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
