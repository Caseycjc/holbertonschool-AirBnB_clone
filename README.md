<h1 align="center">
	<img alt="aitBnB" src="https://cdn.icon-icons.com/icons2/836/PNG/512/Airbnb_icon-icons.com_66791.png" height="30"/> AirBnB clone - The console
</h1>
<p align="center">
	<b><i>HOLBERTON SCHOOL AirBnB Clone - The Console</i></b><br>
</p>

# <center>![page](https://camo.githubusercontent.com/a8cd2eef2325c425519095dc2501111e630a77eddb454938c527cb82ea9c3aeb/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67)

<h3 align="center">
	<a href="##Description">Description</a>
	<span> · </span>
	<a href="#Installation">Installation</a>
	<span> · </span>
	<a href="#Compilation-and-Testing">Compilation and Testing</a>
	<span> · </span>
	<a href="#Example/Usage">Example/Usage</a>
</h3>

##   AirBnB Clone - The Console:

In our Holberton school group project pair programing we work on making a `AirBnB Clone The-Console 0.1`

## 📖 Description: 
 
<p>
This project is a complete web application, integrating database storage, a back-end API, and front-end interfacing in a clone of AirBnB! HBnB, if you will.

The project currently only implements the back-end console.
</p>

### 📦 Storage
All the classes are handled by the storage engine which is defined in the class FileStorage.
Each time the backend is initialized, HBnB defines an instance of FileStorage called storage. 
The storage object is loaded and re-loaded from any class instances stored in the JSON file. 

### 💻 Console 
The console is a command line interpreter that allow to manage of the backend of our AirBnB Console. It also used to handle and manipulate all classes used by HBnB.

### 💻 Console Commands


<table>
<tr>
<th> Commands </th> <th> Usage </th>
</tr>
<tr>
	 <td> help </td>
	 <td> help </td>
	 <td> displays all commands </td>
</tr>
<tr>
	<td> create </td> 
	<td> create < class > </td>
	<td> creates new object </td> 
</tr>
<tr>
	<td> update  </td>
	<td> update < class > < id > < attribute > < value > </td> 
	<td> updates attribute of an object </td>
</tr>
<tr>
	<td> destroy </td> 
	<td> destroy < class > < id >  </td>    
	<td> destroys specified object </td>
</tr>
<tr>
	<td> show </td>   
	<td> show < class > < id > </td>
	<td> show an object from a file, a database </td>
</tr>
<tr>
	<td> all  </td>
	<td> all < class > </td>
	<td> display all objects in class </td> 
</tr>
<tr>
	<td> quit </td>
	<td> quit  </td>
	<td> exits </td>
</tr>
<tr>
	<td> EOF </td>     
	<td>  </td>
	<td> exits </td>                                  	
</tr>
</table>



##  🛠️ Installation

```{r mon_bloc, echo = FALSE, WARNING = TRUE}
git clone https://github.com/Julia-5534/holbertonschool-AirBnB_clone.git
```

## 🛠️  Compilation and Testing

```{r mon_bloc, echo = FALSE, WARNING = TRUE}
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)

``` 



#### 🔧 Testing  via:
```{r mon_bloc, echo = FALSE, WARNING = TRUE}
$ python3 -m unittest tests/test_base_model.py

...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK

```

### 🎥 Example/Usage
 
 * command all :

<center> <img src ="https://media.giphy.com/media/bVCIRlSPmpxt0IgF4S/giphy.gif"/> </center>


## 📂Files:

<div>

<table class="tg" style="undefined;table-layout: fixed; width: 821px">
<colgroup>
<col style="width: 113px">
<col style="width: 152px">
<col style="width: 219px">
<col style="width: 337px">
</colgroup>
<thead>
  <tr>
    <th>Directory</th>
    <th>Subdirectory</th>
    <th class="tg-zylj">File</th>
   </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="18">holbertonschool-AirBnB_clone</td>
    <td  colspan="2"><a href ="https://github.com/majdideveloper/holbertonschool-AirBnB_clone/blob/main/console.py">console.py </a></td>
    </tr>
  <tr>
    <td colspan="2">README.md</td>
  </tr>
  <tr>
    <td  rowspan="7"> <a href ="https://github.com/majdideveloper/holbertonschool-AirBnB_clone/tree/main/models"> Models</a> </td>
    <td> <a href ="https://github.com/majdideveloper/holbertonschool-AirBnB_clone/blob/main/models/base_model.py" > base_model.py </a></td>
    </tr>
  <tr>
    <td> <a href= "https://github.com/majdideveloper/holbertonschool-AirBnB_clone/blob/main/models/user.py">  user.py </a></td>
     </tr>
  <tr>
    <td> <a href ="https://github.com/majdideveloper/holbertonschool-AirBnB_clone/blob/main/models/amenity.py">amenity.py </a></td>
     </tr>
  <tr>
    <td> <a href="https://github.com/majdideveloper/holbertonschool-AirBnB_clone/blob/main/models/city.py">city.py </a></td>
   </tr>
  <tr>
    <td><a href ="https://github.com/majdideveloper/holbertonschool-AirBnB_clone/blob/main/models/place.py">place.py</a></td>
  </tr>
  <tr>
    <td><a href ="https://github.com/majdideveloper/holbertonschool-AirBnB_clone/blob/main/models/review.py">review.py </a></td>
     </tr>
  <tr>
    <td><a href ="https://github.com/majdideveloper/holbertonschool-AirBnB_clone/blob/main/models/__init__.py">__init__.py</a></td>
   </tr>
  <tr>
    <td rowspan="2"> <a href ="https://github.com/Julia-5534/holbertonschool-AirBnB_clone/tree/main/models/engine">Models/engine</a></td>
    <td> <a href ="https://github.com/Julia-5534/holbertonschool-AirBnB_clone/blob/main/models/engine/__init__.py">__init__.py </a></td>
   </tr>
  <tr>
    <td><a href ="https://github.com/Julia-5534/holbertonschool-AirBnB_clone/blob/main/models/engine/file_storage.py">file_storage</a></td>
     </tr>
  <tr>
    <td rowspan="6"> <a href="https://github.com/Julia-5534/holbertonschool-AirBnB_clone/tree/main/tests/test_models">tests/test_model</a></td>
    <td> <a href ="https://github.com/Julia-5534/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_base_model.py">test_base_model.py </a></td>
    </tr>
  <tr>
    <td> <a href="https://github.com/Julia-5534/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_user.py">test_user.py</a></td>
   </tr>
  <tr>
    <td><a href ="https://github.com/Julia-5534/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_amenity.py">test_amenity.py </a></td>
  </tr>
<tr>
    <td><a href="https://github.com/Julia-5534/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_city.py">test_city.py</a></td>
 </tr>
  <tr>
    <td><a href ="https://github.com/Julia-5534/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_place.py">test_place.py</a></td>
  </tr>
  <tr>
    <td><a href="https://github.com/Julia-5534/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_review.py">test_review.py</td>
  </tr>
  <tr>
    <td><a href = "https://github.com/Julia-5534/holbertonschool-AirBnB_clone/tree/main/tests/test_models/test_engine">tests/test_file_storage.py </a></td>
    <td><a href ="https://github.com/Julia-5534/holbertonschool-AirBnB_clone/blob/main/tests/test_models/test_engine/test_file_storage.py">test_file storage</a></td>
  </tr>
</tbody>
</table>
 
</div>

## :octocat: Authors:

* [Casey Chase](https://github.com/Caseycjc)
* [Julia Bullard](https://github.com/Julia-5534)
