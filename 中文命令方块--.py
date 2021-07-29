#!/usr/bin/env python
import random #line:13
import os #line:14
_OOOO000OO00O0O0O0 =['烈焰人','blaze'],['顶部蜘蛛','cave_spider'],['苦力怕','creeper'],['溺尸','drowned'],['远古守卫者','elder_guardian'],['末影龙','ender_dragon'],['末影人','enderman'],['末影螨','endermite'],['唤魔者','evoker'],['恶魂','ghast'],['巨人','giant'],['守卫者','guardian'],['尸壳','husk'],['劫掠兽','ravager'],['幻术师','illusioner'],['岩浆怪','magma_cube'],['幻翼','phantom'],['掠夺者','pillager'],['河豚','pufferfish'],['潜影贝','shulker'],['蠹虫','silverfish'],['骷髅','skeleton'],['史莱姆','slime'],['蜘蛛','spider'],['流浪者','stray'],['恼鬼','vex'],['卫道士','vindicator'],['女巫','witch'],['凋灵','wither'],['凋灵骷髅','wither_skeleton'],['僵尸','zombie'],['僵尸猪人','zombie_pigman'],['僵尸村民','zombie_villager'],['蝙蝠','bat'],['猫','cat'],['鸡','chicken'],['鳕鱼','cod'],['牛','cow'],['海豚','dolphin'],['驴','donkey'],['马','horse'],['铁傀儡','iron_golem'],['羊驼','llama'],['哞菇','mooshroom'],['骡','mule'],['豹猫','ocelot'],['熊猫','panda'],['鹦鹉','parrot'],['猪','pig'],['北极熊','polar_bear'],['兔子','rabbit'],['鲑鱼','salmon'],['羊','sheep'],['骷髅马','skeleton_horse'],['雪傀儡','snow_golem'],['鱿鱼','squid'],['热带鱼','tropical_fish'],['海龟','turtle'],['村民','villager'],['狼','wolf'],['僵尸马','zombie_horse'],['效果区域云','area_effect_cloud'],['拴绳','leash_knot'],['画','painting'],['物品展示框','item_frame'],['盔甲架','armor_stand'],['唤魔者尖牙','evoker_fangs'],['末地水晶','end_crystal'],['掷出的鸡蛋','egg'],['射出的箭或药箭','arrow'],['射出的光灵箭','spectral_arrow'],['三叉戟','trident'],['掷出的雪球','snowball'],['恶魂火球','fireball'],['烈焰人火球或火焰弹','small_fireball'],['掷出的末影珍珠','ender_pearl'],['掷出的末影之眼','eye_of_ender'],['扔出的药水','potion'],['掷出的附魔之瓶','experience_bottle'],['凋灵之首','wither_skull'],['烟花火箭','firework_rocket'],['潜影贝导弹','shulker_bullet'],['末影龙火球','dragon_fireball'],['羊驼的口水','llama_spit'],['命令方块矿车','command_block_minecart'],['船','boat'],['矿车','minecart'],['运输矿车','chest_minecart'],['动力矿车','furnace_minecart'],['TNT矿车','tnt_minecart'],['漏斗矿车','hopper_minecart'],['刷怪笼矿车','spawner_minecart'],['激活的TNT','tnt '],['掉落中的方块','falling_block'],['掉落的物品','item '],['经验球','experience_orb']#line:17
_OO00OO00OOOO00O0O =[['空气','AIR','0'],['石头','STONE','1'],['草块','GRASS','2'],['泥土','DIRT','3'],['圆石','COBBLESTONE','4'],['橡木木板','WOOD','5'],['云杉木板','WOOD:1','5:1'],['桦木木板','WOOD:2','5:2'],['丛林木板','WOOD:3','5:3'],['橡树树苗','SAPLING','6'],['云杉树苗','SAPLING:1','6:1'],['桦木树苗','SAPLING:2','6:2'],['丛林树苗','SAPLING:3','6:3'],['沙子','SAND','12'],['沙硕','GRAVEL','13'],['金矿石','GOLD_ORE','14'],['铁矿石','IRON_ORE','15'],['煤矿石','COAL_ORE','16'],['橡木','LOG','17'],['云杉木','LOG:1','17:1'],['白桦木','LOG:2','17:2'],['丛林木','LOG:3','17:3'],['橡木树叶','LEAVES','18'],['云杉树叶','LEAVES:1','18:1'],['白桦树叶','LEAVES:2','18:2'],['丛林树叶','LEAVES:3','18:3'],['玻璃','GLASS','20'],['青金石矿石','LAPIS_ORE','21'],['青金石块','LAPIS_BLOCK','22'],['发射器','DISPENSER','23'],['沙石','SANDSTONE','24'],['錾制沙石','SANDSTONE:1','24:1'],['平滑沙石','SANDSTONE:2','24:2'],['音符盒','NOTE_BLOCK','25'],['动力铁轨','POWERED_RAIL','27'],['探测铁轨','DETECTOR_RAIL','28'],['粘性活塞','PISTON_STICKY_BASE','29'],['灌木','LONG_GRASS','31'],['枯死的灌木','DEAD_BUSH','32'],['活塞','PISTON_BASE','33'],['白色羊毛','WOOL','35'],['橙色羊毛','WOOL:1','35:1'],['红色羊毛','WOOL:2','35:2'],['蓝色羊毛','WOOL:3','35:3'],['黄色羊毛','WOOL:4','35:4'],['灰色羊毛','WOOL:5','35:5'],['粉色羊毛','WOOL:6','35:6'],['灰色羊毛','WOOL:7','35:7'],['淡灰色羊毛','WOOL:8','35:8'],['青色羊毛','WOOL:9','35:9'],['紫色羊毛','WOOL:10','35:10'],['蓝色羊毛','WOOL:11','35:11'],['棕色羊毛','WOOL:12','35:12'],['深绿色羊毛','WOOL:13','35:13'],['红色羊毛','WOOL:14','35:14'],['黑色羊毛','WOOL:15','35:15'],['蒲公英','YELLOW_FLOWER','37'],['玫瑰','RED_ROSE','38'],['棕色蘑菇','BROWN_MUSHROOM','39'],['红色蘑菇','RED_MUSHROOM','40'],['金块','GOLD_BLOCK','41'],['铁块','IRON_BLOCK','42'],['石台阶','STEP','44'],['沙石台阶','STEP:1','44:1'],['木台阶','STEP:2','44:2'],['圆石台阶','STEP:3','44:3'],['砖台阶','STEP:4','44:4'],['石砖台阶','STEP:5','44:5'],['红砖','BRICK','45'],['TNT','TNT','46'],['书架','BOOKSHELF','47'],['苔石','MOSSY_COBBLESTONE','48'],['黑曜石','OBSIDIAN','49'],['火把','TORCH','50'],['橡木楼梯','WOOD_STAIRS','53'],['箱子','CHEST','54'],['钻石矿石','DIAMOND_ORE','56'],['钻石块','DIAMOND_BLOCK','57'],['工作台','WORKBENCH','58'],['熔炉','FURNACE','61'],['梯子','LADDER','65'],['铁轨','RAILS','66'],['石楼梯','COBBLESTONE_STAIRS','67'],['拉杆','LEVER','69'],['石压力板','STONE_PLATE','70'],['木压力板','WOOD_PLATE','72'],['红石矿石','REDSTONE_ORE','73'],['红石火把','REDSTONE_TORCH_ON','76'],['石按钮','STONE_BUTTON','77'],['冰','ICE','79'],['雪','SNOW_BLOCK','80'],['仙人掌','CACTUS','81'],['粘土','CLAY','82'],['唱片机','JUKEBOX','84'],['栅栏','FENCE','85'],['南瓜','PUMPKIN','86'],['地狱岩','NETHERRACK','87'],['灵魂沙','SOUL_SAND','88'],['萤石','GLOWSTONE','89'],['南瓜灯','JACK_O_LANTERN','91'],['活板门','TRAP_DOOR','96'],['石砖','SMOOTH_BRICK','98'],['苔石砖','SMOOTH_BRICK:1','98:1'],['裂石砖','SMOOTH_BRICK:2','98:2'],['錾制石砖','SMOOTH_BRICK:3','98:3'],['蘑菇','HUGE_MUSHROOM_1','99'],['蘑菇','HUGE_MUSHROOM_2','100'],['铁栅栏','IRON_FENCE','101'],['玻璃板','THIN_GLASS','102'],['西瓜','MELON_BLOCK','103'],['藤蔓','VINE','106'],['栅栏门','FENCE_GATE','107'],['砖楼梯','BRICK_STAIRS','108'],['石楼梯','SMOOTH_STAIRS','109'],['菌丝','MYCEL','110'],['睡莲','WATER_LILY','111'],['地狱砖块','NETHER_BRICK','112'],['地狱砖栅栏','NETHER_FENCE','113'],['地狱砖楼梯','NETHER_BRICK_STAIRS','114'],['附魔台','ENCHANTMENT_TABLE','116'],['末地石','ENDER_STON','121'],['龙蛋','DRAGON_EGG','122'],['红石灯','REDSTONE_LAMP_OFF','123'],['橡木台阶','WOOD_STEP','126'],['云杉台阶','WOOD_STEP:1','126:1'],['桦木台阶','WOOD_STEP:2','126:2'],['丛林台阶','WOOD_STEP:3','126:3'],['沙石楼梯','SANDSTONE_STAIRS','128'],['绿宝石矿石','EMERALD_ORE','129'],['末影箱','ENDER_CHEST','130'],['拌线钩','TRIPWIRE_HOOK','131'],['绿宝石矿石','EMERALD_BLOCK','133'],['云杉木楼梯','SPRUCE_WOOD_STAIRS','134'],['桦木楼梯','BIRCH_WOOD_STAIRS','135'],['丛林木楼梯','JUNGLE_WOOD_STAIRS','136'],['铁铲子','IRON_SPADE','256'],['铁镐','IRON_PICKAXE','257'],['铁斧','IRON_AXE','258'],['打火石','FLINT_AND_STEEL','259'],['弓','BOW','261'],['铁剑','IRON_SWORD','267'],['木剑','WOOD_SWORD','268'],['木铲','WOOD_SPADE','269'],['木镐','WOOD_PICKAXE','270'],['木斧','WOOD_AXE','271'],['石剑','STONE_SWORD','272'],['石铲','STONE_SPADE','273'],['石镐','STONE_PICKAXE','274'],['石斧','STONE_AXE','275'],['金剑','GOLD_SWORD','283'],['金铲','GOLD_SPADE','284'],['金镐','GOLD_PICKAXE','285'],['金斧','GOLD_AXE','286'],['木锄','WOOD_HOE','290'],['石锄','STONE_HOE','291'],['铁锄','IRON_HOE','292'],['钻石锄','DIAMOND_HOE','293'],['金锄','GOLD_HOE','294'],['钻石剑','DIAMOND_SWORD','276'],['钻石铲','DIAMOND_SPADE','277'],['钻石镐','DIAMOND_PICKAXE','278'],['钻石斧','DIAMOND_AXE','279'],['桶','BUCKET','325'],['水桶','WATER_BUCKET','326'],['岩浆桶','LAVA_BUCKET','327'],['指南针','COMPASS','345'],['钓鱼竿','FISHING_ROD','346'],['钟','WATCH','347'],['空地图','MAP','358'],['剪刀','SHEARS','359'],['火焰弹','FIREBALL','385'],['苹果','APPLE','260'],['碗','BOWL','281'],['炖蘑菇','MUSHROOM_SOUP','282'],['小麦种子','SEEDS','295'],['小麦','WHEAT','296'],['面包','BREAD','297'],['生猪排','PORK','319'],['熟猪排','GRILLED_PORK','320'],['金苹果','GOLDEN_APPLE','322'],['牛奶','MILK_BUCKET','335'],['生鱼','RAW_FISH','349'],['熟鱼','COOKED_FISH','350'],['糖','SUGAR','353'],['蛋糕','CAKE','354'],['曲奇','COOKIE','357'],['西瓜','MELON','360'],['南瓜种子','PUMPKIN_SEEDS','361'],['西瓜种子','MELON_SEEDS','362'],['生牛肉','RAW_BEEF','363'],['牛排','COOKED_BEEF','364'],['生鸡肉','RAW_CHICKEN','365'],['熟鸡肉','COOKED_CHICKEN','366'],['皮革帽子','LEATHER_HELMET','298'],['皮革外衣','LEATHER_CHESTPLATE','299'],['皮革裤子','LEATHER_LEGGINGS','300'],['皮靴','LEATHER_BOOTS','301'],['铁头盔','IRON_HELMET','306'],['铁盔甲','IRON_CHESTPLATE','307'],['铁护腿','IRON_LEGGINGS','308'],['铁靴','IRON_BOOTS','309'],['钻石头盔','DIAMOND_HELMET','310'],['钻石胸甲','DIAMOND_CHESTPLATE','311'],['钻石护腿','DIAMOND_LEGGINGS','312'],['钻石靴','DIAMOND_BOOTS','313'],['金头盔','GOLD_HELMET','314'],['金护甲','GOLD_CHESTPLATE','315'],['金护腿','GOLD_LEGGINGS','316'],['金靴子','GOLD_BOOTS','317'],['矿车','MINECART','328'],['鞍','SADDLE','329'],['船','BOAT','330'],['运输矿车','STORAGE_MINECART','342'],['动力矿车','POWERED_MINECART','343'],['煤炭','COAL','263'],['木炭','COAL:1','263:1'],['钻石','DIAMOND','264'],['铁锭','IRON_INGOT','265'],['金锭','GOLD_INGOT','266'],['青金石','INK_SACK:4','351:4'],['萤石粉','GLOWSTONE_DUST','348'],['水瓶','POTION','373'],['恶魂之泪','GHAST_TEAR','370'],['金粒','GOLD_NUGGET','371'],['地狱庞','NETHER_STALK','372'],['玻璃瓶','GLASS_BOTTLE','374'],['蜘蛛眼','SPIDER_EYE','375'],['发酵的蜘蛛眼','FERMENTED_SPIDER_EYE','376'],['烈焰粉','BLAZE_POWDER','377'],['岩浆膏','MAGMA_CREAM','378'],['末影之眼','EYE_OF_ENDER','381'],['闪烁的西瓜','SPECKLED_MELON','382'],['画','PAINTING','321'],['告示牌','SIGN','323'],['木门','WOOD_DOOR','324'],['铁门','IRON_DOOR','330'],['红砖','CLAY_BRICK','336'],['粘土','CLAY_BALL','337'],['床','BED','355'],['酿造台','BREWING_STAND_ITEM','379'],['炼药锅','CAULDRON_ITEM','380'],['绿宝石','EMERALD','388'],['墨囊','INK_SACK','351'],['红色玫瑰','INK_SACK:1','351:1'],['仙人掌绿','INK_SACK:2','351:2'],['可可豆','INK_SACK:3','351:3'],['青金石','INK_SACK:4','351:4'],['紫色的染料','INK_SACK:5','351:5'],['青色的染料','INK_SACK:6','351:6'],['浅灰色的染料','INK_SACK:7','351:7'],['灰色的染料','INK_SACK:8','351:8'],['粉红色染料','INK_SACK:9','351:9'],['黄绿色染料','INK_SACK:10','351:10'],['蒲公英黄','INK_SACK:11','351:11'],['浅蓝色的染料','INK_SACK:12','351:12'],['品红染料','INK_SACK:13','351:13'],['橙色染料','INK_SACK:14','351:14'],['骨粉','INK_SACK:15','351:15'],['唱片C418-13','GOLD_RECORD','2256'],['唱片C418-cat','GREEN_RECORD','2257'],['唱片C418-blocks','RECORD_3','2258'],['唱片C418-chirp','RECORD_4','2259'],['唱片C418-far','RECORD_5','2260'],['唱片C418-mall','RECORD_6','2261'],['唱片C418-mellohi','RECORD_7','2262'],['唱片C418-satl','RECORD_8','2263'],['唱片C418-strad','RECORD_9','2264'],['唱片C418-ward','RECORD_10','2265'],['唱片C418-11','RECORD_11','2266'],['唱片C418-wait','RECORD_12','2267'],['箭','ARROW','262'],['木棍','STICK','280'],['线','STRING','287'],['羽毛','FEATHER','288'],['火药','SULPHUR','289'],['燧石','FLINT','318'],['雪球','SNOW_BALL','332'],['皮革','LEATHER','334'],['甘蔗','SUGAR_CANE','338'],['纸','PAPER','339'],['书','BOOK','340'],['粘液球','SLIME_BALL','341'],['鸡蛋','EGG','344'],['骨头','BONE','352'],['腐肉','ROTTEN_FLESH','367'],['末影珍珠','ENDER_PEARL','368'],['火焰棒','BLAZE_ROD','369'],['书与笔','BOOK_AND_QUILL','386'],['成书','WRITTEN_BOOK','387'],['红石','REDSTONE','331'],['红石中继器','DIODE','356'],['红石比较器','0404']]#line:18
cout =""#line:27
ender =""#line:28
err =""#line:29
def rerr (O0OOO00OOO000O0O0 ):#line:30
    global err #line:31
    err +=O0OOO00OOO000O0O0 #line:32
    raise SyntaxError (O0OOO00OOO000O0O0 )#line:33
