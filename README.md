# Chinese_to_Minecraft_CommandBlock
用中文生成我的世界命令方块

![图片.png](https://i.loli.net/2021/07/30/7GuIy3l8HxYWOeZ.png)

可以使用变量赋值引用和下面的函数

用给定的中文命令生成我的世界命令

所有的命令都尽量放在一起按顺序执行

#命令用法/可用函数

    #取实体集_全部玩家() -> 返回所有玩家
    #物品方块 ('DIRT') 物品方块('钻石块') -> 返回一个物品方块类型表示该物品或方块
    #构建空间_对角坐标 (1,2,3,4,5,6) -> 返回一个空间表示一个矩形的区域 从x1y2z3 到 x4y5z6
    #构建位置_坐标(1,2,3) -> 返回一个位置 x1z2y3
    #取实体集_玩家名字 ('Steve') -> 返回一个实体集 表示所有名字是Steve的玩家
    #取实体集_实体名字 ('Dirt') -> 返回一个实体集 表示所有名字是Steve的实体
    #取实体_实体集_一个(取实体集_实体名字 ('Dirt')) -> 返回一个实体,只有实体可以构建相对空间或相对位置
    #取实体_实体集_一个(取实体集_实体名字 ('Dirt')) -> 返回遍历实体,只有实体可以构建相对空间或相对位置
    #取实体集_矩形空间(构建空间_对角坐标 (1,2,3,4,5,6)) -> 返回一个矩形空间中所有的实体集 (会导致额外的tag命令)
    #构建矩形空间_相对实体坐标(取实体_实体集_一个(取实体集_实体名字 ('雪球')),-1,-1,-1,1,1,1) -> 
                                            #返回一个矩形空间表示从雪球x-1,y-1,z-1到x+1,y+1,z+1
    #构建位置_相对实体坐标(取实体_实体集_一个(取实体集_实体名字 ('雪球')),1,1,1)
                                            #返回一个位置表示从雪球x+1,y+1,z+1
    #生物类型('雪球') -> 返回雪球生物
    #生成生物_位置_名字(构建位置_坐标(1,2,3),生物类型('雪球'),"snowball") 在1,2,3生成一个叫snowball的雪球(最后的参数可以填空文本,就不会改变名字)
    #取实体集_实体类型(生物类型('雪球')) -> 返回一个类型是雪球的所有实体集
    #填充空间_矩形空间(构建空间_对角坐标 (1,2,3,4,5,6),物品方块('DIRT')) -> 将空间填充为DIRT
    #填充空间_替换_矩形空间(构建空间_对角坐标 (1,2,3,4,5,6),物品方块('DIRT'),物品方块('钻石块')) -> 同上,只不过只替换钻石卡
    #放置方块_位置(构建位置_坐标(1,2,3),物品方块('DIRT')) -> 位置上放置DIRT
    #杀死实体(取实体集_玩家名字 ('Steve')) -> 杀死一个实体集或实体
    #传送实体到位置(取实体集_玩家名字 ('Steve'),构建位置_坐标(1,2,3)) -> 传送实体到x1y2z3
    #实体集交集(取实体集_玩家名字 ('Steve'),取实体集_矩形空间(构建空间_对角坐标 (1,2,3,4,5,6))) ->交集运算
    #实体集并集(取实体集_玩家名字 ('Steve'),取实体集_玩家名字 ('teve')) ->并集运算 (会导致额外的tag命令)
    #取实体集_实体_距离(取实体集_玩家名字 ('Steve'),5) -> 获取所有离实体集距离为5的实体(包括自身) (会导致额外的tag命令)
    #添加计分项("menu","菜单") -> 添加一个叫显示名为菜单,命令中用menu表示的菜单
    #删除计分项('menu') -> 删除menu
    #计分项_增加_文本玩家('menu','Time',1)  -> 把menu中Time的数值加1
    #计分项_增加('killcount',取实体集_玩家名字 ('Steve'),1)  -> 把killcount中Steve的数值加1
    #计分项_设置('killcount',取实体集_玩家名字 ('Steve'),0)  -> 把killcount中Steve的数组设置为0
    #计分项_设置_文本玩家 -> 区别同上
    #计分项_清除('killcount',取实体集_玩家名字 ('Steve')) -> 把Steve的名字从killcount中清除(如果显示的话)
    #计分项_清除_文本玩家 -> 区别同上
    #设置计分项边栏显示('killcount') -> 计分板设置为边栏查看
    #设置计分项菜单界面显示('killcount') -> 计分板设置为菜单查看
    #设置计分项名字下方显示('killcount') -> 计分板设置为名字下方显示
    #取实体集_计分板分数('killcount',"3..") -> 返回一个killcount是从3到无限大的实体集 '..5' 表示从无限小到5 '3'表示分数为3 '1..10'表示从1到10
    #聊天栏_输出JSON(取实体集_玩家名字 ('Steve'),'{"rawtext":[{"selector":"@s "},{"text":" 计分板obj的值是："},{"score":{"name":"@s","objective":"obj"}}]}')
                                #最基本的Json {"rawtext": [{"text":"你想说的话"}]}
    #标题_输出JSON(取实体集_玩家名字 ('Steve'),'{"rawtext": [{"translate":"§lChapter %%s","with":["I"]}]}','{"rawtext": [{"text":"§7§oThe story begins..."}]}')
    #标题底栏_输出JSON(取实体集_玩家名字 ('Steve'),'{"rawtext": [{"text":"你想说的话"}]}')
    #标题_输出JSON(取实体集_玩家名字 ('Steve'),构建Json(Json文本('你好啊'),Json计分板分数__文本玩家('killcount','水井y')))
    #上面4个第一个参数都是输出的目标,Json可以通过构建Json来使用
    #载入结构(构建位置_坐标(1,1,1),'www') -> 载入一个结构www到1,1,1
    #保存结构(构建空间_对角坐标 (1,2,3,4,5,6),'www') ->保存1,2,3 4,5,6 为www
    
#例程
1) 场景:将随机玩家脚下的方块替换为空气
中文命令
players = 取实体集_全部玩家()
loc = 构建位置_相对单个实体坐标(取单个实体_实体集_默认(players),0,-1,0)
放置方块_位置( loc ,物品方块('AIR'))
输出
execute @e[type=player,c=1] ~ ~ ~ setblock ~0 ~-1 ~0 AIR 0


