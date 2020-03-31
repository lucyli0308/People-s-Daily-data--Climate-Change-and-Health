# -*- coding: utf-8 -*-
import os
import shutil
import matplotlib.pyplot as plt

#txt目录[需设置]
gstrTxtDir = 'C:/code/new_code/rename/'

#保存目录[需设置]
gstrSaveDir = 'C:/code/new_code/save/'

#年份(仅做结果文件命名，未做单独年份提取)[需设置]
year='2008-2019-rename'

#阈值设置[需设置]
#(1)TotalScore阈值
gnMinTotalScoreThr=10
#(2)Rate阈值
gfMinRateThr=0.01
#(3)HealthScore阈值
gnMinHealthScore=2
#(4)ClimateScore阈值
gnMinClimateScore=2

#开关
#(1)score和rate过滤结果另存为开关(0:不使用,1:使用)[需设置]
gbSaveResultFileSwitch=1
#(2)遗漏正确文章另存为开关(0:不使用,1:使用)[需设置]
gbSaveMissTrueFileSwitch=1
#(3)只使用score过滤结果另存为开关(0:不使用,1:使用)[需设置,要求功能]
gbSaveOnlyScoreSwitch=1
#(4)只搜索气候另存为开关(0:不使用,1:使用):注意有单独的仅搜索气候的关键词[需设置,要求功能]
gbSaveOnlySearchClimateSwitch=1

#搜索结果保存目录
#(1)搜索气候+健康结果
gstrSaveClimateHealthDir = os.path.join(gstrSaveDir,'save-climate-health-'+year)
if os.path.exists(gstrSaveClimateHealthDir):#若存在，则删除
    print('Clear:%s'%gstrSaveClimateHealthDir)
    shutil.rmtree(gstrSaveClimateHealthDir)
if not os.path.exists(gstrSaveClimateHealthDir):#若不存在，则新建
    print('Make:%s'%gstrSaveClimateHealthDir)
    os.makedirs(gstrSaveClimateHealthDir)
#(2)遗漏正确
gstrSaveMissTrueDir= os.path.join(gstrSaveDir,'save-miss-true-'+year)
if os.path.exists(gstrSaveMissTrueDir):#若存在，则删除
    print('Clear:%s'%gstrSaveMissTrueDir)
    shutil.rmtree(gstrSaveMissTrueDir)
if not os.path.exists(gstrSaveMissTrueDir):#若不存在，则新建
    print('Make:%s'%gstrSaveMissTrueDir)
    os.makedirs(gstrSaveMissTrueDir)
#(3)只score过滤结果
gstrSaveOnlyScoreDir = os.path.join(gstrSaveDir,'save-only-score-'+year)
if os.path.exists(gstrSaveOnlyScoreDir):#若存在，则删除
    print('Clear:%s'%gstrSaveOnlyScoreDir)
    shutil.rmtree(gstrSaveOnlyScoreDir)
if not os.path.exists(gstrSaveOnlyScoreDir):#若不存在，则新建
    print('Make:%s'%gstrSaveOnlyScoreDir)
    os.makedirs(gstrSaveOnlyScoreDir)
#(4)只搜索气候结果
gstrSaveOnlyClimateDir = os.path.join(gstrSaveDir,'save-only-climate-'+year)
if os.path.exists(gstrSaveOnlyClimateDir):#若存在，则删除
    print('Clear:%s'%gstrSaveOnlyClimateDir)
    shutil.rmtree(gstrSaveOnlyClimateDir)
if not os.path.exists(gstrSaveOnlyClimateDir):#若不存在，则新建
    print('Make:%s'%gstrSaveOnlyClimateDir)
    os.makedirs(gstrSaveOnlyClimateDir)

#图片保存目录
gstrSavePicPath=gstrSaveDir+'/result.png'

#文件后缀
gstrFileSuffix = '.txt'

#日志
#(1)结果日志
gstrLogPath=os.path.join(gstrSaveDir,'log-'+year+'.txt')
if os.path.exists(gstrLogPath):
    os.remove(gstrLogPath)
#(2)正确样本日志
gstrLogTruePath=os.path.join(gstrSaveDir,'log-true-'+year+'.txt')
if os.path.exists(gstrLogTruePath):
    os.remove(gstrLogTruePath)
