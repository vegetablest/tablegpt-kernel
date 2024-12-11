# tablegpt-kernel  
**Read this in other languages: [中文](README-zh.md).**

`tablegpt-kernel` is a custom iPython kernel designed for use with `tablegpt-agent`, enabling code execution in a sandboxed environment. It comes preloaded with dependencies commonly used for data analysis, streamlining your workflow for development and testing.  

## Installation  

### Install from PyPI  
To install `tablegpt-kernel` from PyPI, run:  
```bash  
pip install tablegpt-kernel  
```  

### Install from Source (Git + Wheel)  
To install `tablegpt-kernel` from the source repository:  
```bash  
git clone https://github.com/vegetablest/tablegpt-kernel  
cd tablegpt-kernel  
pip install .  
```  

## Usage  

### In Jupyter Notebook  
After installation, the **New** menu in Jupyter Notebook will include an option for creating a **Tablegpt Notebook**.  

### In Console Frontends  
To use the kernel with Jupyter console frontends, add the following argument when launching:  
```bash  
jupyter console --kernel=tablegpt
```  
