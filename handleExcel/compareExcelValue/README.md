## **xlrd && xlwt**

对比两个 Excel 文件的值是否相等

### 依赖

- Python 3.7.3

### 原理

1. 使用 `xlrd` 对文件进行读取,并存入 dictionay，进行遍历对比
2. 使用 `xlwt` 将对比结果写入 log 文件

### 🍩一点点总结

1. `xlrd` 的读取函数是 **open_workbook()**，都是小写的喔
2. 文件名千万不可以，命名为 xlrd 或者 xlwt，那样会凉凉的
3. `xlrd` 里有花式读取方法，可以根据需要来选取最方便的方式

### 参考资料

- [xlwt](https://pypi.org/project/xlwt/)
- [xlrd](https://pypi.org/project/xlrd/)

### 测试数据

- 文件夹下的 original.xlsx 和 target.xlsx