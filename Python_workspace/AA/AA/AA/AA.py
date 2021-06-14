from collections import defaultdict
answer  = []
cnt = 0
# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"], ["ICN","AAA"],["AAA","BBB"],["IAD","ICN"]]

'''
ICN:[(AAA,0),(JFK,0)] 
JFK:[(HND,0)]
HND:[(IAD,0)]
IAD:[(ICN,0)]
AAA:[(BBB)]
'''
# 스택을 사용한 DFS
def dfs(routes, start, ticketSize,moveCnt):
    if moveCnt == ticketSize or start not in routes:

        return answer
    elif moveCnt <ticketSize:
        for toValueInfo in routes[start]:
            if toValueInfo[1]: continue # 방문 했으면 다음 티켓 정보 확인
            if toValueInfo[0] in routes:
            moveCnt += 1
            dfs(routes, toValueInfo[0],ticketSize,moveCnt)




def solution(tickets):
    ticketSize = len(tickets)
    # 해쉬 딕셔너리로 tickets 정보 인접 리스트 그래프로 표현
    routes = defaultdict(list)
    for fromKey, toValue in tickets: 
        routes[fromKey].append((toValue,0))
        
    for rKey in routes:
        routes[rKey].sort()
    
    answer.append("ICN")
    dfs(routes,"ICN",ticketSize,0)
    answer.extend(routes[answer[-1]])
    
    return answer

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"], ["ICN","AAA"],["AAA","BBB"],["IAD","ICN"]]

print(solution(tickets))