#(3)结果转csv
gstrCsvPath=os.path.join(gstrSaveDir,'result-'+year+'.csv')
if os.path.exists(gstrCsvPath):
    os.remove(gstrCsvPath)

#CSV标题
strCsvTitle=','.join(
        ['ID',
        'FileName',
        'TotalScore',
        'Rate',
        'CharTotalNum',
        'HealthScore',
        'HealthKeywords',
        'ClimateScore',
        'ClimateKeywords'+'\n'])
with open(gstrCsvPath, 'a+',encoding='utf-8') as f:
    f.write(strCsvTitle)

#健康关键词
#(1)旧的关键词
# '疟疾', '腹泻', '感染', '疾病', '肺炎', '流行病',
# '公共卫生', '流行病学', '卫生保健', '卫生', '死亡率', '发病率', '营养', '疾病',
# '非传染性疾病', '传染性疾病', '传染病', '空气污染',
# '精神障碍', '发育迟缓',
# '传染', '疾患', '症', '病', '瘟疫', '流感', '流行感冒', '治疗', '保健', '健康', '死亡'
#(2)删除关键词
#'病',
#'死鱼',
#'动物疫病','病虫害','病害','病根','病因','药到病除','病倒'
#(3)新增关键词
#特征词：'精神疾病','精神病','登革热','饥饿','粮食','有害','皮肤病','风湿病','呼吸系统疾病','人类健康',
#       '心脏病','糖尿病','人体健康','身体健康','热死','口罩','防护','生存'
#干扰词：'健康发展','生态健康','河流健康','生态环境健康','口蹄疫','黑烂病','珊瑚死亡','沙虫死亡'
gDictHealthKeyWords={
                '疟疾':1, 
                '腹泻':1, 
                '感染':1, 
                '肺炎':1, 
                '流行病':1,
                '公共卫生':1, 
                '卫生':1, 
                '发病':1, 
                '营养':1,
                '精神障碍':1, 
                '发育':1,
                '传染':1, 
                '疾患':1, 
                '症':1,  
                '瘟疫':1, 
                '流感':1, 
                '流行感冒':1, 
                '治疗':1, 
                '保健':1, 
                '健康':1, 
                '死亡':2,
                '精神疾病':1,
                '精神病':1,
                '登革热':1,
                '饥饿':1,
                '粮食':1,
                '有害':1,
                '皮肤病':1,
                '风湿':1,
                '呼吸系统疾病':1,
                '人类健康':1,
                '人体健康':1,
                '身体健康':1,
                '心脏病':1,
                '糖尿病':1,
                '疾病':1,
                '热死':1,
                '口罩':1,
                '防护':1,
                '生存':1,
                '健康发展':-1,
                '生态健康':-1,
                '河流健康':-1,
                '生态环境健康':-1,
                '口蹄疫':-1,
                '黑烂病':-1,
                '珊瑚死亡':-1,
                '沙虫死亡':-1
                }

#气候一级关键词
#(1)旧的关键词
# '气候变化', '全球变暖', '温室', '极端天气', '全球环境变化',
# '低碳',  '可再生能源', '碳排放', '二氧化碳排放', '气候污染',
# '气候', '全球升温', '再生能源', 'CO2排放'
#(2)删除关键词
#'可再生能源','天气',
#(3)新增关键词
#特征词：'极端气候','高温','变暖','排放','环境变化','升温','全球温升','热浪','暴雨','气温','洪水','洪灾',
#       '气候反常','野火','山火','雪灾','低温','年代际','冰雪','可持续发展','海洋酸化','静稳','温室气体'
#干扰词：'高温加热','低碳水'
gDictClimateKeyWords_FirstLevel={
                        '气候变化':1, 
                        '全球变暖':1, 
                        '温室':1, 
                        '极端天气':1, 
                        '全球环境变化':1,
                        '低碳':1, 
                        '碳排放':1, 
                        '二氧化碳排放':1, 
                        '气候污染':1,
                        '气候':1, 
                        '全球升温':1, 
                        '再生能源':1, 
                        'CO2排放':1,
                        '极端气候':1,
                        '高温':1,
                        '变暖':1,
                        '排放':1,
                        '环境变化':1,
                        '升温':1,
                        '全球温升':1,
                        '热浪':1,
                        '暴雨':1,
                        '气温':1,
                        '洪水':1,
                        '洪灾':1,
                        '气候反常':1,
                        '野火':1,
                        '山火':1,
                        '雪灾':1,
                        '低温':1,
                        '年代际':1,
                        '冰雪':1,
                        '可持续发展':1,
                        '海洋酸化':1,
                        '静稳':1,
                        '温室气体':1,
                        '高温加热':-1,
                        '低碳水':-1
                        }

