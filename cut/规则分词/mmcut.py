class MMCut():
    def __init__(self,window_size=1):
        self.window_size=window_size

    def cut(self,text,dic):
        result=[]
        delimiter='--'
        index=0
        text_length=len(text)
        while text_length > index:
            for size in range(self.window_size+index,index,-1):#从最大减小到index+1指示位置
                piece=text[index:size]#没找到就会按这个提取最前1个字切开
                if piece in dic:
                    #找到，分词在字典里，index向后移动到该分词所在末尾位置
                    index=size-1
                    break
            index+=1#①找到，从上次找到次末尾的下一个开始;②未找到，切开这个字，从下一个开始
            result.append(piece+delimiter)
        return result

class DicHelper():
    def __init__(self,dic):
        self.dic=dic

    def longestInDic(self):
        longest_length=1
        for item in self.dic:
            temp_length=len(item)
            if temp_length>longest_length:
                longest_length=temp_length
        return longest_length

if __name__=='__main__':
    text='研究生命的起源'
    dic=['研究','研究生','生命','的','起源']
    helper=DicHelper(dic)
    cutter=MMCut(helper.longestInDic())
    print(cutter.cut(text,dic))


