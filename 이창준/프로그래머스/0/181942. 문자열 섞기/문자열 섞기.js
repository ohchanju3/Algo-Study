function solution(str1, str2) {
    var answer = '';
    for(let i=0; i<str1.length; i++){
        answer += str1[i]+str2[i];
    }
    return answer;
}

/*
    ***다른 사람 풀이***
    return [...str1].map((x, idx)=> x+str2[idx]).join("");

    ***설명***
    str1과 str2의 길이는 같다. 따라서 idx가 갈 수 있는 범위도 같다.
    str1에서 map으로 하나씩 뽑은 x와, 그 x가 있는 인덱스 번호인 idx를 이용하여
    str2에는 index번호인 idx를 이용해 같은 위치에 있는 글자를 뽑는다.

    두 글자를 뽑은 후 join("")을 통해 공백문자와 함께 join하여 문자열을 합친다.

*/