#气候二级关键词（仅当存在一级关键词才会搜索二级关键词）
#(1)删除关键词
#'雾',
#(2)新增关键词
#'霾','空气污染','大气污染'
gDictClimateKeyWords_SecondLevel={
                        '霾':1,
                        '空气污染':1,
                        '大气污染':1
                        }

#仅搜索气候关键词
gArrStrClimateKeyWords=[
                        '气候变化', '全球变暖', '温室', '极端天气', '全球环境变化', 
                        '低碳',  '可再生能源', '碳排放', '二氧化碳排放', '气候污染', 
                        '气候', '全球升温', '再生能源', 'CO2排放'
                        ]                     

#结果得分列表
gListTotalScore=[]

#高于阈值得分列表
gListMoreTotalScore=[]
#低于阈值得分列表
gListLessTotalScore=[]
#高于阈值比重列表
gListMoreRate=[]
#低于阈值比重列表
gListLessRate=[]

#统计
#结果数
gnResultNum=0
#结果中的正确数
gnTrueResultNum=0
#正样本数
gnTrueFileNum=0

###############################################################################
'''
函数名称:SearchKeyWords
函数功能:搜索关键词
函数参数:
    ID[IN]:序号
    strTxtName[IN]:文件名称
    strFilePath[IN]:文件绝对路径
函数返回值:空
'''
###############################################################################
def SearchKeyWords(ID,strTxtName,strFilePath):
 	#打开文件，读取内容
    fr = open(strFilePath, 'r', encoding='utf-8')

    #文章内容
    strContent=''.join(fr.readlines())

    #健康关键词
    listStrHealthKeyWords=[]
    listNumHealthKeyWords=[]
    strHealthLog=''
    nHealthScore=0
    for key in gDictHealthKeyWords.keys():
        nScore=gDictHealthKeyWords[key]
        nWordsNum=strContent.count(key)
        if nWordsNum > 0:
            listStrHealthKeyWords.append(key)
            listNumHealthKeyWords.append(nWordsNum)
            strHealthLog = strHealthLog + ' ' + key + ':' + str(nWordsNum) + '*' + str(nScore)
            nHealthScore = nHealthScore + nWordsNum*nScore
        #end of if
    #end of for

    #气候一级关键词
    listStrClimateKeyWords=[]
    listNumClimateKeyWords=[]
    strClimateLog=''
    nClimateScore=0
    for key in gDictClimateKeyWords_FirstLevel.keys():
        nScore=gDictClimateKeyWords_FirstLevel[key]
        nWordsNum=strContent.count(key)
        if nWordsNum > 0:
            listStrClimateKeyWords.append(key)
            listNumClimateKeyWords.append(nWordsNum)
            strClimateLog = strClimateLog + ' ' + key + ':' + str(nWordsNum) + '*' + str(nScore)
            nClimateScore = nClimateScore + nWordsNum*nScore
        #end of if
    #end of for

    #气候二级关键词(需要有一级关键词才会进行二级搜索)
    if nClimateScore > 0:
        for key in gDictClimateKeyWords_SecondLevel.keys():
            nScore=gDictClimateKeyWords_SecondLevel[key]
            nWordsNum=strContent.count(key)
            if nWordsNum > 0:
                listStrClimateKeyWords.append(key)
                listNumClimateKeyWords.append(nWordsNum)
                strClimateLog = strClimateLog + ' ' + key + ':' + str(nWordsNum) + '*' + str(nScore)
                nClimateScore = nClimateScore + nWordsNum*nScore
            #end of if
        #end of for
    #end of if

    #气候+健康文章：计算得分
    #总分
    nTotalScore=nHealthScore+nClimateScore
    #字符总数
    nTotalWordNum=len(strContent)
    #关键词的全文占比
    fRate=0.0
    if nTotalWordNum > 0:
        fRate=float(nTotalScore)/float(nTotalWordNum)
    #日志
    strLog=str(ID)+':'+strTxtName + '\n' + \
                    'TotalScore=' + str(nTotalScore) + ' ' +'Rate=' + str(round(fRate,4)) +' 字符总数=' + str(nTotalWordNum) + ''+'\n' +\
                    'HealthScore=' + str(nHealthScore) + strHealthLog +  '\n' +\
                    'ClimateScore=' + str(nClimateScore) + strClimateLog +  '\n\n'
    #csv信息
    strCsvText=','.join([str(ID),
        strTxtName,
        str(nTotalScore),
        str(round(fRate,4)),
        str(nTotalWordNum),
        str(nHealthScore),
        strHealthLog,
        str(nClimateScore),
        strClimateLog+'\n'])
    #阈值过滤输出
    if (nHealthScore >= gnMinHealthScore
        and nClimateScore >= gnMinClimateScore):
        if nTotalScore >= gnMinTotalScoreThr and fRate >= gfMinRateThr:
            #总分
            gListTotalScore.append(nTotalScore)
            #高于阈值总分
            gListMoreTotalScore.append(nTotalScore)
            #高于阈值比重
            gListMoreRate.append(fRate)
            #结果数
            global gnResultNum
            gnResultNum = gnResultNum+1
            #结果中的正确数
            nTrueWordNum=strTxtName.count('[正确]')
            if nTrueWordNum > 0:
                global gnTrueResultNum
                gnTrueResultNum = gnTrueResultNum+1
            #日志
            print(strLog)
            with open(gstrLogPath, 'a+',encoding='utf-8') as f:
                f.write(strLog)
            #csv
            with open(gstrCsvPath, 'a+',encoding='utf-8') as f:
                f.write(strCsvText)
            #另存为
            if (gbSaveResultFileSwitch):
                shutil.copy(strFilePath, os.path.join(gstrSaveClimateHealthDir,strTxtName))
        else:
            #低于阈值总分
            gListLessTotalScore.append(nTotalScore)
            #低于阈值比重
            gListLessRate.append(fRate)
        #end of if else
    #end of if

    #正确样本日志
    nTrueWordNum=strTxtName.count('[正确]')
    if nTrueWordNum > 0:
        #计数
        global gnTrueFileNum
        gnTrueFileNum = gnTrueFileNum+1
        #日志
        with open(gstrLogTruePath, 'a+',encoding='utf-8') as f:
            f.write(strLog)
        #漏判
        if (nHealthScore < gnMinHealthScore
            or nClimateScore < gnMinClimateScore
            or nTotalScore < gnMinTotalScoreThr 
            or fRate < gfMinRateThr):
            #另存为
            if gbSaveMissTrueFileSwitch:
                shutil.copy(strFilePath, os.path.join(gstrSaveMissTrueDir,strTxtName))
            #csv信息
            strCsvText=','.join(['漏判'+str(ID),
                strTxtName,
                str(nTotalScore),
                str(round(fRate,4)),
                str(nTotalWordNum),
                str(nHealthScore),
                strHealthLog,
                str(nClimateScore),
                strClimateLog+'\n'])
            print(strCsvText)
            with open(gstrCsvPath, 'a+') as f:
                f.write(strCsvText)
        #end of if
    #end of if

    #只Score过滤另存为
    if (nClimateScore >= gnMinClimateScore):
        if nTotalScore >= gnMinTotalScoreThr and fRate >= gfMinRateThr:
            #另存为
            if (gbSaveOnlyScoreSwitch):
                shutil.copy(strFilePath, os.path.join(gstrSaveOnlyScoreDir,strTxtName))
        #end of if else
    #end of if

    #只搜索气候另存为
    if gbSaveOnlySearchClimateSwitch:
        nOnlyClimateScore=0
        for strClimateKeyWords in gArrStrClimateKeyWords:
            nWordsNum=strContent.count(strClimateKeyWords)
            if nWordsNum > 0:
                nOnlyClimateScore = nOnlyClimateScore + nWordsNum
            #end of if
        #end of for

        #气候文章
        if (nOnlyClimateScore > 0):
            shutil.copy(strFilePath, os.path.join(gstrSaveOnlyClimateDir,strTxtName))
    #end of if

    #关闭文件
    fr.close()
