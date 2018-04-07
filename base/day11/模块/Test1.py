
'''
import 模块.FuncTest

模块.FuncTest.go()
'''
'''
from 模块.FuncTest  import go
go()
'''
'''
from 模块.Google.com.search.GO import go
go()
'''


'''
import 模块.Google.com.search.GO
import 模块.FuncTest
模块.Google.com.search.GO.go()
模块.FuncTest.go()
'''



from 模块.FuncTest  import go
from 模块.Google.com.search.GO import go  #后面的覆盖前面的
go()


