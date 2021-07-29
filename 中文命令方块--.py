#!/usr/bin/env python
import random #line:12
import os #line:13
_OOOO0O000OO0O00OO =['烈焰人','blaze'],['顶部蜘蛛','cave_spider'],['苦力怕','creeper'],['溺尸','drowned'],['远古守卫者','elder_guardian'],['末影龙','ender_dragon'],['末影人','enderman'],['末影螨','endermite'],['唤魔者','evoker'],['恶魂','ghast'],['巨人','giant'],['守卫者','guardian'],['尸壳','husk'],['劫掠兽','ravager'],['幻术师','illusioner'],['岩浆怪','magma_cube'],['幻翼','phantom'],['掠夺者','pillager'],['河豚','pufferfish'],['潜影贝','shulker'],['蠹虫','silverfish'],['骷髅','skeleton'],['史莱姆','slime'],['蜘蛛','spider'],['流浪者','stray'],['恼鬼','vex'],['卫道士','vindicator'],['女巫','witch'],['凋灵','wither'],['凋灵骷髅','wither_skeleton'],['僵尸','zombie'],['僵尸猪人','zombie_pigman'],['僵尸村民','zombie_villager'],['蝙蝠','bat'],['猫','cat'],['鸡','chicken'],['鳕鱼','cod'],['牛','cow'],['海豚','dolphin'],['驴','donkey'],['马','horse'],['铁傀儡','iron_golem'],['羊驼','llama'],['哞菇','mooshroom'],['骡','mule'],['豹猫','ocelot'],['熊猫','panda'],['鹦鹉','parrot'],['猪','pig'],['北极熊','polar_bear'],['兔子','rabbit'],['鲑鱼','salmon'],['羊','sheep'],['骷髅马','skeleton_horse'],['雪傀儡','snow_golem'],['鱿鱼','squid'],['热带鱼','tropical_fish'],['海龟','turtle'],['村民','villager'],['狼','wolf'],['僵尸马','zombie_horse'],['效果区域云','area_effect_cloud'],['拴绳','leash_knot'],['画','painting'],['物品展示框','item_frame'],['盔甲架','armor_stand'],['唤魔者尖牙','evoker_fangs'],['末地水晶','end_crystal'],['掷出的鸡蛋','egg'],['射出的箭或药箭','arrow'],['射出的光灵箭','spectral_arrow'],['三叉戟','trident'],['掷出的雪球','snowball'],['恶魂火球','fireball'],['烈焰人火球或火焰弹','small_fireball'],['掷出的末影珍珠','ender_pearl'],['掷出的末影之眼','eye_of_ender'],['扔出的药水','potion'],['掷出的附魔之瓶','experience_bottle'],['凋灵之首','wither_skull'],['烟花火箭','firework_rocket'],['潜影贝导弹','shulker_bullet'],['末影龙火球','dragon_fireball'],['羊驼的口水','llama_spit'],['命令方块矿车','command_block_minecart'],['船','boat'],['矿车','minecart'],['运输矿车','chest_minecart'],['动力矿车','furnace_minecart'],['TNT矿车','tnt_minecart'],['漏斗矿车','hopper_minecart'],['刷怪笼矿车','spawner_minecart'],['激活的TNT','tnt '],['掉落中的方块','falling_block'],['掉落的物品','item '],['经验球','experience_orb']#line:16
_O000O00OOO0O0OO00 =[['空气','AIR','0'],['石头','STONE','1'],['草块','GRASS','2'],['泥土','DIRT','3'],['圆石','COBBLESTONE','4'],['橡木木板','WOOD','5'],['云杉木板','WOOD:1','5:1'],['桦木木板','WOOD:2','5:2'],['丛林木板','WOOD:3','5:3'],['橡树树苗','SAPLING','6'],['云杉树苗','SAPLING:1','6:1'],['桦木树苗','SAPLING:2','6:2'],['丛林树苗','SAPLING:3','6:3'],['沙子','SAND','12'],['沙硕','GRAVEL','13'],['金矿石','GOLD_ORE','14'],['铁矿石','IRON_ORE','15'],['煤矿石','COAL_ORE','16'],['橡木','LOG','17'],['云杉木','LOG:1','17:1'],['白桦木','LOG:2','17:2'],['丛林木','LOG:3','17:3'],['橡木树叶','LEAVES','18'],['云杉树叶','LEAVES:1','18:1'],['白桦树叶','LEAVES:2','18:2'],['丛林树叶','LEAVES:3','18:3'],['玻璃','GLASS','20'],['青金石矿石','LAPIS_ORE','21'],['青金石块','LAPIS_BLOCK','22'],['发射器','DISPENSER','23'],['沙石','SANDSTONE','24'],['錾制沙石','SANDSTONE:1','24:1'],['平滑沙石','SANDSTONE:2','24:2'],['音符盒','NOTE_BLOCK','25'],['动力铁轨','POWERED_RAIL','27'],['探测铁轨','DETECTOR_RAIL','28'],['粘性活塞','PISTON_STICKY_BASE','29'],['灌木','LONG_GRASS','31'],['枯死的灌木','DEAD_BUSH','32'],['活塞','PISTON_BASE','33'],['白色羊毛','WOOL','35'],['橙色羊毛','WOOL:1','35:1'],['红色羊毛','WOOL:2','35:2'],['蓝色羊毛','WOOL:3','35:3'],['黄色羊毛','WOOL:4','35:4'],['灰色羊毛','WOOL:5','35:5'],['粉色羊毛','WOOL:6','35:6'],['灰色羊毛','WOOL:7','35:7'],['淡灰色羊毛','WOOL:8','35:8'],['青色羊毛','WOOL:9','35:9'],['紫色羊毛','WOOL:10','35:10'],['蓝色羊毛','WOOL:11','35:11'],['棕色羊毛','WOOL:12','35:12'],['深绿色羊毛','WOOL:13','35:13'],['红色羊毛','WOOL:14','35:14'],['黑色羊毛','WOOL:15','35:15'],['蒲公英','YELLOW_FLOWER','37'],['玫瑰','RED_ROSE','38'],['棕色蘑菇','BROWN_MUSHROOM','39'],['红色蘑菇','RED_MUSHROOM','40'],['金块','GOLD_BLOCK','41'],['铁块','IRON_BLOCK','42'],['石台阶','STEP','44'],['沙石台阶','STEP:1','44:1'],['木台阶','STEP:2','44:2'],['圆石台阶','STEP:3','44:3'],['砖台阶','STEP:4','44:4'],['石砖台阶','STEP:5','44:5'],['红砖','BRICK','45'],['TNT','TNT','46'],['书架','BOOKSHELF','47'],['苔石','MOSSY_COBBLESTONE','48'],['黑曜石','OBSIDIAN','49'],['火把','TORCH','50'],['橡木楼梯','WOOD_STAIRS','53'],['箱子','CHEST','54'],['钻石矿石','DIAMOND_ORE','56'],['钻石块','DIAMOND_BLOCK','57'],['工作台','WORKBENCH','58'],['熔炉','FURNACE','61'],['梯子','LADDER','65'],['铁轨','RAILS','66'],['石楼梯','COBBLESTONE_STAIRS','67'],['拉杆','LEVER','69'],['石压力板','STONE_PLATE','70'],['木压力板','WOOD_PLATE','72'],['红石矿石','REDSTONE_ORE','73'],['红石火把','REDSTONE_TORCH_ON','76'],['石按钮','STONE_BUTTON','77'],['冰','ICE','79'],['雪','SNOW_BLOCK','80'],['仙人掌','CACTUS','81'],['粘土','CLAY','82'],['唱片机','JUKEBOX','84'],['栅栏','FENCE','85'],['南瓜','PUMPKIN','86'],['地狱岩','NETHERRACK','87'],['灵魂沙','SOUL_SAND','88'],['萤石','GLOWSTONE','89'],['南瓜灯','JACK_O_LANTERN','91'],['活板门','TRAP_DOOR','96'],['石砖','SMOOTH_BRICK','98'],['苔石砖','SMOOTH_BRICK:1','98:1'],['裂石砖','SMOOTH_BRICK:2','98:2'],['錾制石砖','SMOOTH_BRICK:3','98:3'],['蘑菇','HUGE_MUSHROOM_1','99'],['蘑菇','HUGE_MUSHROOM_2','100'],['铁栅栏','IRON_FENCE','101'],['玻璃板','THIN_GLASS','102'],['西瓜','MELON_BLOCK','103'],['藤蔓','VINE','106'],['栅栏门','FENCE_GATE','107'],['砖楼梯','BRICK_STAIRS','108'],['石楼梯','SMOOTH_STAIRS','109'],['菌丝','MYCEL','110'],['睡莲','WATER_LILY','111'],['地狱砖块','NETHER_BRICK','112'],['地狱砖栅栏','NETHER_FENCE','113'],['地狱砖楼梯','NETHER_BRICK_STAIRS','114'],['附魔台','ENCHANTMENT_TABLE','116'],['末地石','ENDER_STON','121'],['龙蛋','DRAGON_EGG','122'],['红石灯','REDSTONE_LAMP_OFF','123'],['橡木台阶','WOOD_STEP','126'],['云杉台阶','WOOD_STEP:1','126:1'],['桦木台阶','WOOD_STEP:2','126:2'],['丛林台阶','WOOD_STEP:3','126:3'],['沙石楼梯','SANDSTONE_STAIRS','128'],['绿宝石矿石','EMERALD_ORE','129'],['末影箱','ENDER_CHEST','130'],['拌线钩','TRIPWIRE_HOOK','131'],['绿宝石矿石','EMERALD_BLOCK','133'],['云杉木楼梯','SPRUCE_WOOD_STAIRS','134'],['桦木楼梯','BIRCH_WOOD_STAIRS','135'],['丛林木楼梯','JUNGLE_WOOD_STAIRS','136'],['铁铲子','IRON_SPADE','256'],['铁镐','IRON_PICKAXE','257'],['铁斧','IRON_AXE','258'],['打火石','FLINT_AND_STEEL','259'],['弓','BOW','261'],['铁剑','IRON_SWORD','267'],['木剑','WOOD_SWORD','268'],['木铲','WOOD_SPADE','269'],['木镐','WOOD_PICKAXE','270'],['木斧','WOOD_AXE','271'],['石剑','STONE_SWORD','272'],['石铲','STONE_SPADE','273'],['石镐','STONE_PICKAXE','274'],['石斧','STONE_AXE','275'],['金剑','GOLD_SWORD','283'],['金铲','GOLD_SPADE','284'],['金镐','GOLD_PICKAXE','285'],['金斧','GOLD_AXE','286'],['木锄','WOOD_HOE','290'],['石锄','STONE_HOE','291'],['铁锄','IRON_HOE','292'],['钻石锄','DIAMOND_HOE','293'],['金锄','GOLD_HOE','294'],['钻石剑','DIAMOND_SWORD','276'],['钻石铲','DIAMOND_SPADE','277'],['钻石镐','DIAMOND_PICKAXE','278'],['钻石斧','DIAMOND_AXE','279'],['桶','BUCKET','325'],['水桶','WATER_BUCKET','326'],['岩浆桶','LAVA_BUCKET','327'],['指南针','COMPASS','345'],['钓鱼竿','FISHING_ROD','346'],['钟','WATCH','347'],['空地图','MAP','358'],['剪刀','SHEARS','359'],['火焰弹','FIREBALL','385'],['苹果','APPLE','260'],['碗','BOWL','281'],['炖蘑菇','MUSHROOM_SOUP','282'],['小麦种子','SEEDS','295'],['小麦','WHEAT','296'],['面包','BREAD','297'],['生猪排','PORK','319'],['熟猪排','GRILLED_PORK','320'],['金苹果','GOLDEN_APPLE','322'],['牛奶','MILK_BUCKET','335'],['生鱼','RAW_FISH','349'],['熟鱼','COOKED_FISH','350'],['糖','SUGAR','353'],['蛋糕','CAKE','354'],['曲奇','COOKIE','357'],['西瓜','MELON','360'],['南瓜种子','PUMPKIN_SEEDS','361'],['西瓜种子','MELON_SEEDS','362'],['生牛肉','RAW_BEEF','363'],['牛排','COOKED_BEEF','364'],['生鸡肉','RAW_CHICKEN','365'],['熟鸡肉','COOKED_CHICKEN','366'],['皮革帽子','LEATHER_HELMET','298'],['皮革外衣','LEATHER_CHESTPLATE','299'],['皮革裤子','LEATHER_LEGGINGS','300'],['皮靴','LEATHER_BOOTS','301'],['铁头盔','IRON_HELMET','306'],['铁盔甲','IRON_CHESTPLATE','307'],['铁护腿','IRON_LEGGINGS','308'],['铁靴','IRON_BOOTS','309'],['钻石头盔','DIAMOND_HELMET','310'],['钻石胸甲','DIAMOND_CHESTPLATE','311'],['钻石护腿','DIAMOND_LEGGINGS','312'],['钻石靴','DIAMOND_BOOTS','313'],['金头盔','GOLD_HELMET','314'],['金护甲','GOLD_CHESTPLATE','315'],['金护腿','GOLD_LEGGINGS','316'],['金靴子','GOLD_BOOTS','317'],['矿车','MINECART','328'],['鞍','SADDLE','329'],['船','BOAT','330'],['运输矿车','STORAGE_MINECART','342'],['动力矿车','POWERED_MINECART','343'],['煤炭','COAL','263'],['木炭','COAL:1','263:1'],['钻石','DIAMOND','264'],['铁锭','IRON_INGOT','265'],['金锭','GOLD_INGOT','266'],['青金石','INK_SACK:4','351:4'],['萤石粉','GLOWSTONE_DUST','348'],['水瓶','POTION','373'],['恶魂之泪','GHAST_TEAR','370'],['金粒','GOLD_NUGGET','371'],['地狱庞','NETHER_STALK','372'],['玻璃瓶','GLASS_BOTTLE','374'],['蜘蛛眼','SPIDER_EYE','375'],['发酵的蜘蛛眼','FERMENTED_SPIDER_EYE','376'],['烈焰粉','BLAZE_POWDER','377'],['岩浆膏','MAGMA_CREAM','378'],['末影之眼','EYE_OF_ENDER','381'],['闪烁的西瓜','SPECKLED_MELON','382'],['画','PAINTING','321'],['告示牌','SIGN','323'],['木门','WOOD_DOOR','324'],['铁门','IRON_DOOR','330'],['红砖','CLAY_BRICK','336'],['粘土','CLAY_BALL','337'],['床','BED','355'],['酿造台','BREWING_STAND_ITEM','379'],['炼药锅','CAULDRON_ITEM','380'],['绿宝石','EMERALD','388'],['墨囊','INK_SACK','351'],['红色玫瑰','INK_SACK:1','351:1'],['仙人掌绿','INK_SACK:2','351:2'],['可可豆','INK_SACK:3','351:3'],['青金石','INK_SACK:4','351:4'],['紫色的染料','INK_SACK:5','351:5'],['青色的染料','INK_SACK:6','351:6'],['浅灰色的染料','INK_SACK:7','351:7'],['灰色的染料','INK_SACK:8','351:8'],['粉红色染料','INK_SACK:9','351:9'],['黄绿色染料','INK_SACK:10','351:10'],['蒲公英黄','INK_SACK:11','351:11'],['浅蓝色的染料','INK_SACK:12','351:12'],['品红染料','INK_SACK:13','351:13'],['橙色染料','INK_SACK:14','351:14'],['骨粉','INK_SACK:15','351:15'],['唱片C418-13','GOLD_RECORD','2256'],['唱片C418-cat','GREEN_RECORD','2257'],['唱片C418-blocks','RECORD_3','2258'],['唱片C418-chirp','RECORD_4','2259'],['唱片C418-far','RECORD_5','2260'],['唱片C418-mall','RECORD_6','2261'],['唱片C418-mellohi','RECORD_7','2262'],['唱片C418-satl','RECORD_8','2263'],['唱片C418-strad','RECORD_9','2264'],['唱片C418-ward','RECORD_10','2265'],['唱片C418-11','RECORD_11','2266'],['唱片C418-wait','RECORD_12','2267'],['箭','ARROW','262'],['木棍','STICK','280'],['线','STRING','287'],['羽毛','FEATHER','288'],['火药','SULPHUR','289'],['燧石','FLINT','318'],['雪球','SNOW_BALL','332'],['皮革','LEATHER','334'],['甘蔗','SUGAR_CANE','338'],['纸','PAPER','339'],['书','BOOK','340'],['粘液球','SLIME_BALL','341'],['鸡蛋','EGG','344'],['骨头','BONE','352'],['腐肉','ROTTEN_FLESH','367'],['末影珍珠','ENDER_PEARL','368'],['火焰棒','BLAZE_ROD','369'],['书与笔','BOOK_AND_QUILL','386'],['成书','WRITTEN_BOOK','387'],['红石','REDSTONE','331'],['红石中继器','DIODE','356'],['红石比较器','0404']]#line:17
cout =""#line:26
ender =""#line:27
err =""#line:28
def _OOO0O0OOOOOO0O0OO (O0O00000O0O0O0OOO ):#line:29
    global err #line:30
    err +=O0O00000O0O0O0OOO #line:31
    raise SyntaxError (O0O00000O0O0O0OOO )#line:32