def addout (O00OO000OO0000O0O ):#line:35
    global cout #line:36
    cout +=O00OO000OO0000O0O #line:37
def addend (OOO0O0O000O0O0OO0 ):#line:38
    global ender #line:39
    ender +=OOO0O0O000O0O0OO0 #line:40
def 物品方块 (O00OOO0O0OOOOO00O ):#line:42
    O00O0OO00OO000OOO =_OO00OO00OOOO00O0O #line:43
    for OOOOOOO0O00O00OOO in O00O0OO00OO000OOO :#line:44
        if O00OOO0O0OOOOO00O in OOOOOOO0O00O00OOO :#line:45
            O0OOO000O0OOO0000 =OOOOOOO0O00O00OOO [1 ].replace (':'," ")#line:46
            if " "in O0OOO000O0OOO0000 :#line:47
                OOO00000O0O0O0000 =O0OOO000O0OOO0000 #line:48
            else :#line:49
                OOO00000O0O0O0000 =O0OOO000O0OOO0000 +" 0"#line:50
            if " "in O0OOO000O0OOO0000 :#line:52
                OO0000O00OOO00OOO ,O0O0OO00O0O000O00 ,O0OO00OO0OO0OOOO0 =O0OOO000O0OOO0000 .partition (' ')#line:53
            else :#line:54
                OO0000O00OOO00OOO =O0OOO000O0OOO0000 #line:55
            return ['#ITEM',OOO00000O0O0O0000 ,OO0000O00OOO00OOO ]#line:56
    rerr ('没有该物品'+O00OOO0O0OOOOO00O )#line:57
