function solution(n, slicer, num_list) {
  var answer = [];

  // slicer에 담긴 정수를 a, b, c로 할당
  var a = slicer[0];
  var b = slicer[1];
  var c = slicer[2];

  // n에 따라 슬라이싱 다르게 적용
  switch (n) {
    case 1:
      answer = num_list.slice(0, b + 1);
      break;
    case 2:
      answer = num_list.slice(a);
      break;
    case 3:
      answer = num_list.slice(a, b + 1);
      break;
    case 4:
      answer = num_list.slice(a, b + 1).filter(function (_, index) {
        return index % c === 0;
      });
      break;
  }

  return answer;
}
