function solution(arr, queries) {
    var answer = [];

    // 각 쿼리에 따라 arr의 원소를 서로 바꿈
    queries.forEach(query => {
        var i = query[0];
        var j = query[1];
        var temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    });

    return arr;
}