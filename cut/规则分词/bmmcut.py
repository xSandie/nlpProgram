from 规则分词.mmcut import MMCut, DicHelper
from 规则分词.rmmcut import RMMCut


class BMM():
    def __init__(self,window_size=1):
        self.window_size=window_size

    def cut(self,text,dic):
        delimiter = '--'
        rmmcutter=RMMCut(self.window_size)
        rmm_raw=rmmcutter.cut(text,dic)

        mmcutter=MMCut(self.window_size)
        mm_raw=mmcutter.cut(text,dic)

        rmm_strip=[item.rstrip(delimiter) for item in rmm_raw]
        mm_strip=[item.rstrip(delimiter) for item in mm_raw]

        #返回少的
        if len(rmm_strip)>len(mm_strip):
            return_list=mm_raw
        elif len(rmm_strip)<len(mm_strip):
            return_list=rmm_raw
        else:
            #如果相等返回单字少的
            mm_single_word_count=0
            rmm_single_word_count=0
            for item in mm_strip:
                if len(item)==1:
                    mm_single_word_count+=1
            for item in rmm_strip:
                if len(item)==1:
                    rmm_single_word_count+=1
            if mm_single_word_count<rmm_single_word_count:
                return_list=mm_raw
            else:
                return_list=rmm_raw

        return return_list

if __name__=='__main__':
    text='研究生命的起源'
    dic=['研究','研究生','生命','的','起源']
    helper=DicHelper(dic)
    cutter=BMM(helper.longestInDic())
    print(cutter.cut(text,dic))