def 生物类型 (O00OO00O00O00OO0O ):#line:59
    OOO0000O0O00000O0 =_OOOO000OO00O0O0O0 #line:60
    for O0O0O00OOOO0O00OO in OOO0000O0O00000O0 :#line:61
        if O00OO00O00O00OO0O in O0O0O00OOOO0O00OO :#line:62
            O0O0OO00OO0O0O000 =O0O0O00OOOO0O00OO [1 ]#line:63
            return ["#ET",O0O0OO00OO0O0O000 ]#line:64
    rerr ('没有该实体'+O00OO00O00O00OO0O )#line:65
def 取实体集_全部玩家 ():#line:67
    return ["#ELS",'@e[type=player]']#line:68
def 构建空间_对角坐标 (O0OO0O0OO0000OOO0 ,O000O00OOO0O0OO0O ,OOOOO0O0000000000 ,O0O0000OOOOO000O0 ,OO000OOOO00000OOO ,OOO000OO00OO00O00 ):#line:70
    return ['#BOX',"",O0OO0O0OO0000OOO0 ,O000O00OOO0O0OO0O ,OOOOO0O0000000000 ,O0O0000OOOOO000O0 ,OO000OOOO00000OOO ,OOO000OO00OO00O00 ]#line:71
def 构建位置_坐标 (OOOOOOO0O0OOOO00O ,O0OOO0O00OOO000OO ,OO000000O00OO0OO0 ):#line:73
    return ['#LOX',"",OOOOOOO0O0OOOO00O ,O0OOO0O00OOO000OO ,OO000000O00OO0OO0 ]#line:74