def _O0OO0O0OOO0O0OO00 (OOOO00O0OOO00O000 ):#line:34
    global cout #line:35
    cout +=OOOO00O0OOO00O000 #line:36
def _OO00OOOO0O0OO0OOO (O0OO00OO0OO000O0O ):#line:37
    global ender #line:38
    ender +=O0OO00OO0OO000O0O #line:39
def 物品方块 (OO00OOO00O0O0000O ):#line:41
    O0O0OO0O0OO00O0O0 =_O000O00OOO0O0OO00 #line:42
    for O0OO00000000OO0OO in O0O0OO0O0OO00O0O0 :#line:43
        if OO00OOO00O0O0000O in O0OO00000000OO0OO :#line:44
            O00O0OO00O00O0OO0 =O0OO00000000OO0OO [1 ].replace (':'," ")#line:45
            if " "in O00O0OO00O00O0OO0 :#line:46
                OO00OOO000OO0OO00 =O00O0OO00O00O0OO0 #line:47
            else :#line:48
                OO00OOO000OO0OO00 =O00O0OO00O00O0OO0 +" 0"#line:49
            if " "in O00O0OO00O00O0OO0 :#line:51
                O000OO0O0OO00OOO0 ,OOO0O000000000O0O ,OOO000OO00O0OO00O =O00O0OO00O00O0OO0 .partition (' ')#line:52
            else :#line:53
                O000OO0O0OO00OOO0 =O00O0OO00O00O0OO0 #line:54
            return ['#ITEM',OO00OOO000OO0OO00 ,O000OO0O0OO00OOO0 ]#line:55
    _OOO0O0OOOOOO0O0OO ('没有该物品'+OO00OOO00O0O0000O )#line:56
