from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

def url_to_soup(url):
    res = requests.get(url)
    return BeautifulSoup(res.content, 'html.parser')

def main():
    firstdir = "./단계별로 풀어보기-Python"
    os.makedirs(firstdir, exist_ok=True)

    table = url_to_soup("https://www.acmicpc.net/step").find("table")
    table_a = table.find_all(lambda x: x.name == "a" and x.attrs.get("href"))
    table_a__hrefs = map(lambda x: "https://www.acmicpc.net"+x.attrs["href"], table_a)# 링크
    table_a__gettext = map(lambda x: x.get_text(), table_a)# 폴더명

    for href, foldername, i in zip(table_a__hrefs, table_a__gettext, range(len(table_a))):
        table = url_to_soup(href).find("table")
        df_StepTable = pd.read_html(str(table))[0]
        #표가 이상해서 나누고 다시 합치기
        df_StepTable = pd.concat([
            df_StepTable[::2].reset_index(drop=True), 
            df_StepTable[1::2]["정보"].reset_index(drop=True)], axis=1)
        #해당 주제의 폴더 만들기
        seconddir = f'{str(i+1).zfill(2)}_{foldername}'
        os.makedirs(f'{firstdir}/{seconddir}' ,exist_ok=True)

        for i, num in enumerate(df_StepTable["문제 번호"]):
            #파일명 지정
            filename = f"{firstdir}/{seconddir}/{str(i+1).zfill(2)}_{num}"
            #주석 지정
            title = df_StepTable["제목"][i]
            info = df_StepTable["정보"].iloc[:,-1][i]
            annot = f"#제목: {title}\n#정보: {info}"
            #파일 쓰기
            with open(f"{filename}.py", "w", encoding="utf-8") as w:
                w.write(annot)
                w.close()

if __name__ == '__main__':
    main()