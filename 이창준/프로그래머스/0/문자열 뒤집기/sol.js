function solution(my_string, s, e) {
  // s부터 e까지의 부분 문자열을 추출
  var substr = my_string.substring(s, e + 1);

  // 뒤집기
  var reversed_substr = substr.split("").reverse().join("");

  return (
    my_string.substring(0, s) + reversed_substr + my_string.substring(e + 1)
  );
}