def 生物类型 (OO0OOO000000O000O ):#line:58
    OOO00O000OOOO00OO =_OOOO0O000OO0O00OO #line:59
    for O00OOOOOOOO0OOO0O in OOO00O000OOOO00OO :#line:60
        if OO0OOO000000O000O in O00OOOOOOOO0OOO0O :#line:61
            O00O0O000O000OO0O =O00OOOOOOOO0OOO0O [1 ]#line:62
            return ["#ET",O00O0O000O000OO0O ]#line:63
    _OOO0O0OOOOOO0O0OO ('没有该实体'+OO0OOO000000O000O )#line:64
def 取实体集_全部玩家 ():#line:66
    return ["#ELS",'@e[type=player]']#line:67
def 构建空间_对角坐标 (O0O0000OOOOO000O0 ,O0O0O0OOOOOO00OO0 ,OO0O0000OO000O0OO ,O0000OO0O00O000O0 ,O0OO0OOO0O0OOO0OO ,O000OOO0OOO000O00 ):#line:69
    return ['#BOX',"",O0O0000OOOOO000O0 ,O0O0O0OOOOOO00OO0 ,OO0O0000OO000O0OO ,O0000OO0O00O000O0 ,O0OO0OOO0O0OOO0OO ,O000OOO0OOO000O00 ]#line:70
