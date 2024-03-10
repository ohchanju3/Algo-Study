function solution(my_string) {
  var answer = new Array(52).fill(0); // 알파벳 개수를 담을 배열 초기화

  // 문자열을 순회하면서 알파벳 개수를 카운트
  for (var i = 0; i < my_string.length; i++) {
    var charCode = my_string.charCodeAt(i); // 현재 문자의 ASCII 코드를 구함
    if (charCode >= 65 && charCode <= 90) {
      // 대문자인 경우
      answer[charCode - 65]++; // 해당 알파벳의 개수를 증가시킴
    } else if (charCode >= 97 && charCode <= 122) {
      // 소문자인 경우
      answer[charCode - 97 + 26]++; // 해당 알파벳의 개수를 증가시킴 (대문자와 구분하기 위해 26을 더함)
    }
  }

  return answer;
}
