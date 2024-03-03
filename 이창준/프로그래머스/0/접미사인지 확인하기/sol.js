function solution(my_string, is_suffix) {
  // my_string의 끝에서부터 is_suffix의 길이만큼의 부분 문자열을 추출
  const suffix = my_string.substring(my_string.length - is_suffix.length);
  // 추출 문자열과 is_suffix비교
  if (suffix === is_suffix) {
    return 1;
  } else {
    return 0;
  }
}
