function ismul(num, n){
    let mod = num%n;
    if(mod==0){return 1;} else return 0;
}

function solution(num, n) {

    return ismul(num, n) ? 1 : 0;
}

/*
    삼항연산자를 통해서 바로

    function solution(num, n) {
        return num%n ? 0 : 1;
    }

    로 갈 수도 있음. 이 문제에서는 간단하게 해결되지만, 꼭 한 줄로 끝내려는 것이 좋지 않다고 판단하며 위 풀이에서는 함수를 하나 더 만들어 사용함.
*/