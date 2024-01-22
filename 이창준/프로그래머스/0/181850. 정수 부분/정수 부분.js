function solution(flo) {
  var answer = Math.floor(flo);
  return answer;
}

/*
    여기서 사용한 Math에는 ceil, floor, round가 있다. 각각 소수점 반올림, 자름, 반내림이다.
  
    Math를 사용한 방법 이외에도 
    var answer = ~~flo; 
    를 통해 소수점을 자를 수도 있는데, 
    비트 단위의 NOT 연산자를 두 번 사용해 각 비트를 반전시킴으로써 소수점을 자를 수 있다고 한다.

    음수에서 사용할 때 Math.floor의 경우에는 값을 내리고(-1.99 -> -2), ~~는 자르기만 한다.(~~-1.99 -> -1)

    성능만을 따질 때는 ~~를 사용하지만, 명확성과 유지보수를 위해서는 Math.floor을 사용하도록 하자.
    ++
    Math.trunc도 소수를 잘라내는데, 이 의미가 아예 "잘라냄"이다.
    trunc는 음수에서도 ~~와 동일하게 자르기만 하니, 얘를 사용해도 좋을 것 같다.
*/
