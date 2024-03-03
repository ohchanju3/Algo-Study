function solution(arr, queries) {
    var answer = [];

    // 각 쿼리에 대해 처리
    for (var q = 0; q < queries.length; q++) {
        var query = queries[q];
        var start = query[0];
        var end = query[1];
        var k = query[2];
        var min = -1; // 기본적으로 -1로 설정

        // 주어진 범위 내에서 k보다 크면서 가장 작은 값 찾기
        for (var i = start; i <= end; i++) {
            if (arr[i] > k && (min === -1 || arr[i] < min)) {
                min = arr[i];
            }
        }

        // 결과 배열에 저장
        answer.push(min);
    }

    return answer;
}