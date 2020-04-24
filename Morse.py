#coding = utf-8
#所有数据来源于：https://morsecode.51240.com/

words = {
 'A':   '.-'         ,'B':   '-...'       ,'C': '-.-.'         ,'D':    '-..'        ,     
 'E':   '.'          ,'F':   '..-.'       ,'G': '--.'          ,'H':    '....'       ,    #特殊: AR:停止（消息结束）
 'I':   '..'         ,'J':   '.---'       ,'K': '-.-'          ,'L':    '.-..'       ,    #      AS:等待
 'M':   '--'         ,'N':   '-.'         ,'O': '---'          ,'P':    '.--.'       ,    #      K：邀请发射信号（一般跟随AR，表示“该你了”）
 'Q':   '--.-'       ,'R':   '.-.'        ,'S': '...'          ,'T':    '-'          ,    #      SK:终止（联络结束）
 'U':   '..-'        ,'V':   '...-'       ,'W': '.--'          ,'X':    '-..-'       ,    #      BT:分隔符
 'Y':   '-.--'       ,'Z':   '--..'       , 
 
 '0':   '-----'      ,'1':   '.----'      ,'2': '..---'        ,'3':    '...--'      ,    
 '4':   '....-'      ,'5':   '.....'      ,'6': '-....'        ,'7':    '--...'      ,
 '8':   '---..'      ,'9':   '----.'      , 

 '.':   '.-.-.-'     ,':':   '---...'     ,',': '--..--'       ,';':    '-.-.-.'     ,    
 '?':   '..--..'     ,'=':   '-...-'      ,"'": '.----.'       ,'/':    '-..-.'      ,
 '!':   '-.-.--'     ,'-':   '-....-'     ,'_': '..--.-'       ,'"':    '.-..-.'     ,
 '(':   '-.--.'      ,')':   '-.- -.-'    ,'$': '...-..-'      ,'&':    '....'       ,
 '@':   '.--.-.'     ,
 }

specialwords = {                                                                              #因为这个字典的value有重叠 为防止解密时出错 故分开
 'à':   '.--.-'      ,'å':   '.--.-'      ,'æ': '.-.-'         ,'ä':    '.-.-'       ,
 'ch':  '----'       ,'ç':   '-.-..'      ,'ĉ': '-.-..'        ,'ð':    '..--.'      ,
 'é':   '..-..'      ,'è':   '.-..-'      ,'ĝ': '--.-.'        ,'ĥ':    '-.--.'      ,
 'ĵ':   '.---.'      ,'ñ':   '--.--'      ,'ö': '---.'         ,'ø':    '---.'       ,
 'ŝ':   '...-.'      ,'þ':   '.--..'      ,'ü': '..--'         ,'ŭ':    '..--'       ,
 }

def change_to_morse(inpwords):    #加密
    setwords = [] 
    inpwords = inpwords.upper()    #为了转换 输入字母全部大写

    for inpword in inpwords:
        if words[inpword] != "":
            setwords.append(words[inpword])
        elif specialwords[inpword] != "":
            setwords.append(specialwords[inpword])
        else:
            setwords.append(inpword)
    
    return setwords

def change_to_words(inpmorses):
    setmorses = []

    #将words字典的key,value调换
    newwords = {}                     
    for key in words:
        newwords[words[key]] = key
    
    #调换specialwords字典 并将一部分在调换时重新更改value的键值对合并
    #如{'à':'.--.-' ,'å':'.--.-'} 调换后会变成{'.--.-':'å'} 而我们要将他变成{'.--.-':'à/å'}
    newspwords = {}
    for spkey in specialwords:
        newspwords[specialwords[spkey]] = spkey
    repeatedkeys , repeatedwords = ['.--.-','.-.-','-.-..','---.','..--'] , ['à/å','ä/æ','ç/ĉ','ö/ø','ü/ŭ']
    for repkey in repeatedkeys:
        newspwords[repkey] = repeatedwords[repeatedkeys.index(repkey)]

    for morsecode in inpmorses.split():
        setmorses.append(newwords[morsecode])
    
    return setmorses

def print_results(decode = False): #False为加密 True为解密
    if decode is True:
        inpmorses = input("请输入你想要解密的摩尔斯密码：")
        setmorses = change_to_words(inpmorses)
        print("转换后的明文是：")
        for setmorse in setmorses:
            print(setmorse,end="")
    else:
        inpwords = input("请输入你想要加密的明文：")
        setwords = change_to_morse(inpwords)
        print("转换后的密文：")
        for setword in setwords:
            print(setword,end = " ")
    print("\n")

if __name__ == "__main__":
    while True: 
        print_results(decode = False)
