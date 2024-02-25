function solution(arr, queries) {
    queries.forEach(query => {
        const [s, e, k] = query; // 구조 분해 할당을 사용하여 쿼리의 각 요소를 추출
        // s부터 e까지 반복하며, i가 k의 배수인 경우 arr[i]에 1을 더한다.
        for (let i = s; i <= e; i++) {
            if (i % k === 0) { // i가 k의 배수인지 확인
                arr[i] += 1; // 조건 만족하면 arr[i]에 1을 더한다.
            }
        }
    });
    return arr;
}