function solution(arr) {
  const startIdx = arr.indexOf(2);
  const endIdx = arr.lastIndexOf(2);

  return startIdx + endIdx < 1 ? [-1] : arr.slice(startIdx, endIdx + 1);
}

// 무지성으로 짠 코드
/* 얘는 시간초과로 테스트 실패했음. 그냥 반성용..
function solution(arr) {
    var result = [];
    var idx = []; // 2가 있는 인덱스를 저장하는 배열

    // 배열을 순회하면서 2가 있는 인덱스를 저장
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] === 2) {
            idx.push(i);
        }
    }

    // 2가 하나도 없는 경우
    if (idx.length === 0) {
        result.push(-1);
    } else {
        // 가장 작은 연속된 부분 배열을 찾음
        var minSubArrayLength = idx[idx.length - 1] - idx[0] + 1;

        // 가장 작은 연속된 부분 배열 추출
        for (var j = 0; j <= arr.length - minSubArrayLength; j++) {
            var subArray = arr.slice(j, j + minSubArrayLength);
            if (subArray.filter(num => num === 2).length === idx.length) {
                result = subArray;
                break;
            }
        }
    }

    return result;
}
*/
