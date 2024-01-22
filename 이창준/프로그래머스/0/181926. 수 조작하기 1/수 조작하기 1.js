function solution(n, control) {
  for (let i = 0; i < control.length; i++) {
    let char = control[i];
    switch (char) {
      case "w":
        n += 1;
        break;
      case "s":
        n -= 1;
        break;
      case "d":
        n += 10;
        break;
      case "a":
        n -= 10;
        break;
    }
  }
  return n;
}

/*
다른 풀이: 객체와 reducer를 사용하여 문제 풀기

const operations = {
  w: (n) => n + 1,
  s: (n) => n - 1,
  d: (n) => n + 10,
  a: (n) => n - 10,
};

function solution(n, control) {
  return [...control].reduce((prev, op) => operations[op](prev), n);
}

*/