def 取实体集_玩家名字 (O0000OO0O00000OO0 ):#line:76
    return ["#ELS",'@e[type=player,name="'+O0000OO0O00000OO0 +'"]']#line:77
def 取实体集_实体名字 (O000OO000O000O000 ):#line:79
    return ["#ELS",'@e[name="'+O000OO000O000O000 +'"]']#line:80
def 取实体集_计分板分数 (O0OOOO00OO00OO0OO ,O00O000O0OO00O0O0 ):#line:82
    return ["#ELS",'@e[scores={'+O0OOOO00OO00OO0OO +'='+str (O00O000O0OO00O0O0 )+'}]']#line:83
def 取单个实体_实体集_默认 (O00000O0OO0OOOO0O ):#line:86
    if O00000O0OO0OOOO0O [0 ]=="#ELS":#line:87
        return ['#AE',O00000O0OO0OOOO0O [1 ].replace (']',',c=1]')]#line:88
    else :#line:89
        rerr ("不是实体集")#line:90
def 取实体集_矩形空间 (O00OOOOOOO000000O ):#line:92
    if O00OOOOOOO000000O [0 ]=='#BOX':#line:93
        if O00OOOOOOO000000O [1 ]=="":#line:94
            O0O00O0000OO0OO00 ="temp"+str (random .randint (0 ,10000 ))#line:95
            addout ('[command]')#line:98
            addout ('tag ')#line:99
            addout ('@e[x='+str (O00OOOOOOO000000O [2 ])+',y='+str (O00OOOOOOO000000O [3 ])+',z='+str (O00OOOOOOO000000O [4 ])+',dx='+str (int (O00OOOOOOO000000O [5 ]-O00OOOOOOO000000O [2 ]))+',dy='+str (int (O00OOOOOOO000000O [6 ]-O00OOOOOOO000000O [3 ]))+',dz='+str (int (O00OOOOOOO000000O [7 ]-O00OOOOOOO000000O [4 ]))+']')#line:100
            addout (' add')#line:101
            addout (' '+str (O0O00O0000OO0OO00 ))#line:102
            addend ('[command]tag @e remove'+O0O00O0000OO0OO00 )#line:103
            return ["#ELS",'@e[tag="'+str (O0O00O0000OO0OO00 )+'"]']#line:105
        else :#line:106
            O0O00O0000OO0OO00 ="temp"+str (random .randint (0 ,10000 ))#line:107
            addout ('[command]')#line:110
            addout ('execute '+O00OOOOOOO000000O [1 ]+" ~ ~ ~ ")#line:111
            addout ('tag ')#line:112
            addout ('@e[x=~'+str (O00OOOOOOO000000O [2 ])+',y=~'+str (O00OOOOOOO000000O [3 ])+',z=~'+str (O00OOOOOOO000000O [4 ])+',dx='+str (int (O00OOOOOOO000000O [5 ]-O00OOOOOOO000000O [2 ]))+',dy='+str (int (O00OOOOOOO000000O [6 ]-O00OOOOOOO000000O [3 ]))+',dz='+str (int (O00OOOOOOO000000O [7 ]-O00OOOOOOO000000O [4 ]))+']')#line:113
            addout (' add')#line:114
            addout (' '+str (O0O00O0000OO0OO00 ))#line:115
            addend ('[command]tag @e remove'+O0O00O0000OO0OO00 )#line:116
            return ["#ELS",'@e[tag="'+str (O0O00O0000OO0OO00 )+'"]']#line:118
    else :#line:119
        rerr ("不是矩形空间")#line:120
