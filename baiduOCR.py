# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 10:35:20 2021

百度tesseract-ocr使用
若第一次使用，需要在cmd中先运行 pip install --user baidu-aip
@author: L380
"""


from aip import AipOcr

""" API """
APP_ID = '23493427'
API_KEY = '7Y6o6s8Yoaaxn8KKnaFNyYoF'
SECRET_KEY = 'veVU7pYAlHRjMqlMl6OVI6lzoKnTLaee'

# 初始化AipFace对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def img_to_str(image_path):

    """ 可选参数 """
    options = {}
    options["language_type"] = "CHN_ENG"  # 中英文混合
    options["detect_direction"] = "true"  # 检测朝向
    options["detect_language"] = "true"  # 是否检测语言
    options["probability"] = "False"  # 是否返回识别结果中每一行的置信度

    image = get_file_content(image_path)

    """ 带参数调用通用文字识别 """
    result = client.basicGeneral(image, options)
    #result = client.basicAccurate(image, options)
    text=''
    # 格式化输出-提取需要的部分
    if 'words_result' in result:
    #    text = ('\n'.join([w['words'] for w in result['words_result']]))
        for w in result['words_result']:
            text += w['words']+'\n'
    
    #print(type(result), "和", type(text))
  
    return text

if __name__ == '__main__':
    imagePath = './imag/sample1.jpg'
    txtPath = './txt/baidu_ocr.txt'
    text=img_to_str(imagePath)
    print(text)
    """ save """
    fs = open(txtPath, 'w+')  # 将str,保存到txt
    fs.write(text)
    fs.close()
    print("识别完成。")
    