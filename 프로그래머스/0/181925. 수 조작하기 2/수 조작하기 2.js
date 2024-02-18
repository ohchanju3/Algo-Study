function solution(numLog) {
    let answer = '';
    let currentNum = numLog[0]; // 초기 수

    // numLog 배열을 순회하면서 조작에 따른 문자열을 생성
    for (let i = 1; i < numLog.length; i++) {
        const diff = numLog[i] - numLog[i - 1]; // 현재 수와 이전 수의 차이

        // 조작에 따라 문자열에 해당하는 알파벳 추가
        if (diff === 1) {
            answer += 'w'; // 수에 1을 더하는 경우
        } else if (diff === -1) {
            answer += 's'; // 수에 1을 빼는 경우
        } else if (diff === 10) {
            answer += 'd'; // 수에 10을 더하는 경우
        } else if (diff === -10) {
            answer += 'a'; // 수에 10을 빼는 경우
        }
    }

    return answer;
}