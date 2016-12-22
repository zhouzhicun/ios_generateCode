###描述文件
#####描述文件主要由三部分组成：   
1. 文件夹描述(folder节点)，具体定义如下:
		
		folder|文件夹名 
2. 类描述(class节点)，具体定义如下：

		class|基类名|类名
		
3. 属性描述，具体定义如下:
		
		属性类型|属性名
	
#####注意: 
* 本脚本的目的主要是为了减轻view定义的工作量。因此为了兼顾配置简单化，属性描述中只能添加UI控件属性。
* 文件夹描述定义了一个文件夹，脚本会在类描述文件所有当前目录下创建该文件夹，并使得后续的类描述生成的.h.m文件都在该文件夹，直到下一个文件夹描述。
* 由于生成出来的.h.m文件，无法做到文件内容格式对齐，因此只能手工打开文件(双击默认xcode打开)
然后ctrl+a全选-->右击-->Structure-->Re-Indent


例如:

	folder|aaa
	
	class|UIView|loginView
	UILabel|nameLabel
	UILabel|textLabel
	UILabel|ageLabel
	UIImageView|imageView
	UIButton|loginButton
	
	class|UIView|RegisterView
	UILabel|nameLabel
	UILabel|textLabel
	UILabel|ageLabel
	UIImageView|imageView
	UIButton|loginButton
	
	class|XNLBaseViewModel|LoginViewModel
	
	class|UIViewController|LoginViewController






####如何使用脚本
1. 新创建一个文件夹，然后在该文件夹下面创建一个描述文件，文件名随意，然后写上类描述等。
2. 打开控制台，python test.py
3. 根据输出提示，把描述文件拖到控制台即可，然后回车。脚本就会在描述文件所在当前目录创建对应的子目录以及生成对应的.h.m文件到各个子目录。