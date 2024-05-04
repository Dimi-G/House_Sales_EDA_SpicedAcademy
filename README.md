# King County House Exploratory Data Analysis 

## Description

Follow along JupyterLab Notebook performing Exploratory Data Analysis of the King County House dataset. We examine a case-based scenario with specific client requirements. 

The folder includes Spiced-EDA Presentation-House Sales.pdf file, with the respective project presentation. 

![Preview](data/preview.gif)

## Installation
Clone the repository:
```
git clone https://github.com/Dimi-G/House_Sales_EDA_SpicedAcademy.git
cd your_project
```



## Set up your Environment
This repo contains a requirements.txt file with a list of all the packages and dependencies you will need.

Before you can start with plotly in Jupyter Lab you have to install node.js (if you haven't done it before).
- Check **Node version**  by run the following commands:
    ```sh
    node -v
    ```
    If you haven't installed it yet, begin at `step_1`. Otherwise, proceed to `step_2`.


### **`macOS`** type the following commands : 


- `Step_1:` Update Homebrew and install Node by following commands:
    ```sh
    brew update
    brew install node
    ```

- `Step_2:` Install the virtual environment and the required packages by following commands:

    ```BASH
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
### **`WindowsOS`** type the following commands :


- `Step_1:` Update Chocolatey and install Node by following commands:
    ```sh
    choco upgrade chocolatey
    choco install nodejs
    ```

- `Step_2:` Install the virtual environment and the required packages by following commands.

   For `PowerShell` CLI :

    ```PowerShell
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

    For `Git-Bash` CLI :
  
    ```BASH
    python -m venv .venv
    source .venv/Scripts/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
 

 **`Note:`**
    If you encounter an error when trying to run `pip install --upgrade pip`, try using the following command:

   ```Bash
   python.exe -m pip install --upgrade pip
   ```

## Usage
JupyterLab Notebook:To run the JupyterLab Notebook, execute the following command from within the project folder:
```
jupyter-lab
```

## Contributing 

Contributions are welcome. If you would wish to contribute, please fork the project, create a branch with your additions and submit a pull request.