def 构建位置_坐标 (OO00O0000OOOO0OOO ,OOO0O0OOOO0O0OO00 ,O000O000O00O00O0O ):#line:72
    return ['#LOX',"",OO00O0000OOOO0OOO ,OOO0O0OOOO0O0OO00 ,O000O000O00O00O0O ]#line:73
def 取实体集_玩家名字 (O0O00OOO0OO00OO0O ):#line:75
    return ["#ELS",'@e[type=player,name="'+O0O00OOO0OO00OO0O +'"]']#line:76
def 取实体集_实体名字 (OOOO00OO00000O000 ):#line:78
    return ["#ELS",'@e[name="'+OOOO00OO00000O000 +'"]']#line:79
def 取实体集_计分板分数 (OOO0OO000O0O0000O ,OOO00O000O000O00O ):#line:81
    return ["#ELS",'@e[scores={'+OOO0OO000O0O0000O +'='+str (OOO00O000O000O00O )+'}]']#line:82
def 取实体_实体集_一个 (OO00000OOO000OOOO ):#line:85
    if OO00000OOO000OOOO [0 ]=="#ELS":#line:86
        return ['#AE',OO00000OOO000OOOO [1 ].replace (']',',c=1]')]#line:87
    else :#line:88
        _OOO0O0OOOOOO0O0OO ("不是实体集")#line:89
def 取实体_实体集_遍历 (OO0OO0O00O0000000 ):#line:91
    if OO0OO0O00O0000000 [0 ]=="#ELS":#line:92
        return ['#AE',OO0OO0O00O0000000 [1 ]]#line:93
    else :#line:94
        _OOO0O0OOOOOO0O0OO ("不是实体集")#line:95
def 取实体集_矩形空间 (OOOO000O0O0O0000O ):#line:97
    if OOOO000O0O0O0000O [0 ]=='#BOX':#line:98
        if OOOO000O0O0O0000O [1 ]=="":#line:99
            O0O0O00O00OOOO0OO ="temp"+str (random .randint (0 ,10000 ))#line:100
            _O0OO0O0OOO0O0OO00 ('[command]')#line:103
            _O0OO0O0OOO0O0OO00 ('tag ')#line:104
            _O0OO0O0OOO0O0OO00 ('@e[x='+str (OOOO000O0O0O0000O [2 ])+',y='+str (OOOO000O0O0O0000O [3 ])+',z='+str (OOOO000O0O0O0000O [4 ])+',dx='+str (int (OOOO000O0O0O0000O [5 ]-OOOO000O0O0O0000O [2 ]))+',dy='+str (int (OOOO000O0O0O0000O [6 ]-OOOO000O0O0O0000O [3 ]))+',dz='+str (int (OOOO000O0O0O0000O [7 ]-OOOO000O0O0O0000O [4 ]))+']')#line:105
            _O0OO0O0OOO0O0OO00 (' add')#line:106
            _O0OO0O0OOO0O0OO00 (' '+str (O0O0O00O00OOOO0OO ))#line:107
            _OO00OOOO0O0OO0OOO ('[command]tag @e remove'+O0O0O00O00OOOO0OO )#line:108
            return ["#ELS",'@e[tag="'+str (O0O0O00O00OOOO0OO )+'"]']#line:110
        else :#line:111
            O0O0O00O00OOOO0OO ="temp"+str (random .randint (0 ,10000 ))#line:112
            _O0OO0O0OOO0O0OO00 ('[command]')#line:115
            _O0OO0O0OOO0O0OO00 ('execute '+OOOO000O0O0O0000O [1 ]+" ~ ~ ~ ")#line:116
            _O0OO0O0OOO0O0OO00 ('tag ')#line:117
            _O0OO0O0OOO0O0OO00 ('@e[x=~'+str (OOOO000O0O0O0000O [2 ])+',y=~'+str (OOOO000O0O0O0000O [3 ])+',z=~'+str (OOOO000O0O0O0000O [4 ])+',dx='+str (int (OOOO000O0O0O0000O [5 ]-OOOO000O0O0O0000O [2 ]))+',dy='+str (int (OOOO000O0O0O0000O [6 ]-OOOO000O0O0O0000O [3 ]))+',dz='+str (int (OOOO000O0O0O0000O [7 ]-OOOO000O0O0O0000O [4 ]))+']')#line:118
            _O0OO0O0OOO0O0OO00 (' add')#line:119
            _O0OO0O0OOO0O0OO00 (' '+str (O0O0O00O00OOOO0OO ))#line:120
            _OO00OOOO0O0OO0OOO ('[command]tag @e remove'+O0O0O00O00OOOO0OO )#line:121
            return ["#ELS",'@e[tag="'+str (O0O0O00O00OOOO0OO )+'"]']#line:123
    else :#line:124
        _OOO0O0OOOOOO0O0OO ("不是矩形空间")#line:125