#end of def SearchKeyWords

###############################################################################
'''
函数名称:StatisticalDistributionLog
函数功能:统计分布日志
函数参数:空
函数返回值:空
'''
###############################################################################
def StatisticalDistributionLog():
    #统计分布
    arrHistCount=[0,0,0,0,0,
                  0,0,0,0,0,
                  0,0,0,0,0,
                  0,0,0,0,0]
    for ID,nTotalScore in enumerate(gListTotalScore):
        nHistID=int((nTotalScore-1)/5)
        if nHistID>19:
            nHistID=19
        arrHistCount[nHistID] = arrHistCount[nHistID] + 1
    #end of for
    print(arrHistCount)

    #打印分布
    nTotal=0
    for ID,nHistCount in enumerate(arrHistCount):
        nTotal = nTotal+nHistCount
        nMinHist=ID*5
        if ID > 0:
            nMinHist=ID*5+1
        nMaxHist=(ID+1)*5
        with open(gstrLogPath, 'a+',encoding='utf-8') as f:
            strLog=str(nMinHist) + '--' + str(nMaxHist) + ':' + str(nHistCount) + '\n'
            f.write(strLog)
    #end of for

    #打印总数
    with open(gstrLogPath, 'a+',encoding='utf-8') as f:
        f.write('Total='+str(nTotal))