def 构建矩形空间_相对单个实体坐标 (O0O0OOOOOOOOO0O0O ,OOOO00O0O000000OO ,O0OOO000000OOOO00 ,O0OOO00O00OO0OOOO ,OO0O0O0O0OO0O0OOO ,O0OO0O0OO0O0O0O0O ,OO0O0OOOOO00O00O0 ):#line:122
    if O0O0OOOOOOOOO0O0O [0 ]=="#AE":#line:123
        return ['#BOX',O0O0OOOOOOOOO0O0O [1 ],OOOO00O0O000000OO ,O0OOO000000OOOO00 ,O0OOO00O00OO0OOOO ,OO0O0O0O0OO0O0OOO ,O0OO0O0OO0O0O0O0O ,OO0O0OOOOO00O00O0 ]#line:124
    else :#line:125
        rerr ("不是单个实体")#line:126
def 构建位置_相对单个实体坐标 (O000O0O000O00000O ,OOO00O00000O00O00 ,OOO0OO000OOOOO0O0 ,OOO0O00O0OOO00O0O ):#line:128
    if O000O0O000O00000O [0 ]=="#AE":#line:129
        return ['#LOX',O000O0O000O00000O [1 ],OOO00O00000O00O00 ,OOO0OO000OOOOO0O0 ,OOO0O00O0OOO00O0O ]#line:130
    else :#line:131
        rerr ("不是单个实体")#line:132
def 取实体集_实体类型 (O0O0OO0OOOOOOOO0O ):#line:134
    if O0O0OO0OOOOOOOO0O [0 ]=="#ET":#line:135
        return ["#ELS",'@e[type="'+O0O0OO0OOOOOOOO0O [1 ]+'"]']#line:136
    rerr ('不是生物类型')#line:137
def 填充空间_矩形空间 (OOO0OOO00O0000O0O ,O0O0OOOOOOO0000O0 ):#line:138
    if not O0O0OOOOOOO0000O0 [0 ]=="#ITEM":#line:139
        rerr ("不是物品")#line:140
    O0O00OO0OOO00000O =_O00O0O00O0O0OOO0O ('<e> fill <x1> <y1> <z1> <x2> <y2> <z2> '+O0O0OOOOOOO0000O0 [1 ],OOO0OOO00O0000O0O )#line:141
    addout ('[command]'+O0O00OO0OOO00000O )#line:142
def 保存结构 (O00O00OOOO0OO0000 ,O0OO0OO0O000OOOOO ):#line:144
    OO0000000000O00OO ='<e> structure save '+O0OO0OO0O000OOOOO +' <x1> <y1> <z1> <x2> <y2> <z2> true disk true'#line:145
    OO00000OOOOO0O00O =_O00O0O00O0O0OOO0O (OO0000000000O00OO ,O00O00OOOO0OO0000 )#line:146
    addout ('[command]'+OO00000OOOOO0O00O )#line:147
def 载入结构 (OO0O000O0OO0000OO ,OO00O000O00O0O0O0 ):#line:149
    OOO000OOO00O000OO ='<e> structure load '+OO00O000O00O0O0O0 +' <x> <y> <z> 0_degrees none true true'#line:150
    O0OOOOOOOOOO0O000 =_OO00O000O0OO0OO00 (OOO000OOO00O000OO ,OO0O000O0OO0000OO )#line:151
    addout ('[command]'+O0OOOOOOOOOO0O000 )#line:152
def 放置方块_位置 (O0000OO000OOO00OO ,O0O0O0O0000O00OO0 ):#line:154
    if not O0O0O0O0000O00OO0 [0 ]=="#ITEM":#line:155
        rerr ("不是物品")#line:156
    O0O00O0O0O00OOOOO =_OO00O000O0OO0OO00 ('<e> setblock <x> <y> <z> '+O0O0O0O0000O00OO0 [1 ],O0000OO000OOO00OO )#line:157
    addout ('[command]'+O0O00O0O0O00OOOOO )#line:158
def 生成生物_位置_名字 (O000O000OO000O0O0 ,O00OOO0OO000000OO ,OOOOO0O0O0OOOOOO0 =""):#line:160
    if not item [0 ]=="#ITEM":#line:161
        rerr ("不是物品")#line:162
    if O00OOO0OO000000OO [0 ]=="#ET":#line:163
        O0OO00O0O00OO00O0 =_OO00O000O0OO0OO00 ('<e> summon '+O00OOO0OO000000OO [1 ]+" "+OOOOO0O0O0OOOOOO0 +' <x> <y> <z> ',O000O000OO000O0O0 )#line:164
        addout ('[command]'+O0OO00O0O00OO00O0 )#line:165
    rerr ('不是生物类型')#line:166