def 构建矩形空间_相对实体坐标 (OOO00OOO00O00000O ,OOOO0000000OO0000 ,O00O0O0OOOOOOOOO0 ,OO0O00OOOO0O0OO0O ,O00O0O0OO000O0OO0 ,OO0O0000000O0OO00 ,OO0OO0OO0OOOO0O00 ):#line:127
    if OOO00OOO00O00000O [0 ]=="#AE":#line:128
        return ['#BOX',OOO00OOO00O00000O [1 ],OOOO0000000OO0000 ,O00O0O0OOOOOOOOO0 ,OO0O00OOOO0O0OO0O ,O00O0O0OO000O0OO0 ,OO0O0000000O0OO00 ,OO0OO0OO0OOOO0O00 ]#line:129
    else :#line:130
        _OOO0O0OOOOOO0O0OO ("不是实体")#line:131
def 构建位置_相对实体坐标 (O000O0O00O0O000OO ,OO00O0OO00O0O000O ,OO00O00OOO00OOO00 ,O0OOO0000O00OOO00 ):#line:133
    if O000O0O00O0O000OO [0 ]=="#AE":#line:134
        return ['#LOX',O000O0O00O0O000OO [1 ],OO00O0OO00O0O000O ,OO00O00OOO00OOO00 ,O0OOO0000O00OOO00 ]#line:135
    else :#line:136
        _OOO0O0OOOOOO0O0OO ("不是实体")#line:137
def 取实体集_实体类型 (OOOO0O0O0O0O00OOO ):#line:139
    if OOOO0O0O0O0O00OOO [0 ]=="#ET":#line:140
        return ["#ELS",'@e[type="'+OOOO0O0O0O0O00OOO [1 ]+'"]']#line:141
    _OOO0O0OOOOOO0O0OO ('不是生物类型')#line:142
def 填充空间_矩形空间 (OOO0OOOOOO0O00000 ,OOO00O0O0O0000000 ):#line:143
    if not OOO00O0O0O0000000 [0 ]=="#ITEM":#line:144
        _OOO0O0OOOOOO0O0OO ("不是物品")#line:145
    O00O00OO00O000O00 =_O0O00O0O0OOO0O000 ('<e> fill <x1> <y1> <z1> <x2> <y2> <z2> '+OOO00O0O0O0000000 [1 ],OOO0OOOOOO0O00000 )#line:146
    _O0OO0O0OOO0O0OO00 ('[command]'+O00O00OO00O000O00 )#line:147
def 保存结构 (OOOOO0O0OO000O00O ,O000O000O0O00O000 ):#line:149
    OOO0O0OOOO000O000 ='<e> structure save '+O000O000O0O00O000 +' <x1> <y1> <z1> <x2> <y2> <z2> true disk true'#line:150
    O00OO00O00O0O0OOO =_O0O00O0O0OOO0O000 (OOO0O0OOOO000O000 ,OOOOO0O0OO000O00O )#line:151
    _O0OO0O0OOO0O0OO00 ('[command]'+O00OO00O00O0O0OOO )#line:152
def 载入结构 (OO0OOOOOO00OOO000 ,OOOO00O0OO0OO0O0O ):#line:154
    O000OO000OO0000OO ='<e> structure load '+OOOO00O0OO0OO0O0O +' <x> <y> <z> 0_degrees none true true'#line:155
    OO00000000O00OOO0 =_OO000OOOO00OOOOOO (O000OO000OO0000OO ,OO0OOOOOO00OOO000 )#line:156
    _O0OO0O0OOO0O0OO00 ('[command]'+OO00000000O00OOO0 )#line:157
def 放置方块_位置 (OOO0OO0000O00OOOO ,OO00OOOOO0OO0O0OO ):#line:159
    if not OO00OOOOO0OO0O0OO [0 ]=="#ITEM":#line:160
        _OOO0O0OOOOOO0O0OO ("不是物品")#line:161
    OO0000O0OO00O00O0 =_OO000OOOO00OOOOOO ('<e> setblock <x> <y> <z> '+OO00OOOOO0OO0O0OO [1 ],OOO0OO0000O00OOOO )#line:162
    _O0OO0O0OOO0O0OO00 ('[command]'+OO0000O0OO00O00O0 )#line:163
def 生成生物_位置_名字 (OO0O00O00O0OOOOO0 ,OOOOO0OO00O000OOO ,OO0O00O0O000OO0OO =""):#line:165
    if not item [0 ]=="#ITEM":#line:166
        _OOO0O0OOOOOO0O0OO ("不是物品")#line:167
    if OOOOO0OO00O000OOO [0 ]=="#ET":#line:168
        OOOOOOOO0O00OOO00 =_OO000OOOO00OOOOOO ('<e> summon '+OOOOO0OO00O000OOO [1 ]+" "+OO0O00O0O000OO0OO +' <x> <y> <z> ',OO0O00O00O0OOOOO0 )#line:169
        _O0OO0O0OOO0O0OO00 ('[command]'+OOOOOOOO0O00OOO00 )#line:170
    _OOO0O0OOOOOO0O0OO ('不是生物类型')#line:171
def 填充空间_替换_矩形空间 (O00OO00O000OOO0O0 ,O00O0OOO0000O0OO0 ,OO000O0OOOO0O0O0O ):#line:174
    if not O00O0OOO0000O0OO0 [0 ]=="#ITEM":#line:175
        _OOO0O0OOOOOO0O0OO ("不是物品")#line:176
    if not OO000O0OOOO0O0O0O [0 ]=="#ITEM":#line:177
        _OOO0O0OOOOOO0O0OO ("不是物品")#line:178
    O0OOO0OO0O0O00O0O =_O0O00O0O0OOO0O000 ('<e> fill <x1> <y1> <z1> <x2> <y2> <z2> '+O00O0OOO0000O0OO0 [1 ]+" replace "+OO000O0OOOO0O0O0O [2 ],O00OO00O000OOO0O0 )#line:179
    _O0OO0O0OOO0O0OO00 ('[command]'+O0OOO0OO0O0O00O0O )#line:180
