function solution(tickets) {
    var answer = [];
    // 출발지를 ICN 이면
    // 출발지가 ICN엔인거 찾아서 dfs
    const ans = []
    
    function dfs(result, unusedTickets) {
        if (unusedTickets.length === 0) {
            ans.push(result)
        }
        for (const i in unusedTickets) {
            if (result[result.length-1] === unusedTickets[i][0]) {
                var tmp = result.concat([unusedTickets[i][1]])
                var tmp2 = unusedTickets.filter((ticket, index) => index != i)
                dfs(tmp, tmp2)
            }
            
        }
    }
    dfs(['ICN'], tickets)
    ans.sort()
    answer = ans[0]
    return answer;
}