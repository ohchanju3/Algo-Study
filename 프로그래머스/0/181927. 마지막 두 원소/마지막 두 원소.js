function solution(num_list) {
    var answer = num_list.slice(); // 입력 리스트를 복사하여 answer 변수에 할당
    
    // 주어진 리스트의 마지막 원소가 그전 원소보다 큰지 확인하고, 그에 따라 처리
    if (answer[answer.length - 1] > answer[answer.length - 2]) {
        answer.push(answer[answer.length - 1] - answer[answer.length - 2]); // 마지막 원소에서 그전 원소를 뺀 값을 추가
    } else {
        answer.push(answer[answer.length - 1] * 2); // 마지막 원소를 두 배한 값을 추가
    }
    
    return answer;
}