def 杀死实体 (O00O000O00O0OOOOO ):#line:182
    if O00O000O00O0OOOOO [0 ]=="#AE"or O00O000O00O0OOOOO [0 ]=='#ELS':#line:183
        O0OOOOO0OOO000OOO ='kill '+O00O000O00O0OOOOO [1 ]#line:184
        _O0OO0O0OOO0O0OO00 ('[command]'+O0OOOOO0OOO000OOO )#line:185
    else :#line:186
        _OOO0O0OOOOOO0O0OO ("不是实体(集)")#line:187
def 传送实体到位置 (OOO00O0OO00OOOO0O ,OOO0OO0OO0OO00O00 ):#line:189
    if OOO00O0OO00OOOO0O [0 ]=="#AE"or OOO00O0OO00OOOO0O [0 ]=='#ELS':#line:190
        OOO0OO0000000O0OO ='<e> tp '+OOO00O0OO00OOOO0O [1 ]+" <x> <y> <z>"#line:191
        OOO0OO0000000O0OO =_OO000OOOO00OOOOOO (OOO0OO0000000O0OO ,OOO0OO0OO0OO00O00 )#line:192
        _O0OO0O0OOO0O0OO00 ('[command]'+OOO0OO0000000O0OO )#line:193
    else :#line:194
        _OOO0O0OOOOOO0O0OO ("不是实体(集)")#line:195
def 实体集交集 (O0O0000O0O0000000 ,OO00000O0O0OO000O ):#line:197
    if (O0O0000O0O0000000 [0 ]=="#AE"or O0O0000O0O0000000 [0 ]=='#ELS')and (OO00000O0O0OO000O [0 ]=="#AE"or OO00000O0O0OO000O [0 ]=='#ELS'):#line:198
        O0O00O0000O0OOO00 ,OOOOO0OOO00OOOOOO ,OOOO0O00OOO0O0O0O =O0O0000O0O0000000 [1 ].partition ('[')#line:199
        OOOO0O00OOO0O0O0O =OOOO0O00OOO0O0O0O .replace (']',"")#line:200
        O0O00O0000O0OOO00 ,OOOOO0OOO00OOOOOO ,O000000O00OO0OO00 =OO00000O0O0OO000O [1 ].partition ('[')#line:202
        O000000O00OO0OO00 =O000000O00OO0OO00 .replace (']',"")#line:203
        O0OOOO0OOO0OOOOO0 =OOOO0O00OOO0O0O0O +","+O000000O00OO0OO00 #line:205
        O0OOOO0OOO0OOOOO0 =O0OOOO0OOO0OOOOO0 .replace (",,",",")#line:206
        OOOOO00O0OO000O0O =O0OOOO0OOO0OOOOO0 .split (',')#line:207
        OO0O0OOOOO0O0OO00 ='@e['#line:208
        for OOOO0O0O0O000OO0O in OOOOO00O0OO000O0O :#line:209
            if not OOOO0O0O0O000OO0O in OO0O0OOOOO0O0OO00 :#line:210
                OO0O0OOOOO0O0OO00 +=","+OOOO0O0O0O000OO0O #line:211
        OO0O0OOOOO0O0OO00 =OO0O0OOOOO0O0OO00 .replace ('@e[,','@e[')#line:212
        OO0O0OOOOO0O0OO00 +="]"#line:213
        return (['#ELS',OO0O0OOOOO0O0OO00 ])#line:214
    else :#line:215
        _OOO0O0OOOOOO0O0OO ("不是实体(集)")#line:216
def 实体集并集 (OO00O0OO0OO0O000O ,OO00O0OO0O000OOOO ):#line:218
    if (OO00O0OO0OO0O000O [0 ]=="#AE"or OO00O0OO0OO0O000O [0 ]=='#ELS')and (OO00O0OO0O000OOOO [0 ]=="#AE"or OO00O0OO0O000OOOO [0 ]=='#ELS'):#line:219
        OO000O0O0O0000OOO ="temp"+str (random .randint (0 ,10000 ))#line:220
        _O0OO0O0OOO0O0OO00 ('[command]tag '+OO00O0OO0OO0O000O [1 ]+' add '+OO000O0O0O0000OOO )#line:222
        _O0OO0O0OOO0O0OO00 ('[command]tag '+OO00O0OO0O000OOOO [1 ]+' add '+OO000O0O0O0000OOO )#line:223
        _OO00OOOO0O0OO0OOO ('[command]tag @e remove'+OO000O0O0O0000OOO )#line:224
        return (['#ELS','@e[tag='+OO000O0O0O0000OOO +']'])#line:225
    else :#line:226
        _OOO0O0OOOOOO0O0OO ("不是实体(集)")#line:227
def 计分项_增加 (O0O0OOOOO000OOO0O ,OOOO00O0OOOOOO0OO ,O00O0O0O000000O00 ):#line:229
    if not (OOOO00O0OOOOOO0OO [0 ]=="#AE"or OOOO00O0OOOOOO0OO [0 ]=='#ELS'):#line:230
         _OOO0O0OOOOOO0O0OO ("不是实体(集)")#line:231
    _O0OO0O0OOO0O0OO00 ('[command]scoreboard players add '+OOOO00O0OOOOOO0OO [1 ]+" "+O0O0OOOOO000OOO0O +" "+str (O00O0O0O000000O00 ))#line:232
def 计分项_增加_文本玩家 (O00O0OO0O00O0OOOO ,O000000O00OO00000 ,OOO0O0O0OO0000O00 ):#line:233
    _O0OO0O0OOO0O0OO00 ('[command]scoreboard players add '+O000000O00OO00000 +" "+O00O0OO0O00O0OOOO +" "+str (OOO0O0O0OO0000O00 ))#line:234
def 计分项_设置 (OOOOO0O0OOOOOO000 ,O00OOOO0000O00OOO ,OOO000000OOOOOOO0 ):#line:235
    if not (O00OOOO0000O00OOO [0 ]=="#AE"or O00OOOO0000O00OOO [0 ]=='#ELS'):#line:236
         _OOO0O0OOOOOO0O0OO ("不是实体(集)")#line:237
    _O0OO0O0OOO0O0OO00 ('[command]scoreboard players set '+O00OOOO0000O00OOO [1 ]+" "+OOOOO0O0OOOOOO000 +" "+str (OOO000000OOOOOOO0 ))#line:238
