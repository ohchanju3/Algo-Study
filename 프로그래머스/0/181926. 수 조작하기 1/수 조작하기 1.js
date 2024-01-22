function solution(n, control) {
    for (let i = 0; i < control.length; i++) {
        let char = control[i];
        switch (char) {
            case 'w': 
                n += 1;
                break;
            case 's': 
                n -= 1;
                break;
            case 'd': 
                n += 10;
                break;
            case 'a': 
                n -= 10;
                break;
        }
    }
    return n;
}