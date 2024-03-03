function solution(l, r) {
    var answer = [];
    for (var i = l; i <= r; i++) {
        // 숫자를 문자열로 변환
        var numStr = i.toString();
        // 정규표현식으로 숫자가 0과 5로만 구성되어 있는지 확인
        if (/^[0,5]+$/.test(numStr)) {
            answer.push(i);
        }
    }
    // 만족하지 않으면 -1반환
    if (answer.length === 0) {
        return [-1];
    }
    return answer;
}
