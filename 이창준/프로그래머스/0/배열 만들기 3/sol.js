function solution(arr, intervals) {
  var answer = [];
  // 첫 번째 구간에 해당하는 부분 배열을 추출하여 answer에 추가
  for (var i = intervals[0][0]; i <= intervals[0][1]; i++) {
    answer.push(arr[i]);
  }
  // 두 번째 구간에 해당하는 부분 배열을 추출하여 answer에 추가
  for (var j = intervals[1][0]; j <= intervals[1][1]; j++) {
    answer.push(arr[j]);
  }
  return answer;
}
