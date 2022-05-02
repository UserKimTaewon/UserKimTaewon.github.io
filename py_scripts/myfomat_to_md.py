from constants import FILEPATH,OUTPUTPATH
from typing import Iterable

"""
def convert_lines(lines:Iterable[str])->Iterable[str]:
    g_lvl=1
    for line in lines:
        rgal= '{' in line
        lgal= '}' in line
        if lgar ^ rgal:
            g_lvl+=rgar
            g_lvl-=lgal
            yield '#'*g_lvl+' '+line.replace('{','').replace('}','')
        else:
            yield line
"""
"""
def count_rspace(inp:str):
    cnt=0
    for i,c in enumerate(inp):
        if c!=' ':
            return cnt
        cnt+=1
    return cnt
"""
FOMAL_DICT=[
('ㄱㄴ','가능'),
('그없','그런 거 없음'),
('EU','이유'),
('뭔','무슨'),
('긍께','그러니까'),
('네트웤','네트워크'),
('암튼','아무튼'),

]
def formalize(word):
    for i,j in FOMAL_DICT:
        word=word.replace(i,j)
    return word


def convert_nomal_line(inp,file):
    if '-' in inp:
        r,l=inp.split('-',1)
        if r.isspace() or r=='':
            return print('\t'*(len(r))+'-',l,file=file)
    print(formalize(inp),file=file)

def convert_line_to_file(lines:Iterable[str],file)->None:
    g_lvl=1
    for line in lines:
        rgal= '{' in line
        lgal= '}' in line
        if lgal and rgal:
            convert_nomal_line(line,file=file)
        elif rgal:
            print('#'*g_lvl,line.replace('{',''),file=file)
            g_lvl+=1
        elif lgal:
            g_lvl-=1
            if line.rstrip().lstrip()=='}':
                #print('* * *',file=file)
                pass
            else:
                convert_nomal_line(line.replace('}',''),file=file)
        else:
            convert_nomal_line(line,file=file)

def convert_file(src,dst):
    with open(src,encoding='utf8') as srcf:
        with open(dst,mode='w',encoding='utf8') as dstf:
            convert_line_to_file(srcf,dstf)

def find_files(src):
    return src.glob('[0-9]*.txt')

def convone(src,outpath=OUTPUTPATH):
    convert_file(src,OUTPUTPATH/src.name.replace('.txt','.md'))

if __name__=='__main__':
    for file in find_files(FILEPATH):
        convone(file)
    #toconv=tuple(find_files(FILEPATH))
    #convone(toconv[0])


