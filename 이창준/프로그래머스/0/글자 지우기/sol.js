function solution(my_string, indices) {
  let answer = "";

  // 주어진 인덱스를 기준으로 주어진 문자열에서 문자를 삭제하고 남은 문자열을 이어 붙임
  for (let i = 0; i < my_string.length; i++) {
    if (!indices.includes(i)) {
      // 인덱스가 indices 배열에 포함되지 않으면 해당 문자를 answer에 추가
      answer += my_string[i];
    }
  }

  return answer;
}
