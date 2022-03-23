
import pyapollo
from tkinter import *
from tkinter import ttk



if __name__ == '__main__':

    with open('apollo-propertier.txt') as f:
        content = f.readlines()

    myDict = {}

    for line in content:
        a, b = line.split('=')
        myDict[a] = b

    appIds = myDict['appid'].split(',')
    sourceUrls = myDict['sourceUrl'].split(',')
    targetUrls = myDict['targetUrl'].split(',')

    # 设置tkinter窗口
    root = Tk()
    # 绘制两个label,grid（）确定行列
    Label(root, text="请输入AppId：").grid(row=0, column=0)
    Label(root, text="请输入源url：").grid(row=1, column=0)
    Label(root, text="请输入目标url：").grid(row=2, column=0)

    # 创建下拉AppID菜单
    appiBox = ttk.Combobox(root)
    # 使用 grid() 来控制控件的位置
    appiBox.grid(row=0, column=1)
    # 设置下拉菜单中的值
    appiBox['value'] = appIds

    # 创建下拉源地址菜单
    sourceBox = ttk.Combobox(root)
    # 使用 grid() 来控制控件的位置
    sourceBox.grid(row=1,column=1)
    # 设置下拉菜单中的值
    sourceBox['value'] = sourceUrls

    # 创建下拉目标地址菜单
    targetBox = ttk.Combobox(root)
    # 使用 grid() 来控制控件的位置
    targetBox.grid(row=2, column=1)
    # 设置下拉菜单中的值
    targetBox['value'] = targetUrls


    # def func(event):
    #     print('select', appiBox.get() + "\n")
    #     print('select', sourceBox.get() + "\n")
    #     print('select', targetBox.get() + "\n")
    #
    #
    # # 绑定下拉菜单事件
    # appiBox.bind("<<ComboboxSelected>>", func)
    # sourceBox.bind("<<ComboboxSelected>>", func)
    # targetBox.bind("<<ComboboxSelected>>", func)

    # # 导入三个输入框
    # appId = Entry(root)
    # sourceUrl = Entry(root)
    # targetUrl = Entry(root)

    # # 设置输入框的位置
    # appId.grid(row=0, column=1)
    # sourceUrl.grid(row=1, column=1)
    # targetUrl.grid(row=2,column=1)

    # 清除函数，清除输入框的内容
    def delete():
        appiBox.delete(0, END)
        sourceBox.delete(0, END)
        targetBox.delete(0, END)
    #
    #
    # # 输入内容获取函数print打印
    # def show():
    #     print("appId: " + appiBox.get())
    #     print("源地址 ： " + sourceBox.get())
    #     print("目标地址 ： " + targetBox.get())


    def compare():
        appId = str(appiBox.get()).strip('\n')
        sourceUrl = str(sourceBox.get()).strip('\n')
        targetUrl = str(targetBox.get()).strip('\n')
        sourceApollo = pyapollo.ApolloClient(appId,"default",sourceUrl)
        targetApollo = pyapollo.ApolloClient(appId,"default",targetUrl)
        sourceApollo.start()
        targetApollo.start()

        source = sourceApollo._cache['application']
        target = targetApollo._cache['application']



        for k in target:
            if k in source:
                if target[k] != source[k]:
                    print("key : " + k + " :  source :" + source[k] + " ; target : " + target[k])
            else:
                print("target 新增 ： " + k + " ; value : " + target[k]);

        for k in source:
            if k not in target:
                print("source 少 ： " + k + " ; value : " + source[k]);
        sourceApollo.stop()
        targetApollo.stop()


    # 设置两个按钮，点击按钮执行命令 command= 命令函数
    theButton1 = Button(root, text="对比信息", width=10, command=compare)
    theButton2 = Button(root, text="清除", width=10, command=delete)


    # 设置按钮的位置行列及大小
    theButton1.grid(row=3, column=0, sticky=W, padx=10, pady=5)
    theButton2.grid(row=3, column=1, sticky=E, padx=10, pady=5)

    mainloop()