def 填充空间_替换_矩形空间 (O00OOOO0O000OO000 ,OO0000OO00O0OOO0O ,OO0OO00O0O0O0O00O ):#line:169
    if not OO0000OO00O0OOO0O [0 ]=="#ITEM":#line:170
        rerr ("不是物品")#line:171
    if not OO0OO00O0O0O0O00O [0 ]=="#ITEM":#line:172
        rerr ("不是物品")#line:173
    OOO00O00OO0OOO000 =_O00O0O00O0O0OOO0O ('<e> fill <x1> <y1> <z1> <x2> <y2> <z2> '+OO0000OO00O0OOO0O [1 ]+" replace "+OO0OO00O0O0O0O00O [2 ],O00OOOO0O000OO000 )#line:174
    addout ('[command]'+OOO00O00OO0OOO000 )#line:175
def 杀死实体 (OOO000OO0O000O000 ):#line:177
    if OOO000OO0O000O000 [0 ]=="#AE"or OOO000OO0O000O000 [0 ]=='#ELS':#line:178
        OOOOOO00OO0O0O00O ='kill '+OOO000OO0O000O000 [1 ]#line:179
        addout ('[command]'+OOOOOO00OO0O0O00O )#line:180
    else :#line:181
        rerr ("不是实体(集)")#line:182
def 传送实体到位置 (OO0O000OOO0O00O00 ,OOOO000OOOO0O00OO ):#line:184
    if OO0O000OOO0O00O00 [0 ]=="#AE"or OO0O000OOO0O00O00 [0 ]=='#ELS':#line:185
        O0OO0O0OOO000O0O0 ='<e> tp '+OO0O000OOO0O00O00 [1 ]+" <x> <y> <z>"#line:186
        O0OO0O0OOO000O0O0 =_OO00O000O0OO0OO00 (O0OO0O0OOO000O0O0 ,OOOO000OOOO0O00OO )#line:187
        addout ('[command]'+O0OO0O0OOO000O0O0 )#line:188
    else :#line:189
        rerr ("不是实体(集)")#line:190
def 实体集交集 (O0OOO000OOOO00OO0 ,OO00OOO0OOO0OOO0O ):#line:192
    if (O0OOO000OOOO00OO0 [0 ]=="#AE"or O0OOO000OOOO00OO0 [0 ]=='#ELS')and (OO00OOO0OOO0OOO0O [0 ]=="#AE"or OO00OOO0OOO0OOO0O [0 ]=='#ELS'):#line:193
        O00O0O0000OO000OO ,O00O000O0O0OO00OO ,OOOO0O000OO0OO00O =O0OOO000OOOO00OO0 [1 ].partition ('[')#line:194
        OOOO0O000OO0OO00O =OOOO0O000OO0OO00O .replace (']',"")#line:195
        O00O0O0000OO000OO ,O00O000O0O0OO00OO ,OO00O0OOOOO0OOO00 =OO00OOO0OOO0OOO0O [1 ].partition ('[')#line:197
        OO00O0OOOOO0OOO00 =OO00O0OOOOO0OOO00 .replace (']',"")#line:198
        OOOOO0OO000000O0O =OOOO0O000OO0OO00O +","+OO00O0OOOOO0OOO00 #line:200
        OOOOO0OO000000O0O =OOOOO0OO000000O0O .replace (",,",",")#line:201
        OO0000O00000OOOOO =OOOOO0OO000000O0O .split (',')#line:202
        O0O00OOOO0O0OO000 ='@e['#line:203
        for OO0OO00O0OOOOOO0O in OO0000O00000OOOOO :#line:204
            if not OO0OO00O0OOOOOO0O in O0O00OOOO0O0OO000 :#line:205
                O0O00OOOO0O0OO000 +=","+OO0OO00O0OOOOOO0O #line:206
        O0O00OOOO0O0OO000 =O0O00OOOO0O0OO000 .replace ('@e[,','@e[')#line:207
        O0O00OOOO0O0OO000 +="]"#line:208
        return (['#ELS',O0O00OOOO0O0OO000 ])#line:209
    else :#line:210
        rerr ("不是实体(集)")#line:211
def 实体集并集 (O000OOO0OO000O00O ,O0OOOO0O000O00O00 ):#line:213
    if (O000OOO0OO000O00O [0 ]=="#AE"or O000OOO0OO000O00O [0 ]=='#ELS')and (O0OOOO0O000O00O00 [0 ]=="#AE"or O0OOOO0O000O00O00 [0 ]=='#ELS'):#line:214
        OOO0000O00OO0OO00 ="temp"+str (random .randint (0 ,10000 ))#line:215
        addout ('[command]tag '+O000OOO0OO000O00O [1 ]+' add '+OOO0000O00OO0OO00 )#line:217
        addout ('[command]tag '+O0OOOO0O000O00O00 [1 ]+' add '+OOO0000O00OO0OO00 )#line:218
        addend ('[command]tag @e remove'+OOO0000O00OO0OO00 )#line:219
        return (['#ELS','@e[tag='+OOO0000O00OO0OO00 +']'])#line:220
    else :#line:221
        rerr ("不是实体(集)")#line:222
def 计分项_增加 (O0OO0OOO0O0O0O00O ,O0O00000O00O00OO0 ,O0O0OOOOO0OO00OO0 ):#line:224
    if not (O0O00000O00O00OO0 [0 ]=="#AE"or O0O00000O00O00OO0 [0 ]=='#ELS'):#line:225
         rerr ("不是实体(集)")#line:226
    addout ('[command]scoreboard players add '+O0O00000O00O00OO0 [1 ]+" "+O0OO0OOO0O0O0O00O +" "+str (O0O0OOOOO0OO00OO0 ))#line:227
def 计分项_增加_文本玩家 (OO0O000O00OO00OO0 ,O000000OO00O0OO0O ,O00O00O0O0O00O0OO ):#line:228
    addout ('[command]scoreboard players add '+O000000OO00O0OO0O +" "+OO0O000O00OO00OO0 +" "+str (O00O00O0O0O00O0OO ))#line:229
