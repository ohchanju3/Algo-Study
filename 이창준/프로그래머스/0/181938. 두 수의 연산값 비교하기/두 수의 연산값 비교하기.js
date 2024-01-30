function parsing(a, b) {
  let answer = a.toString() + b.toString();
  return parseInt(answer);
}

function solution(a, b) {
  var ans1 = parsing(a, b);
  var ans2 = 2 * a * b;

  if (ans1 >= ans2) {
    return ans1;
  } else return ans2;
}

/** 다른 사람 풀이 참고
    function solution(a, b) {
        let num1 = parseInt(a+""+b+"");
        let num2 = 2*a*b;
        return num1 > num2 ? num1 : num2;
    }
    여기서 num1을 만들 때 a+""를 해주는 것은 스트링으로 변환을 해주는 것이다.
    따라서 solution(a, b)로 들어온 Number타입의 변수를 parseInt함수에 넣어서 사용할 때,
    그 인자를 a+""와 b+""를 사용함으로써 String 타입인 a와 b를 사용하는 것이 된다.

    이는, a와 b가 연산되는 것이 아니라, String을 더해 두 글자를 붙이는 작용이 된다.
    이렇게 붙여진 a와 b로 이루어진 String을 parseInt를 통해 Number로 만드는 것이 let num1의 동작 순서이다.

    return에서 삼항연산자 쓴 것도 참고하면 좋을 듯 하다.
    if문을 통해 바로 return을 시켜도 되지만, 삼항 연산자가 조금 더 명확해보임.

 */
