#-*-coding:utf-8-*-
import copy
## 처음으로 입력되는 정점개수, 선분개수, 시작점 정보 input에 저장
input=raw_input()
input=input.split()
for x in range(len(input)):
    input[x]=int(input[x])
##그래프를 다중 리스트 형식으로 저장
graph=[]
for x in range(input[0]):
    graph.append([])
for x in range(input[1]):
    imsi=raw_input()
    imsi2=imsi.split()
    first=int(imsi2[0])
    last=int(imsi2[1])
    #if real_last in graph[real_first-1]:
    #    continue
    #if real_first in graph[real_last-1]:
    #    continue
    graph[first-1].append(last)
    graph[last-1].append(first)
##-----------시험
for x in range(len(graph)):
    graph[x].sort()
##grapf 복사
graph_bfs=copy.deepcopy(graph)
#print(graph_bfs)
##변수 설정
answer_dfs=[]
stack=[]
cursor=input[2]
stack.append(cursor)
answer_dfs.append(cursor)
while len(stack)!=0:
    #print(stack)
    #print(answer_dfs)
    #print(graph)
    imsi=stack[len(stack)-1]
    if len(graph[imsi-1])!=0:
        imsi2=graph[imsi-1].pop(0)
        if imsi2 in answer_dfs:
            pass
        else:
            stack.append(imsi2)
            answer_dfs.append(imsi2)
    else:
        stack.pop()
#print(answer_dfs)
#print(answer_dfs)
##bfs
stack=[]
answer_bfs=[]
cursor=input[2]
stack.append(cursor)
#print(graph_bfs)
#answer_bfs.append(cursor)
while len(stack)!=0:
    #print(graph_bfs)
    #print(answer_bfs)
    #print(stack)
    imsi=stack.pop(0)
    if imsi in answer_bfs:
        pass
    else:
        answer_bfs.append(imsi)
    if len(graph_bfs[imsi-1])!=0:
        for x in range(len(graph_bfs[imsi-1])):
            stack.append(graph_bfs[imsi-1].pop(0))
#print(answer_dfs)
#print(answer_bfs)
answerlistdfs=[]
answerlistbfs=[]
for x in range(len(answer_dfs)):
    a1=answer_dfs[x]
    a2=answer_bfs[x]
    stra1=str(a1)
    stra2=str(a2)
    answerlistdfs.append(stra1+" ")
    answerlistbfs.append(stra2+" ")
answer1=""
answer2=""
for x in range(len(answer_dfs)):
    answer1=answer1+answerlistdfs[x]
    answer2=answer2+answerlistbfs[x]
print(answer1[0:len(answer1)-1])
print(answer2[0:len(answer2)-1])