def 计分项_设置 (O0000OOOO0000O00O ,O0OO00OO0O00OO0OO ,O00O000O0OO0O0OOO ):#line:230
    if not (O0OO00OO0O00OO0OO [0 ]=="#AE"or O0OO00OO0O00OO0OO [0 ]=='#ELS'):#line:231
         rerr ("不是实体(集)")#line:232
    addout ('[command]scoreboard players set '+O0OO00OO0O00OO0OO [1 ]+" "+O0000OOOO0000O00O +" "+str (O00O000O0OO0O0OOO ))#line:233
def 计分项_设置_文本玩家 (OOO0OO00O000OOOO0 ,OOO000OO00OO0O0O0 ,OO00OO0OOO0OO000O ):#line:234
    addout ('[command]scoreboard players set '+OOO000OO00OO0O0O0 +" "+OOO0OO00O000OOOO0 +" "+str (OO00OO0OOO0OO000O ))#line:235
def 计分项_清除 (OOO0OOO00OO0O0OO0 ,OOOOOO0O000OO0O00 ):#line:236
    if not (OOOOOO0O000OO0O00 [0 ]=="#AE"or OOOOOO0O000OO0O00 [0 ]=='#ELS'):#line:237
         rerr ("不是实体(集)")#line:238
    addout ('[command]scoreboard players reset '+OOOOOO0O000OO0O00 [1 ]+" "+OOO0OOO00OO0O0OO0 )#line:239
def 计分项_清除_文本玩家 (OOOO00OO0O0OOOOOO ,OO0OO0OOOO000O0OO ):#line:240
    addout ('[command]scoreboard players reset '+OO0OO0OOOO000O0OO +" "+OOOO00OO0O0OOOOOO )#line:241
def 添加计分项 (O000000OOOO00O000 ,O000O0O0O0OOOOOOO ):#line:242
    addout ("[command]scoreboard objectives add "+O000000OOOO00O000 +" dummy "+O000O0O0O0OOOOOOO )#line:243
def 删除计分项 (O0000OO000O0O00OO ):#line:244
    addout ('[command]scoreboard objectives remove '+O0000OO000O0O00OO )#line:245
def 设置计分项边栏显示 (O000000OOO0OO0O00 ):#line:246
    addout ('[command]scoreboard objectives setdisplay sidebar '+O000000OOO0OO0O00 )#line:247
def 设置计分项菜单界面显示 (O00OOO0O0OOOOO000 ):#line:248
    addout ('[command]scoreboard objectives setdisplay list '+O00OOO0O0OOOOO000 )#line:249
def 设置计分项名字下方显示 (O0000OO00OO0OOOOO ):#line:250
    addout ('[command]scoreboard objectives setdisplay belowname '+O0000OO00OO0OOOOO )#line:251
def 取实体集_实体_距离 (O0OO00OOOOO0000OO ,OO000O0OOO000O00O ):#line:252
    if not (O0OO00OOOOO0000OO [0 ]=="#AE"or O0OO00OOOOO0000OO [0 ]=='#ELS'):#line:253
         rerr ("不是实体(集)")#line:254
    OO000OOOO0000O000 ="temp"+str (random .randint (0 ,10000 ))#line:255
    addout ('[command]execute '+O0OO00OOOOO0000OO [1 ]+" ~ ~ ~ tag @e[rm=0.1,r="+str (OO000O0OOO000O00O )+"] add "+OO000OOOO0000O000 )#line:256
    addend ('[command]tag @e remove'+OO000OOOO0000O000 )#line:257
    return (['#ELS','@e[tag='+OO000OOOO0000O000 +']'])#line:258
def 构建Json (*O00O0O0OOO0O000OO ):#line:259
    OO0OOO00O0O0OOO00 ='##'#line:260
    for O000O00OO000O00OO in O00O0O0OOO0O000OO :#line:261
        if not O000O00OO000O00OO [0 ]=='#JW':#line:262
             rerr ("不是Json")#line:263
        OO0OOO00O0O0OOO00 +=','+O000O00OO000O00OO [1 ]#line:265
    OO0OOO00O0O0OOO00 +=']}'#line:266
    OO0OOO00O0O0OOO00 =OO0OOO00O0O0OOO00 .replace ('##,','{"rawtext": [')#line:267
    return (OO0OOO00O0O0OOO00 )#line:268
def 聊天栏_输出JSON (O0O0OOO00OO0O00OO ,O0OOO000OOOOOOOO0 ):#line:270
    if not (O0O0OOO00OO0O00OO [0 ]=="#AE"or O0O0OOO00OO0O00OO [0 ]=='#ELS'):#line:271
         rerr ("不是实体(集)")#line:272
    addout ('[command]tellraw '+O0O0OOO00OO0O00OO [1 ]+" "+O0OOO000OOOOOOOO0 )#line:274
def 标题_输出JSON (OOOOO000OO0OOO0OO ,OOOO0OOO000O00000 ,OOOO0O00OO0O00OO0 =""):#line:276
    if not (OOOOO000OO0OOO0OO [0 ]=="#AE"or OOOOO000OO0OOO0OO [0 ]=='#ELS'):#line:277
        print (OOOOO000OO0OOO0OO )#line:278
        rerr ("不是实体(集)")#line:279
    if (OOOO0O00OO0O00OO0 ):#line:280
        addout ('[command]titleraw '+OOOOO000OO0OOO0OO [1 ]+" subtitle "+OOOO0O00OO0O00OO0 )#line:281
    addout ('[command]titleraw '+OOOOO000OO0OOO0OO [1 ]+" title "+OOOO0OOO000O00000 )#line:282
def 标题底栏_输出JSON (O0O00O0OOOO0O0000 ,O00O0O00OOO0O0O00 ):#line:284
    if not (O0O00O0OOOO0O0000 [0 ]=="#AE"or O0O00O0OOOO0O0000 [0 ]=='#ELS'):#line:285
         rerr ("不是实体(集)")#line:286
    addout ('[command]titleraw '+O0O00O0OOOO0O0000 [1 ]+" actionbar "+O00O0O00OOO0O0O00 )#line:287
