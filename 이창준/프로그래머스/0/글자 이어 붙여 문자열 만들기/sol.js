function solution(my_string, index_list) {
  var answer = "";
  // index_list의 각 원소에 대해 루프 실행
  for (var i = 0; i < index_list.length; i++) {
    // my_string에서 해당 인덱스의 문자를 answer에 추가
    answer += my_string[index_list[i]];
  }
  return answer;
}
