const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input = [line];
}).on("close", function () {
  str = input[0];

  console.log(str);
});

/*
    node.js의 readline모듈을 사용하여 입출력 처리

    ***사용법***
    1. require('readline')을 통해 node.js의 readline 모듈을 불러온다.
    2. readline 인터페이스 생성하기
        readline.createInterface를 통해 readline.Interface인스턴스를 생성한다.
        여기서 input은 입력 스트림 -> process.stdin을 사용
        output은 출력 스트림 -> process.stdoput을 사용
    3. 변수 선언(빈 배열로 선언하여 사용자 입력 데이터를 저장한다.)
    4. line 이벤트 리스너 적용
        rl.on('line', ...)은 새 줄을 입력할 때마다 생성됨.
            콜백 함수는 입력된 줄 'line'을 매개변수로 받음
            입력된 줄을 line배열에 저장함. line=[line];는 input배열을 입력된 한 줄로 설정한다.
        rl.on('close', function)는 입력 스트림이 닫힐 때 호출됨.
            콜백 함수 내에서 input[0]을 str변수에 할당.
            console.log로 입력받은 str을 나타내면 됨.

    ***여러 줄 입력 방법***
rl.on('line', function (line) {
    if (line === 'exit') { // 'exit'를 입력받으면 입력 종료
        rl.close();
    } else {
        input.push(line); // 입력받은 줄을 input 배열에 추가
    }
}).on('close', function() {
    // 입력이 종료되면 input 배열에 저장된 모든 줄을 출력
    input.forEach((line) => {
        console.log(line);
    });
});
*/
