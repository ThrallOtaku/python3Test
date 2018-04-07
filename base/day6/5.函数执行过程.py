def go1():
    print("go1  start")
    print("go1  end")

def go2():
    print("go2  start")
    print("go2  end")


def go3():
    print("go3  start")
    print("go3  end")

#按照先后顺序执行，go2函数必须等go1执行完成再执行
go1()
go2()
go3()