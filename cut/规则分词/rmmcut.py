from 规则分词.mmcut import DicHelper


class RMMCut():
    def __init__(self,window_size=1):
        self.window_size=window_size

    def cut(self,text,dic):
        result=[]
        delimiter='--'
        index=len(text)
        while index > 0:
            for size in range(index-self.window_size,index):#从index-window_size增加到index-1位置
                piece=text[size:index]#没找到就会按这个提取最后1个字切开
                if piece in dic:
                    #找到，分词在字典里，index前移动到该分词所在开头位置
                    index=size+1#左闭右开
                    break
            index-=1#①找到，从上次找到次开头的下一个开始;②未找到，切开这个字，从下一个开始
            result.append(piece+delimiter)
        result.reverse()
        return result


if __name__=='__main__':
    text = '研究生命的起源'
    dic = ['研究', '研究生', '生命', '的', '起源']
    helper = DicHelper(dic)
    cutter=RMMCut(helper.longestInDic())
    print(cutter.cut(text,dic))