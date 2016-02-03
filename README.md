# README

haroopad导出的html文件中，如果包含了本地图片资源，其`<img>`标签的`src`属性内容是绝对路径，不方便html文件交换。这个脚本可以把绝对路径转换成相对路径，同时把相关的图片文件拷贝到与html文件相同的路径下。

## 用法

````python
python transhtml.py html文件
````
