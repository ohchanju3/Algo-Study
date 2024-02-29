function solution(intStrs, k, s, l) {
  var answer = [];
  intStrs.forEach((str) => {
    // s 인덱스에서 시작하는 길이 l짜리 부분 문자열을 잘라냄.
    const subStr = str.substring(s, s + l);
    const num = parseInt(subStr, 10);
    // 반환 값이 k보다 큰 경우 answer 배열에 추가
    if (num > k) {
      answer.push(num);
    }
  });
  return answer;
}
