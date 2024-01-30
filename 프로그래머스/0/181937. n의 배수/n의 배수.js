function ismul(num, n){
    let mod = num%n;
    if(mod==0){return 1;} else return 0;
}

function solution(num, n) {

    return ismul(num, n) ? 1 : 0;
}