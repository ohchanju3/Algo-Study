function solution(my_string, k) {
  let strArr = [];
  for (let i = 0; i < k; i++) {
    strArr.push(my_string);
  }
  var answer = strArr.join("");

  return answer;
}

/*
    var answer = my_string.repeat(k);
    return answer;
    
    또는

    return my_string.repeat(k);

    로 간단하게 나타낼 수도 있다. 반복문이 생각날 때 습관적으로 for문을 떠올리지 말고
    repeat도 있음을 인식해야겠다.
*/