#end of def StatisticalDistribution

###############################################################################
'''
函数名称:StatisticalResult
函数功能:统计结果
函数参数:空
函数返回值:空
'''
###############################################################################
def StatisticalResult():
    #关键词
    #(1)健康关键词
    strCsvText=','.join(['\nHealthKeyWords',str(gDictHealthKeyWords)])
    print(strCsvText)
    with open(gstrCsvPath, 'a+',encoding='utf-8') as f:
        f.write(strCsvText)
    #(2)气候一级关键词
    strCsvText=','.join(['\nClimateKeyWords-1',str(gDictClimateKeyWords_FirstLevel)])
    print(strCsvText)
    with open(gstrCsvPath, 'a+',encoding='utf-8') as f:
        f.write(strCsvText)
    #(3)气候二级关键词
    strCsvText=','.join(['\nClimateKeyWords-2',str(gDictClimateKeyWords_SecondLevel)])
    print(strCsvText)
    with open(gstrCsvPath, 'a+',encoding='utf-8') as f:
        f.write(strCsvText)

    #阈值
    #(1)TotalScore阈值
    strCsvText=','.join(['\n\nMinTotalScoreThr',str(gnMinTotalScoreThr)])
    print(strCsvText)
    with open(gstrCsvPath, 'a+',encoding='utf-8') as f:
        f.write(strCsvText)
    #(2)Rate阈值
    strCsvText=','.join(['\nMinRateThr',str(round(gfMinRateThr,4))])
    print(strCsvText)
    with open(gstrCsvPath, 'a+',encoding='utf-8') as f:
        f.write(strCsvText)
    #(3)HealthScore阈值
    strCsvText=','.join(['\nMinHealthScore',str(gnMinHealthScore)])
    print(strCsvText)
    with open(gstrCsvPath, 'a+',encoding='utf-8') as f:
        f.write(strCsvText)
    #(4)ClimateScore阈值
    strCsvText=','.join(['\nMinClimateScore',str(gnMinClimateScore)])
    print(strCsvText)
    with open(gstrCsvPath, 'a+',encoding='utf-8') as f:
        f.write(strCsvText)

    #统计结果
    strCsvText=','.join(['\n\n结果',str(gnResultNum)])
    print(strCsvText)
    with open(gstrCsvPath, 'a+',encoding='utf-8') as f:
        f.write(strCsvText)
    strCsvText=','.join(['\n正样本数',str(gnTrueFileNum)])
    print(strCsvText)
    with open(gstrCsvPath, 'a+',encoding='utf-8') as f:
        f.write(strCsvText)
    nMissTrueNum=gnTrueFileNum-gnTrueResultNum
    strCsvText=','.join(['\n漏判',str(nMissTrueNum)])
    print(strCsvText)
    with open(gstrCsvPath, 'a+',encoding='utf-8') as f:
        f.write(strCsvText)
    nErrorResultNum=gnResultNum-gnTrueResultNum
    strCsvText=','.join(['\n误判',str(nErrorResultNum)])
    print(strCsvText)
    with open(gstrCsvPath, 'a+',encoding='utf-8') as f:
        f.write(strCsvText)
    strCsvText=','.join(['\n正确',str(gnTrueResultNum)])
    print(strCsvText)
    with open(gstrCsvPath, 'a+',encoding='utf-8') as f:
        f.write(strCsvText)
    fP=round(float(gnResultNum)/float(gnResultNum+nMissTrueNum),4)
    strCsvText=','.join(['\n查全率P',str(fP)])
    print(strCsvText)
    with open(gstrCsvPath, 'a+',encoding='utf-8') as f:
        f.write(strCsvText)
    fR=round(float(gnTrueResultNum)/float(gnResultNum),4)
    strCsvText=','.join(['\n查准率R',str(fR)])
    print(strCsvText)
    with open(gstrCsvPath, 'a+',encoding='utf-8') as f:
        f.write(strCsvText)
    fF1=round(2*fP*fR/(fP+fR),4)
    strCsvText=','.join(['\nF1',str(fF1)])
    print(strCsvText)
    with open(gstrCsvPath, 'a+',encoding='utf-8') as f:
        f.write(strCsvText)
