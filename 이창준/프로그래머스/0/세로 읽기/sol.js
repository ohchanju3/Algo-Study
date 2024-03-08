function solution(my_string, m, c) {
  var answer = "";

  var arr = [];
  for (var i = 0; i < my_string.length; i += m) {
    arr.push(my_string.substr(i, m));
  }

  for (var j = 0; j < arr.length; j++) {
    answer += arr[j][c - 1];
  }

  return answer;
}
