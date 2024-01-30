function parsing(a, b){
    let answer = a.toString() + b.toString();
    return parseInt(answer);
}

function solution(a, b) {
    var ans1 = parsing(a,b);
    var ans2 = 2*a*b;
    
    if(ans1>=ans2) {
        return ans1;
    } else return ans2;
    
}