def 计分项_设置_文本玩家 (O0O0O0OO0O0O00O0O ,O0OOO0O0O00O0OO00 ,OOO000O0OO000O0O0 ):#line:239
    _O0OO0O0OOO0O0OO00 ('[command]scoreboard players set '+O0OOO0O0O00O0OO00 +" "+O0O0O0OO0O0O00O0O +" "+str (OOO000O0OO000O0O0 ))#line:240
def 计分项_清除 (OO0O0OOO0O0O00OOO ,O00O0O00O00OO000O ):#line:241
    if not (O00O0O00O00OO000O [0 ]=="#AE"or O00O0O00O00OO000O [0 ]=='#ELS'):#line:242
         _OOO0O0OOOOOO0O0OO ("不是实体(集)")#line:243
    _O0OO0O0OOO0O0OO00 ('[command]scoreboard players reset '+O00O0O00O00OO000O [1 ]+" "+OO0O0OOO0O0O00OOO )#line:244
def 计分项_清除_文本玩家 (O0OO0O00OOO000OO0 ,O0O000O00OO00OO00 ):#line:245
    _O0OO0O0OOO0O0OO00 ('[command]scoreboard players reset '+O0O000O00OO00OO00 +" "+O0OO0O00OOO000OO0 )#line:246
def 添加计分项 (OO0OO00O0000OO000 ,O0O00OOOOOOO0OO00 ):#line:247
    _O0OO0O0OOO0O0OO00 ("[command]scoreboard objectives add "+OO0OO00O0000OO000 +" dummy "+O0O00OOOOOOO0OO00 )#line:248
def 删除计分项 (O0O00O0O0OOOOOOO0 ):#line:249
    _O0OO0O0OOO0O0OO00 ('[command]scoreboard objectives remove '+O0O00O0O0OOOOOOO0 )#line:250
def 设置计分项边栏显示 (OO0000000000OO000 ):#line:251
    _O0OO0O0OOO0O0OO00 ('[command]scoreboard objectives setdisplay sidebar '+OO0000000000OO000 )#line:252
def 设置计分项菜单界面显示 (OOO000OO0OO00OO0O ):#line:253
    _O0OO0O0OOO0O0OO00 ('[command]scoreboard objectives setdisplay list '+OOO000OO0OO00OO0O )#line:254
def 设置计分项名字下方显示 (OO0O00OO0OO00OOO0 ):#line:255
    _O0OO0O0OOO0O0OO00 ('[command]scoreboard objectives setdisplay belowname '+OO0O00OO0OO00OOO0 )#line:256
def 取实体集_实体_距离 (O00000OO0O0OOO0OO ,OOOO000OO0000O0OO ):#line:257
    if not (O00000OO0O0OOO0OO [0 ]=="#AE"or O00000OO0O0OOO0OO [0 ]=='#ELS'):#line:258
         _OOO0O0OOOOOO0O0OO ("不是实体(集)")#line:259
    OO00OO0O000000000 ="temp"+str (random .randint (0 ,10000 ))#line:260
    _O0OO0O0OOO0O0OO00 ('[command]execute '+O00000OO0O0OOO0OO [1 ]+" ~ ~ ~ tag @e[rm=0.1,r="+str (OOOO000OO0000O0OO )+"] add "+OO00OO0O000000000 )#line:261
    _OO00OOOO0O0OO0OOO ('[command]tag @e remove'+OO00OO0O000000000 )#line:262
    return (['#ELS','@e[tag='+OO00OO0O000000000 +']'])#line:263
def 构建Json (*O00O00OO00O0OOO00 ):#line:264
    O0000000O00O00O00 ='##'#line:265
    for OOOO000O000OO00OO in O00O00OO00O0OOO00 :#line:266
        if not OOOO000O000OO00OO [0 ]=='#JW':#line:267
             _OOO0O0OOOOOO0O0OO ("不是Json")#line:268
        O0000000O00O00O00 +=','+OOOO000O000OO00OO [1 ]#line:270
    O0000000O00O00O00 +=']}'#line:271
    O0000000O00O00O00 =O0000000O00O00O00 .replace ('##,','{"rawtext": [')#line:272
    return (O0000000O00O00O00 )#line:273
def 聊天栏_输出JSON (O0OO0O0O0OOO0O0O0 ,O0000OO0OO0O0O00O ):#line:275
    if not (O0OO0O0O0OOO0O0O0 [0 ]=="#AE"or O0OO0O0O0OOO0O0O0 [0 ]=='#ELS'):#line:276
         _OOO0O0OOOOOO0O0OO ("不是实体(集)")#line:277
    _O0OO0O0OOO0O0OO00 ('[command]tellraw '+O0OO0O0O0OOO0O0O0 [1 ]+" "+O0000OO0OO0O0O00O )#line:279
def 标题_输出JSON (OOO0OO000OO0OO0O0 ,O00OO00OOO0000000 ,OO00OOOOO00O0O0O0 =""):#line:281
    if not (OOO0OO000OO0OO0O0 [0 ]=="#AE"or OOO0OO000OO0OO0O0 [0 ]=='#ELS'):#line:282
        print (OOO0OO000OO0OO0O0 )#line:283
        _OOO0O0OOOOOO0O0OO ("不是实体(集)")#line:284
    if (OO00OOOOO00O0O0O0 ):#line:285
        _O0OO0O0OOO0O0OO00 ('[command]titleraw '+OOO0OO000OO0OO0O0 [1 ]+" subtitle "+OO00OOOOO00O0O0O0 )#line:286
    _O0OO0O0OOO0O0OO00 ('[command]titleraw '+OOO0OO000OO0OO0O0 [1 ]+" title "+O00OO00OOO0000000 )#line:287
def 标题底栏_输出JSON (OOOO000OO0O0OO000 ,O0OOO00OO00OOOOOO ):#line:289
    if not (OOOO000OO0O0OO000 [0 ]=="#AE"or OOOO000OO0O0OO000 [0 ]=='#ELS'):#line:290
         _OOO0O0OOOOOO0O0OO ("不是实体(集)")#line:291
    _O0OO0O0OOO0O0OO00 ('[command]titleraw '+OOOO000OO0O0OO000 [1 ]+" actionbar "+O0OOO00OO00OOOOOO )#line:292