#end of def StatisticalResult()

###############################################################################
'''
函数名称:DrawGraph
函数功能:画图
函数参数:空
函数返回值:空
'''
###############################################################################
def DrawGraph():
    #标题
    plt.title('Score-Rate')
    #X轴名称
    plt.xlabel('Score')
    #Y轴名称
    plt.ylabel('Rate')

    #高于阈值数据
    #X轴数据
    xValue1 = gListMoreTotalScore
    #Y轴数据
    yValue1 = gListMoreRate
    # plt.scatter(x, y, s, c, marker)
    # x: x轴坐标
    # y：y轴坐标
    # s：点的大小/粗细 标量或array_like 默认是 rcParams['lines.markersize'] ** 2
    # c: 点的颜色 
    # marker: 标记的样式 默认是 'o'
    plt.scatter(xValue1, yValue1, s=20, c='red', marker='o')

    #低于阈值数据
    #X轴数据
    xValue2 = gListLessTotalScore
    #Y轴数据
    yValue2 = gListLessRate
    # plt.scatter(x, y, s, c, marker)
    # x: x轴坐标
    # y：y轴坐标
    # s：点的大小/粗细 标量或array_like 默认是 rcParams['lines.markersize'] ** 2
    # c: 点的颜色 
    # marker: 标记的样式 默认是 'o'
    plt.scatter(xValue2, yValue2, s=20, c='blue', marker='o')

    #竖分割线
    x=[gnMinTotalScoreThr,gnMinTotalScoreThr]
    y=[0,max(max(gListMoreRate),max(gListLessRate))]
    plt.plot(x,y,linewidth = '1.0',color='black')
    #横分割线
    x=[0,max(max(gListMoreTotalScore),max(gListLessTotalScore))]
    y=[gfMinRateThr,gfMinRateThr]
    plt.plot(x,y,linewidth = '1.0',color='black')

    #图例
    plt.legend()

    #保存
    plt.savefig(gstrSavePicPath)

    #显示
    plt.show()
#end of def DrawGraph()

###############################################################################
def main():
	#文件列表
    files=os.listdir(gstrTxtDir)
    #files.sort()#排序
    arrTxtFiles = [f for f in files if f.endswith(gstrFileSuffix)]#若不对后缀限制，则去除.endswith(gstrFileSuffix)
    #文件总数
    nFileNum = len(arrTxtFiles)
    #检测
    if (nFileNum == 0):
        print ('提示：没有%s的文件!!!' % gstrFileSuffix)
        return 1

    #(1)遍历pic文件夹进行搜索
    for ID,strTxtName in enumerate(arrTxtFiles):
        #打印
        print ("ID=%d,%s\n" % (ID, strTxtName))

        #txt绝对路径
        strFilePath=os.path.join(gstrTxtDir,strTxtName)
        print(strFilePath)

        #搜索内容
        SearchKeyWords(ID,strTxtName,strFilePath)
    #end of for

    #(2)统计分布日志
    StatisticalDistributionLog()

    #(3)统计结果
    StatisticalResult()

    #(4)画图
    DrawGraph()
#end fo def main()

###############################################################################
if __name__ == "__main__":
    main()