def Json文本 (O000OOOOO00000000 ):#line:290
    return ['#JW','{"text":"'+O000OOOOO00000000 +'"}']#line:291
def Json计分板分数__文本玩家 (O0OOO000O00O0O0O0 ,OOOO0OOOOOOO0O0O0 ):#line:292
    return ['#JW','{"score":{"name":"'+OOOO0OOOOOOO0O0O0 +'","objective":"'+O0OOO000O00O0O0O0 +'"}}']#line:293
def Json计分板分数 (O00O00OOO0OOOOO00 ,O00O0O0OOOO000O0O ):#line:294
    if not (O00O0O0OOOO000O0O [0 ]=="#AE"or O00O0O0OOOO000O0O [0 ]=='#ELS'):#line:295
         rerr ("不是实体(集)")#line:296
    return ['#JW','{"score":{"name":"'+O00O0O0OOOO000O0O [1 ]+'","objective":"'+O00O00OOO0OOOOO00 +'"}}']#line:297
def _O00O0O00O0O0OOO0O (OOO0OO000O0OO0O0O ,O00O00O00000O000O ):#line:300
    if not O00O00O00000O000O [0 ]=="#BOX":#line:302
        rerr ("不是矩形空间")#line:303
    O00OO000O000OOO00 =OOO0OO000O0OO0O0O #line:304
    if O00O00O00000O000O [1 ]=="":#line:305
        OOO0OO000O0OO0O0O =OOO0OO000O0OO0O0O .replace ('<e>',"")#line:306
    else :#line:307
        OOO0OO000O0OO0O0O =OOO0OO000O0OO0O0O .replace ('<e>','execute '+O00O00O00000O000O [1 ]+" ~ ~ ~ ")#line:308
        OOO0OO000O0OO0O0O =OOO0OO000O0OO0O0O .replace ('<',"~<")#line:309
    OOO0OO000O0OO0O0O =OOO0OO000O0OO0O0O .replace ('<x1>',str (O00O00O00000O000O [2 ]))#line:310
    OOO0OO000O0OO0O0O =OOO0OO000O0OO0O0O .replace ('<y1>',str (O00O00O00000O000O [3 ]))#line:311
    OOO0OO000O0OO0O0O =OOO0OO000O0OO0O0O .replace ('<z1>',str (O00O00O00000O000O [4 ]))#line:312
    OOO0OO000O0OO0O0O =OOO0OO000O0OO0O0O .replace ('<x2>',str (O00O00O00000O000O [5 ]))#line:313
    OOO0OO000O0OO0O0O =OOO0OO000O0OO0O0O .replace ('<y2>',str (O00O00O00000O000O [6 ]))#line:314
    OOO0OO000O0OO0O0O =OOO0OO000O0OO0O0O .replace ('<z2>',str (O00O00O00000O000O [7 ]))#line:315
    return OOO0OO000O0OO0O0O #line:316
def _OO00O000O0OO0OO00 (OOO00O000O00OOO0O ,O000OOOO0O000000O ):#line:317
    if not O000OOOO0O000000O [0 ]=="#LOX":#line:319
        rerr ("不是位置")#line:320
    O000OO00O0O00OOO0 =OOO00O000O00OOO0O #line:321
    if O000OOOO0O000000O [1 ]=="":#line:322
        OOO00O000O00OOO0O =OOO00O000O00OOO0O .replace ('<e>',"")#line:323
    else :#line:324
        OOO00O000O00OOO0O =OOO00O000O00OOO0O .replace ('<e>','execute '+O000OOOO0O000000O [1 ]+" ~ ~ ~ ")#line:325
        OOO00O000O00OOO0O =OOO00O000O00OOO0O .replace ('<',"~<")#line:326
    OOO00O000O00OOO0O =OOO00O000O00OOO0O .replace ('<x>',str (O000OOOO0O000000O [2 ]))#line:327
    OOO00O000O00OOO0O =OOO00O000O00OOO0O .replace ('<y>',str (O000OOOO0O000000O [3 ]))#line:328
    OOO00O000O00OOO0O =OOO00O000O00OOO0O .replace ('<z>',str (O000OOOO0O000000O [4 ]))#line:329
    return OOO00O000O00OOO0O #line:330
import base64 #line:388
def Run (O00OO00OO0O00OO00 ):#line:389
    global cout #line:390
    global ender #line:391
    global err #line:392
    cout =""#line:393
    ender =""#line:394
    err =""#line:395
    OOO00O0OO000O000O =['def','os','+','\\','/','import','&','@','[]',"*",":","."]#line:397
    for OO000O00OOOO00OOO in OOO00O0OO000O000O :#line:398
        O00OO00OO0O00OO00 =O00OO00OO0O00OO00 .replace (OO000O00OOOO00OOO ,"")#line:399
    print (O00OO00OO0O00OO00 )#line:400
    try :#line:402
        exec (O00OO00OO0O00OO00 )#line:403
    except :#line:404
        OOO00OO0000OOOO0O ="语法错误 : "+err #line:405
    else :#line:406
        OOO00OO0000OOOO0O =cout +ender #line:407
        OOO00OO0000OOOO0O =OOO00OO0000OOOO0O .replace ('  '," ")#line:408
        OOO00OO0000OOOO0O =OOO00OO0000OOOO0O .replace (' [command]','[command]')#line:409
        OOO00OO0000OOOO0O =OOO00OO0000OOOO0O .replace ('[command] ','[command]')#line:410
        OOO00OO0000OOOO0O =OOO00OO0000OOOO0O .replace ('[command]','\n')#line:411
    return OOO00OO0000OOOO0O #line:412
bb =aa =""#line:415
while True :#line:416
    aa =input ()#line:417
    bb +=aa #line:418
    if aa =="":#line:419
        cc =Run (bb )#line:420
        bb =""#line:421
        aa =""#line:422
        print (cc )#line:423
