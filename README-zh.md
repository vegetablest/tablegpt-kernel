# tablegpt-kernel  
**其他语言阅读: [English](README.md).**

`tablegpt-kernel`是一个定制的iPython内核，专为`tablegpt-agent`构建，用于在沙盒环境中执行代码。该内核预装了常用数据分析任务所需的依赖，助力快速开发与测试。  

## 安装方法  

### 通过 PyPI 安装  
从PyPI安装 **tablegpt-kernel**：  
```bash  
pip install tablegpt-kernel  
```  

### 通过源码安装（Git + Wheel）  
从源码仓库克隆并安装`tablegpt-kernel`：  
```bash  
git clone https://github.com/vegetablest/tablegpt-kernel  
cd tablegpt-kernel  
pip install .  
```  

## 使用方法

### 在 Jupyter Notebook 中使用  
在 Jupyter Notebook 的 **New** 菜单中，您会看到新增的 **Tablegpt Notebook** 选项。  

### 在控制台前端使用  
若需在Jupyter控制台前端使用，请在命令行中添加以下参数：  
```bash  
jupyter console --kernel=tablegpt
```
