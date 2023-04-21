def solution(id_list, report, k):
    answer = []
    
    rep = set(report) # 중복제거
    mail= {m:0 for m in id_list}  #메일 받은 횟수
    repo = {r:0 for r in id_list} #신고당한 횟수
    
        
    for i in rep:  #i에 중복 제거한 값 넣음
        sp = i.split(' ')  #공백기준 제거
        repo[sp[1]]+=1 #신고 당한 아이디를 보고 딕셔너리에 밸류 값을 1 증가시킴
    
    print(repo)
    
    for i in rep:
        sp = i.split(' ')  
        print(sp)
        if repo[sp[1]]>=k:  #만약 신고당한 아이디의 밸류 값이 k보다 크다면
            mail[sp[0]]+=1  #신고한 아이디에 메일 받은 횟수 1을 더해줌
    print(mail)
    answer = mail.values()
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","muzi frodo","muzi frodo","muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))