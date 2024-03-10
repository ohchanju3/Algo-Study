function solution(my_string, queries) {
  let arr = my_string.split("");
  queries.forEach((query) => {
    let [start, end] = query;
    while (start < end) {
      // temp로 start 위치의 문자와 end 위치의 문자를 교환한다.
      let temp = arr[start];
      arr[start] = arr[end];
      arr[end] = temp;
      // 다음 문자로 이동
      start++;
      end--;
    }
  });
  // 문자열 합치기
  return arr.join("");
}