def Json文本 (O0OOO0OOOO00O0OOO ):#line:295
    return ['#JW','{"text":"'+O0OOO0OOOO00O0OOO +'"}']#line:296
def Json计分板分数__文本玩家 (O00OOO0OOOO00OO0O ,O0O00OOOOOO0OOO00 ):#line:297
    return ['#JW','{"score":{"name":"'+O0O00OOOOOO0OOO00 +'","objective":"'+O00OOO0OOOO00OO0O +'"}}']#line:298
def Json计分板分数 (O0O0O00000O00O00O ,O0OOOOO00OO0OOO0O ):#line:299
    if not (O0OOOOO00OO0OOO0O [0 ]=="#AE"or O0OOOOO00OO0OOO0O [0 ]=='#ELS'):#line:300
         _OOO0O0OOOOOO0O0OO ("不是实体(集)")#line:301
    return ['#JW','{"score":{"name":"'+O0OOOOO00OO0OOO0O [1 ]+'","objective":"'+O0O0O00000O00O00O +'"}}']#line:302
def _O0O00O0O0OOO0O000 (OO000OO0O0OO00000 ,OO00O00OOO0OO0O0O ):#line:305
    if not OO00O00OOO0OO0O0O [0 ]=="#BOX":#line:307
        _OOO0O0OOOOOO0O0OO ("不是矩形空间")#line:308
    O000O0O0OO00O0000 =OO000OO0O0OO00000 #line:309
    if OO00O00OOO0OO0O0O [1 ]=="":#line:310
        OO000OO0O0OO00000 =OO000OO0O0OO00000 .replace ('<e>',"")#line:311
    else :#line:312
        OO000OO0O0OO00000 =OO000OO0O0OO00000 .replace ('<e>','execute '+OO00O00OOO0OO0O0O [1 ]+" ~ ~ ~ ")#line:313
        OO000OO0O0OO00000 =OO000OO0O0OO00000 .replace ('<',"~<")#line:314
    OO000OO0O0OO00000 =OO000OO0O0OO00000 .replace ('<x1>',str (OO00O00OOO0OO0O0O [2 ]))#line:315
    OO000OO0O0OO00000 =OO000OO0O0OO00000 .replace ('<y1>',str (OO00O00OOO0OO0O0O [3 ]))#line:316
    OO000OO0O0OO00000 =OO000OO0O0OO00000 .replace ('<z1>',str (OO00O00OOO0OO0O0O [4 ]))#line:317
    OO000OO0O0OO00000 =OO000OO0O0OO00000 .replace ('<x2>',str (OO00O00OOO0OO0O0O [5 ]))#line:318
    OO000OO0O0OO00000 =OO000OO0O0OO00000 .replace ('<y2>',str (OO00O00OOO0OO0O0O [6 ]))#line:319
    OO000OO0O0OO00000 =OO000OO0O0OO00000 .replace ('<z2>',str (OO00O00OOO0OO0O0O [7 ]))#line:320
    return OO000OO0O0OO00000 #line:321
def _OO000OOOO00OOOOOO (OO000OO0O0OOOO00O ,O0O00OO0O000O0O00 ):#line:322
    if not O0O00OO0O000O0O00 [0 ]=="#LOX":#line:324
        _OOO0O0OOOOOO0O0OO ("不是位置")#line:325
    OOOO0OOO0O0O0OOO0 =OO000OO0O0OOOO00O #line:326
    if O0O00OO0O000O0O00 [1 ]=="":#line:327
        OO000OO0O0OOOO00O =OO000OO0O0OOOO00O .replace ('<e>',"")#line:328
    else :#line:329
        OO000OO0O0OOOO00O =OO000OO0O0OOOO00O .replace ('<e>','execute '+O0O00OO0O000O0O00 [1 ]+" ~ ~ ~ ")#line:330
        OO000OO0O0OOOO00O =OO000OO0O0OOOO00O .replace ('<',"~<")#line:331
    OO000OO0O0OOOO00O =OO000OO0O0OOOO00O .replace ('<x>',str (O0O00OO0O000O0O00 [2 ]))#line:332
    OO000OO0O0OOOO00O =OO000OO0O0OOOO00O .replace ('<y>',str (O0O00OO0O000O0O00 [3 ]))#line:333
    OO000OO0O0OOOO00O =OO000OO0O0OOOO00O .replace ('<z>',str (O0O00OO0O000O0O00 [4 ]))#line:334
    return OO000OO0O0OOOO00O #line:335
import base64 #line:393
def Run (OO00OOOOOOO00O0OO ):#line:394
    global cout #line:395
    global ender #line:396
    global err #line:397
    cout =""#line:398
    ender =""#line:399
    err =""#line:400
    OO0000OOO0000OO0O =['def','os','+','\\','/','import','&','@','[]',"*",":","."]#line:402
    for O00O0O00000O0OO00 in OO0000OOO0000OO0O :#line:403
        OO00OOOOOOO00O0OO =OO00OOOOOOO00O0OO .replace (O00O0O00000O0OO00 ,"")#line:404
    print (OO00OOOOOOO00O0OO )#line:405
    try :#line:407
        exec (OO00OOOOOOO00O0OO )#line:408
    except :#line:409
        O00OOOOOOOO0O000O ="语法错误 : "+err #line:410
    else :#line:411
        O00OOOOOOOO0O000O =cout +ender #line:412
        O00OOOOOOOO0O000O =O00OOOOOOOO0O000O .replace ('  '," ")#line:413
        O00OOOOOOOO0O000O =O00OOOOOOOO0O000O .replace (' [command]','[command]')#line:414
        O00OOOOOOOO0O000O =O00OOOOOOOO0O000O .replace ('[command] ','[command]')#line:415
        O00OOOOOOOO0O000O =O00OOOOOOOO0O000O .replace ('[command]','\n<br>')#line:416
    return O00OOOOOOOO0O000O #line:417
bb =aa =""#line:420
while True :#line:421
    aa =input ()#line:422
    bb += aa + "\n"#line:423
    if aa =="":#line:424
        cc =Run (bb )#line:425
        bb =""#line:426
        aa =""#line:427
        print (cc )#line:428
