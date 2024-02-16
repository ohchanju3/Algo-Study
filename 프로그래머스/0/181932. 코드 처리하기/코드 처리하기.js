function solution(code) {
    var ret = '';
    var mode = 0;

    for (var idx = 0; idx < code.length; idx++) {
        if (code[idx] === '1') {
            mode = 1 - mode; 
        } else {
            if (mode === 0 && idx % 2 === 0) {
                ret += code[idx]; 
            } else if (mode === 1 && idx % 2 !== 0) {
                ret += code[idx];
            }
        }
    }

    return ret === '' ? 'EMPTY' : ret;
}
