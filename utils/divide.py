import jieba


def read_txt():
    with open("../news/xinhuanet_latest_news.txt", "r", encoding="gb2312") as f:  # 打开文件
        data = f.read()  # 读取文件
        print(data)
    return data


# jieba.enable_paddle()

def stop_words_list():
    stopwords = [line.strip() for line in open('../news/hit_stopwords.txt', encoding='UTF-8').readlines()]
    return stopwords


# 对句子进行中文分词
def seg_depart(sentence):
    # 对文档中的每一行进行中文分词
    # print("正在分词")
    sentence_depart = jieba.cut(sentence.strip())
    # 创建一个停用词列表
    stopwords = stop_words_list()
    # 输出结果为outstr
    outstr = ''
    # 去停用词
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


if __name__ == "__main__":
    filename = "../news/xinhuanet_latest_news.txt"
    outfilename = "../news/out.txt"
    inputs = open(filename, 'r', encoding='utf-8')
    outputs = open(outfilename, 'w', encoding='utf-8')
    # 将输出结果写入out.txt中
    for line in inputs:
        line_seg = seg_depart(line)
        outputs.write(line_seg + '\n')
        # print("-------------------正在分词和去停用词-----------")
    outputs.close()
    inputs.close()
    print("删除停用词和分词成功！！！")
